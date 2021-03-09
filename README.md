# devguy

Bot Discord collaboratif du serveur **Dev Cherche Collègue**

Pour collaborer efficacement, chaque collaborateur est responsable de se créer un Serveur Discord et d'inviter un bot créé à partir de son propre compte Discord.

Les étapes du bot sont documentées dans cette vidéo : [créer un bot discord](https://www.youtube.com/watch?v=AeCytN_eQII)
En cas de besoin la documentation officielle de Discord : [documentation](https://discord.com/developers/docs/intro)

On est également à votre disposition sur le canal textuel byebyedevbot pour vous aider à réaliser toutes ces étapes.

## Configuration de l'environnement client

Création de l'environnement virtuel local

```
$ python3 -m bot-env venv
```

Activation de l'environnement (Linux et Mac)

```
$ source bot-env/bin/activate
```

Activation de l'environnement (Windows Powershell)

```
$ bot-env\bin\activate.ps1
```

Installation des dépendances

```
$ pip3 install -r requirements.txt
```

## Utilisation de l'environnement de développement

Exécuter le linter

```
$ pylama
```

Exécuter les tests

```
$ python3 -m pytest
```

Mettre à jour le fichier de dépendance

```
$ pip3 freeze > requirements.txt
```

## Lancer le bot

_Libre à chacun d'utiliser un alias ou une variable d'environnement globale pour éviter de devoir spécifier l'environnement à chaque lancement_

```
$ BOT_ENV=development python3 main.py
```
