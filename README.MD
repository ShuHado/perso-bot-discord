# Bot Discord avec [Discord.py](https://discordpy.readthedocs.io/en/latest/)

## Installation :

### Prérequis :

-   Python 3.6 ou supérieur
-   Un compte Discord
-   Un IDE (PyCharm, Visual Studio Code, Atom, etc.)

### Installation :

-   Télécharger le projet en zip ou en clonant le projet
-   Ouvrez et éxécuter la commande ``npm install`` ( ou ``npm i`` pour les adeptes des commandes abrégée) dans le dossier du projet
-   Créer un fichier ``.env`` à la racine du projet
    -   Créer une variable ``TOKEN`` et y mettre le token de votre bot que vous pouvez trouver sur le site de Discord Developer
-   Éxécutez la commande ``npm run start`` (ou ``npm start``) pour lancer le bot

## Fonctionnalités :

-   Affiche ``Bot is ready.`` dans la console lorsque le bot est prêt
-   Affiche le préfixe du bot dans la console lorsqu'il est prêt

## Commandes :

-   ``!hello`` : Envoie ``Hello World!`` dans le channel où la commande a été envoyée
-   ``!serverinfo`` ou ``!si`` : Envoie des informations sur le serveur dans le channel où la commande a été envoyée


## Datas Infos :

-   ``ctx.author`` : L'objet de l'auteur du message
    -   ``.id`` : L'ID de l'auteur du message
    -   ``.name`` : Le nom de l'auteur du message
-   ``ctx.guild`` : L'objet du serveur
    -   ``.id`` : L'ID du serveur
    -   ``.name`` : Le nom du serveur
    -   ``.owner`` : L'objet du propriétaire du serveur
        -   ``.id`` : L'ID du propriétaire du serveur
        -   ``.name`` : Le nom du propriétaire du serveur
    -   ``.members`` : La liste des membres du serveur
        -   ``.id`` : L'ID du membre
        -   ``.name`` : Le nom du membre
    -   ``.channels`` : La liste des salons du serveur
        -   ``.id`` : L'ID du salon
        -   ``.name`` : Le nom du salon
    -   ``.roles`` : La liste des rôles du serveur
        -   ``.id`` : L'ID du rôle
        -   ``.name`` : Le nom du rôle

