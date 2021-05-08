# devguy

![CI Status](https://github.com/devcherchecollegue-org/devguy-python/actions/workflows/main.yaml/badge.svg?branch=main)
[![Coverage Status](https://coveralls.io/repos/github/devcherchecollegue-org/devguy-python/badge.svg?branch=main)](https://coveralls.io/github/devcherchecollegue-org/devguy-python?branch=main)
[![security: bandit](https://img.shields.io/badge/security-bandit-yellow.svg)](https://github.com/PyCQA/bandit)

<!-- TOC -->

- [devguy](#devguy)
  - [Cas d'usage](#cas-dusage)
  - [Setup des environnement](#setup-des-environnement)
  - [Lancer le bot](#lancer-le-bot)

<!-- /TOC -->

Bot Discord collaboratif du serveur **Dev Cherche Collègue**

Pour collaborer efficacement, chaque collaborateur est responsable de se créer un Serveur Discord et d'inviter un bot
créé à partir de son propre compte Discord.

Les étapes du bot sont documentées dans cette
vidéo : [créer un bot discord](https://www.youtube.com/watch?v=AeCytN_eQII)
En cas de besoin la documentation officielle de Discord : [documentation](https://discord.com/developers/docs/intro)

On est également à votre disposition sur le canal textuel byebyedevbot pour vous aider à réaliser toutes ces étapes.

## Cas d'usage

Pour tester sur votre serveur privé:

- Créer un bot avec tous les droits
- Inviter le bot sur votre serveur
- Renseigner la clé secrète dans le futur .env
- Créer des roles à assigner et récupérer leurs IDs
- Assigner à chaque emoji un role et dans le cas d'un emoji custom son id dans le fichier `emoji_to_roles.json` au
  format:

```json
{
  "<emoji_name>": {
    "emoji_id": <emoji_id>,
    "role_id": <role_id>
  },
  ...
}
```

- Lancer le bot `python3 main.py`
- Dans le channel de votre choix taper `! set_role_picker'
- Un message du bot devrait apparaitre avec les emotes configurées dans `emoji_to_roles.json`.

## Setup des environnement

- `make setup_dev`

## Lancer le bot

Pas de notion prod et développement pour le moment, c'est un protoype !

- copy .env.sample into .env
- fill .env
- `make run`
