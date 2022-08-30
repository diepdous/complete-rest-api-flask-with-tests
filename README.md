# BOILERPLATE FLASK API

Ce boilerplate contient la structure d'une API Flask complète avec gestion de Token pour l'authentification des requêtes. Les données sont stockées dans une base de données PostgreSQL. 
La documentation de l'API est générée à l'aide de l'outil APIDOC. 
Les tests sont gérés à l'aide du module pytest. 


## pile Docker

Il faut se placer dans le dossier scripts_bash

### démarrage pile
'''bash
./dcTool dev up
'''

### arrêt pile en conservant les données de la bdd
'''bash
./dcTool dev down
'''

### arrêt pile en supprimant les données de la bdd
'''bash
./dcTool dev down -v
'''

### pour se connecter au conteneur http (flask)
'''bash
./connect_flask_container_dev.sh
'''

### pour se connecter au conteneur db (postgresql)
'''bash
./connect_postgres_container_dev.sh
'''

### pour générer la documentation de l'API
'''bash
./create_apidoc.sh
'''


## accès serveur

Le serveur flask est automatiquement lancé à l'adresse : http://127.0.0.0.1:5000/api

La documentation est disponible à l'adresse : http://127.0.0.0.1:5000/api/docs