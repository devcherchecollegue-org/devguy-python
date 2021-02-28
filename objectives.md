Attentes :
- Grue31
  - Approfondir ma connaissance de la DDD (mise en pratique et méthode)
  - Faire du test voire du TDD
  - Pratique de la formation et du mentoring
  - Découvrir kotlin
  - Jouer avec discord

- Maestro31 :
  - Aider les plus juniors à atteindre l'objectif
  - Me permettre d'expérimenter DDD (archi haxagonale) sur un projet de taille raisonnable
  - Permettre aux juniors non encore en entreprise d'apprendre à travailler sur un vrai projet (outils, gestion, ...)

- Rakops : 
    - Faire du kotlin :D
    - Si je peux découvrir le TDD/DDD je suis preneur

- Neonima:
    - Etait devops dans la passé, c'etait un peu la galere sans python :P Donc pourquoi pas réctifier ça!
    - Ce qui m'attire avec ce projet c'est de pouvoir créer pleins de commandes fun
    - Voir un projet qui evolue et pouvoir y apporter ma patte

Expérience :
    Python :
        - Grue31 : confirmé/senior (~2/3 ans d'xp) (activité principale)
        - Maestro31 : des notions lointaines
        - Neonima : N/A - mais senior sur d'autre lang
        - Rakops : je sais faire une boucle for
    Java/Kotlin :
        - Rakops : 5/7 ans Java avec 1.5 ans de Kotlin
        - Grue31 : 6 mois de Java il y a 4 ans (c'est lointain)
        - Maestro31 : intermédiaire

Fonctionnement:
- Fonctionnement par point étape :
  - Présentation des développements
  - Revue des codes
  - Validation d'une version pour merge vers le main (ou mise en place d'une PR)
  - Définition des prochains objectifs
  - Evolution progressive du fonctionnement

- Structure du projet :
  - Branche principale sans paradigme (pas de limitation DDD ou autre)
  - Aucune restriction pour mettre en place des paradigmes et les présenter aux autres

- Structure du repo :
  - 1 repo par langage
  - Branche principale (main/master)
  - Chacun son fork et possibilité d'avoir des branches dédiées sur le repo principal
  - Chaque branche privée est préfixée par private

- Règles du repo :
  - Commits en anglais
  - PR approvals : tout le monde doit approuver ou dire balek (LGTM!)

Objectifs prochain point étape :
1 - Objectif fonctionnel: se familiariser avec le bot discord

2 - Message aux nouveaux arrivants
    1 - Message par défaut
    2 - Doit pouvoir faire <@user> celui qui vient d'arriver
    3 - Doit pouvoir pointer vers des channels
    4 - Optionel - Paramétrable par l'admin
        - Paramétrable coté serveur
        - Paramétrable depuis une commande discord
    5 - Optionel - Possibilité de d'avoir un message random parmis une liste fournie

3 - Attribution des roles par réaction
    - [Action] Commande qui spawn un message contenant des réactions
    - [Action] Si un utilisateur clique sur une réaction, ça lui assigne un role dépendant de la réaction
    - [Configuration] L'admin peut associer des roles à des réactions
    - [Configuration] L'admin peut paramétrer quelles réactions s'affichent dans ce message
    - [Configuration] L'admin peut paramétrer le layout du message



Feature complete:
1 - Message aux nouveaux arrivants
    1 - Message par défaut
    2 - Doit pouvoir faire <@user> celui qui vient d'arriver
    3 - Doit pouvoir pointer vers des channels
    4 - Optionel - Paramétrable par l'admin
        - Paramétrable coté serveur
        - Paramétrable depuis une commande discord
    5 - Optionel - Possibilité de d'avoir un message random parmis une liste fournie

2 - Attribution des roles par réaction
    - [Action] Commande qui spawn un message contenant des réactions
    - [Action] Si un utilisateur clique sur une réaction, ça lui assigne un role dépendant de la réaction
    - [Configuration] L'admin peut associer des roles à des réactions
    - [Configuration] L'admin peut paramétrer quelles réactions s'affichent dans ce message
    - [Configuration] L'admin peut paramétrer le layout du message

3 - Attribution d'xp et de niveau
    - XP de participation à la guilde :
        - en fonction du nombre de messages postés
            - pouvoir définir un nombre max d'xp gagné par jour / semaine / mois
    - XP de pertinence
        - en fonction de certaines réactions prédéfinies (comme les awards reddit)
    - Formule de calcul paramétrable
    - Pouvoir paramétrer tout ça :)

4 - Morpion
    - C'est un morpion
    - On verra plus tard

5 - Quand Octavius est en train d'écrire, le bot écrit "la ferme, le boss écrit" et supprime tous les nouveaux messages

6 - Une backdoor pour Rakops ( et pour Grue :) )

7 - Modération 
    - Modifier les messages qui contiennent un email ou numéro -> remplacer par **********

