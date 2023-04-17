class LogsModel:
    def __init__(self):
        pass

    def serialize_player(player):
        serialized_player = {
            "Prénom": player["first_name"],
            "Nom de famille": player["last_name"],
            "Date de naissance": player["birthdate"],
            "Numéro national d'échec": player["chess_id"],
            "score": player["score"],
        }
        return serialized_player

    def serialize_tournament(tournament, players, rounds):
        serialized_tournament = {
            "Nom du tournoi": tournament["name"],
            "Localisation": tournament["location"],
            "Date de début": tournament["start_date"],
            "Date de fin": tournament["end_date"],
            "Joueurs": players,
            "Notes": tournament["notes"],
            "Nombre de Rounds": tournament["rounds"],
            "Round actuel": tournament["current_round"],
            "Liste des rounds": rounds,
        }
        return serialized_tournament

    def serialize_tournament_infos(tournament):
        serialized_tournament = {
            "Nom du tournoi": tournament["name"],
            "Localisation": tournament["location"],
            "Date de début": tournament["start_date"],
            "Date de fin": tournament["end_date"],
            "Notes": tournament["notes"],
            "Nombre de Rounds": tournament["rounds"],
            "Round actuel": tournament["current_round"],
        }
        return serialized_tournament

    def serialize_round(round, matches):
        serialized_round = {
            "Numéro de round": round["round_number"],
            "Horaire de début": round["start_time"],
            "Horaire de fin": round["end_time"],
            "Matchs": matches,
        }
        return serialized_round

    def serialize_match(match):
        player1 = match["players"][0]
        player2 = match["players"][1]
        scoreP1 = match["score"][0]
        scoreP2 = match["score"][1]

        serialized_match = {
            "Nom du match": match["name"],
            "Joueurs": f"{player1} contre {player2}",
            "Score": f"{scoreP1} | {scoreP2}",
            "Gagnant": match["winner"],
        }
        return serialized_match
