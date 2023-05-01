[![forthebadge](https://forthebadge.com/images/badges/made-with-python.svg)](https://forthebadge.com)

## [OpenClassrooms] - Projet 4 : Développer un programme logiciel en Python

As part of the Openclassrooms [Python software developer program](https://openclassrooms.com/fr/paths/518-developpeur-dapplication-python)

### Chess Club

## Prerequisites for installation

- [Python3](https://www.python.org/downloads/)
- Pip3 (If Python3 is installed, you can install pip3 with `python -m pip3 install`)

### Dependencies

The dependencies and their versions are listed in the `requirements.txt` but mainly, it requires:

- tinydb
- flake8

## Installing and lauching

1. Clone or download the content of [this repository](https://github.com/Mimi1706/HanNguyen_4_130223)
2. (⚠️ Please make sure you're in the right directory for the next steps)
3. Create your environment with `Python3 -m venv env` (the recommended name is env)
4. Activate your environement with `source env/bin/activate`
5. Install the dependencies for your environment with `pip3 install -r requirements.txt`
6. Make sure you're in the right folder then launch `main.py` by writing in your terminal `python3 main.py`

To generate a flake8 report in HTML format, write `flake8 --format=html --htmldir=flake-report` in your terminal, the report will generate itself in a flake-report directory.

## Using the program

# To create players

- Select option 2 "Gérer la base de données de joueurs"
- Create a player with option 1 "Créer un joueur"
- The created player will be saved in the database "db_players.json"

# To create a tournament

- Select option 1 "Gérer les tournois"
- Create a tournament with option 1 "Créer un nouveau tournoi"

# To create a round

- After creating a tournament, select ("Gérer les tournois" ->) "Continuer un tournoi"
- Load your tournament
- Create a new round with option 1 ("Gérer les tournois" ->) "Créer un nouveau round"

# To score a match

- After creating a round, the players will be paired together in matches
- Select ("Gérer les tournois" -> "Continuer un tournoi" ->) "Entrer les scores du round en cours" and score the matches

# To consult reports

- You can consult tournament reports and the player database from the main menu with option 3 "Consulter les rapports"
