# byebyedevbot

Bot Discord collaboratif du serveur **Dev Cherche Collègue**

Pour collaborer efficacement, chaque collaborateur est responsable de se créer un Serveur Discord et d'inviter un bot créé à partir de son propre compte Discord.

Les étapes du bot sont documentées dans cette vidéo : [créer un bot discord](https://www.youtube.com/watch?v=AeCytN_eQII)
En cas de besoin la documentation officielle de Discord : [documentation](https://discord.com/developers/docs/intro)

On est également à votre disposition sur le canal textuel byebyedevbot pour vous aider à réaliser toutes ces étapes.


## Cas d'usage
Pour tester sur votre serveur privé:
- Créer un bot avec tous les droits
- Invitez le bot sur votre serveur
- Renseigner la clé secrète dans le futur .env
- Créez 2 roles de test
- Créez 1 emoji custom nommé : `custom_emoji1` et récupérez son id.
- Ajuster les CONSTANTES GLOBALES de `discrod_client.py` aux valeurs de votre serveur (à déplacer plus tard dans une persistance: .env, .ini, BDD...)
  - ROLE_TEST1_ID: l'id du premier role de test
  - ROLE_TEST2_ID: l'id du deuxième role de test
  - EMOJI_CUSTOM1_ID: l'id de `custom_emoji1`
  - BOT_ADMIN_USER_ID: votre id sur votre serveur privé (vous autorise à créer un nouveau message à réactions)
- Lancez le bot `python3 main.py`
- Dans le channel de votre choix tapez `! set_role_picker'
- Un message du bot devrait apparaitre avec les emotes configurées dans les CONSTANTES GLOBALES.

## Configuration de l'environnement client

Création de l'environnement virtuel local

```bash
python3 -m venv venv
```

Création d'un fichier .env pour les variables locales

```bash
cat > .env <<EOF
DISCORD_BOT_SECRET_KEY=<YOU-DISCORD-BOT-SECRET-KEY>
EOF
```

Activation de l'environnement (Linux et Mac)

```bash
source venv/bin/activate
```

Activation de l'environnement (Windows Powershell)

```powershell
venv\bin\activate.ps1
```

Installation des dépendances

```bash
pip3 install -r requirements.txt
```

## Utilisation de l'environnement de développement


Installation des dépendances de test

```bash
pip3 install - r requirements-dev.txt
```

Exécuter le linter

```bash
pylama main.py app/*
```

Exécuter les tests

```bash
python3 -m pytest
```

## Lancer le bot
Pas de notion prod et développement pour le moment, c'est un protoype !

```
python3 main.py
```
