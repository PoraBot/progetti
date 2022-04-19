# Visto che il nostro progetto è usabile solo sul nostro computer, noi possiamo fare in modo che questo 
# progetto diventi come un pacchetto python, distribuibile e gestibile da esso.
# Installare da anche altri benefit come ad esempio puoi importarlo e quindi lo puoi eseguire ovunque, 
# non solo dalla cartella del progetto, puoi anche gestire le dipendenze e isolarlo per effettuare test su
# di esso. Di solito si dovrebbe partire sempre con questo.

from setuptools import find_packages, setup

setup(
    name='flaskr',
    version='1.0.0',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    install_requires=[
        'flask',
    ],
)