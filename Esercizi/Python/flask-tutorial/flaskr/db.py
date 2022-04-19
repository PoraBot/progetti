#Import di SQLite 3
import sqlite3

import click
from flask import current_app, g
from flask.cli import with_appcontext

def get_db():
    #L'oggetto g è un oggetto speciale unico per ogni richiesta, è usato per contenere dati che potrebbero 
    # essere usati da altre funzioni durante la richiesta. La connesione è salvata e riutilizzata piuttosto 
    # di creare una seconda connessione se get_db è chiamata una seconda volta nella stessa richiesta.
    if 'db' not in g:
        g.db = sqlite3.connect(
            # current_app è un oggetto speciale che punta alla applicazione Flask che si occupa di gestire
            # la richiesta, visto che si è usata una application factory non c'è bisogno di altri oggetti
            # applicazione mentre scrivi il resto del tuo codice.
            current_app.config['DATABASE'],
            detect_types=sqlite3.PARSE_DECLTYPES
        )
        g.db.row_factory = sqlite3.Row

    return g.db

def init_db():
    #get_db richiama la connessione al database, che è usato per eseguire i comandi dal file
    db = get_db()
    # Apre un file relativo al flaskr package, è utile perchè così non devi sapere dove si trova esso quando
    # fai il deploy della app.
    with current_app.open_resource('schema.sql') as f:
        db.executescript(f.read().decode('utf8'))
# click.command definisce un comando nella command line chiamato init-db, che richiama la funzione init_db 
# e mostra un messaggio di successo all'utente
@click.command('init-db')
@with_appcontext
def init_db_command():
    """Clear the existing data and create new tables."""
    init_db()
    click.echo('Initialized the database.')

# Questa funzione controlla se c'è una connessione creata controllando se g.db è impostato, se esiste la chiude
def close_db(e=None):
    db = g.pop('db', None)

    if db is not None:
        db.close()

# Dopo che abbiamo creato le funzioni close_db e init_db_command, devono essere registrate nella istanza
# dell'applicazione se no non possono essere usate dalla app. Quindi creo una funzione che prende l'app
# e fa la registrazione.
def init_app(app):
    # Dice a flask di chiamare la funzione close_db quando pulisce dopo aver ricevuto una risposta
    app.teardown_appcontext(close_db)
    # Aggiunge un nuovo comando che può essere ciamato usando il comando flask
    app.cli.add_command(init_db_command)