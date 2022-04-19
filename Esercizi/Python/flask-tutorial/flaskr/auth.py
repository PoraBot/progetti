# Una funzione view è il codice che scrivi per rispondere alla richieste della tua app. Flask usa 
# pattern per matchare le richieste URL in arrivo alla view che se ne dovrebbe occupare. La view restituisce
# dati che Flask trasforma in una risposta continua. Flask può anche fare il contrario e generare un URL
# per una view basandosi sul nome e gli argomenti.

# Un Blueprint è un modo per organizzare un gruppo di views connesse e altro codice. Piuttosto che registrare
# le views e altro codice direttamente con un applicazione, si registrano tramite blueprint.
# In seguito il blueprint è registrato con l'app quando è disponibile nella funzione factory.

import functools

from flask import (
    Blueprint, flash, g, redirect, render_template, request, session, url_for
)
from werkzeug.security import check_password_hash, generate_password_hash

from flaskr.db import get_db

# Questo crea un Blueprint chiamato 'auth', proprio come un application object, il blueprint deve sapere
# dov'è definito, quindi __name__ è passato come secondo argomento, url_prefix sarà associato a tutti gli
# URL associato con questo blueprint. Questo blueprint ha le views per registrare nuovi utenti e per 
# log-in e log-out.

bp = Blueprint('auth', __name__, url_prefix='/auth')

# Quando l'utente visita l'URL /auth/register, la register view ritornerà un HTML con un form per loro da
# compilare. Quando loro inviano un form, verrà validato il loro imput e mostrerà di nuovo il form con un 
# messaggio di errore o crea un nuovo utente e lo porta alla pagina di login.

# bp.route associa l'URL /register con la funzione view register. QUando flask riceve una richiesta da 
# /auth/register chiama la register view e usa il return value come risposta.
@bp.route('/register', methods=('GET', 'POST'))
def register():
    # Se l'utente invia un form, request.method sarà 'POST', in questo caso può iniziare a validare l'imput
    if request.method == 'POST':
        # request.form è un tipo speciale di dict formato da key e value, l'utente qui inserirà il loro
        # username e password.
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None

        #Controlla se username e password sono vuoti
        if not username:
            error = 'Username is required.'
        elif not password:
            error = 'Password is required.'

        # Se i dati sono validi, inserisci i nuovi dati dell'utente dentro al database
        if error is None:
            try:
                #db.execute prende una query SQL con "?" come placeholders che verranno rimpiaziati dall'input
                # dell'utente, che è una coppia chiave valore. La libreria database si occuperà di prevenire
                # attacchi SQL injection. 
                db.execute(
                    "INSERT INTO user (username, password) VALUES (?, ?)",
                    # Per sicurezza le password non dovrebbero essere mai salvate diretttamente nel database,
                    # si unsa infatti generate_password_hash() per fare l'hashing della pw e salva l'hash.
                    (username, generate_password_hash(password)),
                )
                # Visto che questa query modifica i dati, db.commit() deve essere chiamata per salvare
                # i cambiamenti effettuati.
                db.commit()
            #Questo errore accade quando un username è già registrato
            except db.IntegrityError:
                error = f"User {username} is already registered."
            else:
                # Dopo aver salvato l'utente, essi vengono reindirizzati alla pagina di login, url_for()
                # genera l'URL per la login view basandosi sul nome, è meglio che scrivere l'URL diretto
                # perchè puoi cambiare l'URL senza dover cambiare tutto il codice che è colelgato ad esso.
                # redirect() genera una redirection response al URL generato.
                return redirect(url_for("auth.login"))
        # Se la validazione dei dati fallisce, l'errore è mostrato all'utente. flash() contiene messaggi 
        # che possono avvenire mentre si inseriscono i dati.
        flash(error)
    # Quando l'utente va all'URL auth/register oppure ha un validation error, una pagina HTML con il form
    # per l'iscrizione dovrebbe apparire, render_template() crea un template contenendo un HTML.
    return render_template('auth/register.html')

#Definisco un altro Blueprint per il login
@bp.route('/login', methods=('GET', 'POST'))
def login():
    #In questo caso l'utente inserisce i dati che vengono salvati in una variabile per essere usata in seguito
    #  
    if request.method == 'POST':
        username = request.form['username']
        password = request.form['password']
        db = get_db()
        error = None
        #fetchone() restituisce una riga dalla query, se la query restituisce nessun risultato, ritorna None.
        # In seguito fetchall() verrà usato per restituire una lista con tutti i risultati.
        user = db.execute(
            'SELECT * FROM user WHERE username = ?', (username,)
        ).fetchone()

        if user is None:
            error = 'Incorrect username.'
        # check_password_hash() usa lo stesso metodo di hashing che è stato usato per salvare la password e 
        # compara il risutato, se sono uguali la password è valida
        elif not check_password_hash(user['password'], password):
            error = 'Incorrect password.'

        # session è un dict che archivia dati tra le varie richieste. Quando la verifica dei dati ha successo,
        # l'id dell'utente è archiviato in una nuova sessione. Questo dato è archiviato in un cookie  che 
        # viene poi inviato ad un broserm e il browse lo reinvia in caso di richieste. Flask firma i dati 
        # in modo da evitare l'eventuale modifica.
        if error is None:
            session.clear()
            session['user_id'] = user['id']
            return redirect(url_for('index'))

        # Ora che l'ID è salvato nella sessione, potrà essere usato per le successive richieste. Per ogni 
        # richiesta, se l'utente è loggato, queste informazioni vengono caricate e usate per le altre views.

        flash(error)

    return render_template('auth/login.html')

# Creiamo una view che registra una funzione che si avvia prima della view function, indipendentemente dall'
# URL richiesto. load_logged_in_user controlla se un user id è contenuto nella sessione e ottiene i dati
# dell'utente dal database, inserendolo all'interno di g.user, che dura per tutta la richiesta. Se non ci sono
# user id, o se l'ID non esistem g.user viene impostato come None.
@bp.before_app_request
def load_logged_in_user():
    user_id = session.get('user_id')

    if user_id is None:
        g.user = None
    else:
        g.user = get_db().execute(
            'SELECT * FROM user WHERE id = ?', (user_id,)
        ).fetchone()

# Per eseguire il logout bisogna rimuovere lo user id dalla sessione e in seguito load_logged_in_user non
# carica un utente per le richieste successive.
@bp.route('/logout')
def logout():
    session.clear()
    return redirect(url_for('index'))

# Creare, modificare e cancellare post sul blog richiedono un utente di loggare, un decorator può essere usato
# per controllare questo per ogni view che viene applicato.
# Questo decorator restituisce una nuova view function che avvolge la view originale a cui viene applicata.
# Questa nuova funzione controlla se un utente è caricato e lo ridireziona alla login page se non lo è.
# Se un utente è caricato la view orginiale viene chiamata e continua normalmente.
def login_required(view):
    @functools.wraps(view)
    def wrapped_view(**kwargs):
        if g.user is None:
            # url_for() è una funzione che genera un URL ad una view vasandosi sul nome e sull'argomento.
            # Il nome associato ad una view è anche chiamato endpoint, e di default  è lo stesso nome della
            # view function. Quando si usa un blueprint, il nome del blueprint è anteposto al nome della
            # funzione, quindi l'endpoint per la funzione di login scritta è 'auth.login' perchè è inserita
            # nella 'auth' blueprint.
            return redirect(url_for('auth.login'))

        return view(**kwargs)

    return wrapped_view
