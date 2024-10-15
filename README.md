# SQL Injection Blind Script

Ce script Python effectue une attaque de type "Blind SQL Injection" sur une cible web en utilisant des requêtes POST pour extraire le mot de passe d'un utilisateur spécifique (par défaut `admin`). Il permet de déterminer la longueur du mot de passe et d'extraire chaque caractère un par un en utilisant des requêtes SQL conditionnelles.

## Fonctionnalités

- Détecte la longueur du mot de passe à partir de la base de données.
- Utilise une attaque "Blind SQL Injection" pour extraire le mot de passe.
- Supporte les caractères alphanumériques et les symboles.
- Affiche chaque caractère trouvé et calcule le temps total nécessaire à l'exécution.

## Installation

Avant d'exécuter le script, assurez-vous d'avoir Python 3.x et les modules nécessaires installés. Vous pouvez installer les dépendances via `pip` :

```bash
pip install requests argparse
```

## Utilisation
Lancer le script
Le script se lance depuis la ligne de commande en passant l'URL cible et les données de connexion sous forme de JSON :

```bash
python3 script.py -u <url_cible> -d '<données_connexion>'
```

Exemple
Supposons que vous souhaitiez attaquer une URL à l'adresse http://example.com/login avec les données de connexion suivantes :

```bash
python3 script.py -u http://example.com/login -d '{"username":"admin","password":"anything"}'
```

 
