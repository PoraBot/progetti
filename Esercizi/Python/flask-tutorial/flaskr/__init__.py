# Ad ogni avvio usare questi comandi per far trovare la directory a flask
# Entri nella cartella con cd : cd "C:\Users\consporazziandrea\Documents\Esercizi Python\flask-tutorial"
# $env:FLASK_APP = "flaskr"
# $env:FLASK_ENV = "development"
# flask init-db
# flask run

import os

from flask import Flask

#Create_app è la function che fa da application factory
def create_app(test_config=None):
    #Crea l'istanza di Flask, __name__ è il nome del modulo Python usato, istance_relative_config=True indica che i file di configurazione
    # sono relativi alla istance folder.
    app = Flask(__name__, instance_relative_config=True)
    app.config.from_mapping(
        SECRET_KEY='dev',
        DATABASE=os.path.join(app.instance_path, 'flaskr.sqlite'),
    )

    if test_config is None:
        # Se è presente un file di configurazione lo carica e sovrascrive quello di default
        app.config.from_pyfile('config.py', silent=True)
    else:
        # Carica la configurazione di test se presente
        app.config.from_mapping(test_config)

    # Controlla se è presente la cartella app.istance_path, se non è presente la crea se no skippa
    try:
        os.makedirs(app.instance_path)
    except OSError:
        pass

    # Cuore dell'app, crea una pagina html con scritto "Benvenuto in Flask!" dentro ad una funzione
    @app.route('/hello')
    def hello():
        return 'Benvenuto in Flask!'

    #Importo db e lo inizializzo
    from . import db
    db.init_app(app)

    # Importo il blueprint auth e lo registro usando app.register_blueprint()
    from . import auth
    app.register_blueprint(auth.bp)

    # Importo il blueprint dal factory usando app.register_blueprint(), essendo il blog la feature
    # principale di questo esempio, ha senso mettere il suo index come main index.
    from . import blog
    app.register_blueprint(blog.bp)
    app.add_url_rule('/', endpoint='index')

    return app