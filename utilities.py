#Rotation data column names
rotations_table_header = ["vehicle", "town", "date", "time", "net_extra", "gap", "net_cet", "tare", "brute", "ticket", "cet"]

#dict of column names and renaming rules
rotations_table_renaming = {
                    "véhicule": "vehicle",
                    "matricule": "vehicle",
                    "t/ véh": "tare",
                    "t/ véhi": "tare",
                    "tare véhicule": "tare",
                    "t/véhicule": "tare",
                    "tare véh": "tare",
                    "commune": "town", 
                    "nom client": "town",
                    "heure": "time",
                    "heure 1": "time",
                    "h/ 1": "time",
                    "n ticket": "ticket", 
                    "n tick": "ticket",
                    "n/ ticket": "ticket",
                    "numéro ticket": "ticket",
                    "bon": "ticket",
                    "n° bon": "ticket",
                    "net cet": "net_cet",
                    'poids net': 'net_cet',
                    "p/ net": "net_cet",
                    'p/net': 'net_cet',
                    "net extr": "net_extra",
                    "net extra": "net_extra",
                    "extra net": "net_extra",
                    "net extranet": "net_extra",
                    "poids extra": "net_extra",
                    "pesée 1 (kg)": "brute",
                    "p/ 1 (kg)": "brute",
                    "brut": "brute",
                    "ecart": "gap",
                    "écart": "gap",
                    "différence": "gap",
                    "diff": "gap",
}

#dict of column names and types
rotations_table_types = {
        "vehicle" : str,
        "town": str,
        "gap" : float,
        "date": str,
        "time" : str,
        "ticket" : str,
        "net_cet": float,
        "net_extra": float,
        "tare": float,
        "brute": float,
        "cet": str
    }

#Algiers town names
towns_list = [
     "Alger-Centre",
     "Sidi M'Hamed", 
     "El Madania", 
     "Belouizdad", 
     "Bab El Oued", 
     "Bologhine", 
     "Casbah", 
     "Oued Koriche", 
     "Bir Mourad Raïs", 
     "El Biar", 
     "Bouzareah", 
     "Birkhadem", 
     "El Harrach", 
     "Baraki", 
     "Oued Smar", 
     "Bachdjerrah", 
     "Hussein Dey", 
     "Kouba", 
     "Bourouba", 
     "Dar El Beïda", 
     "Bab Ezzouar", 
     "Ben Aknoun", 
     "Dely Ibrahim", 
     "El Hammamet", 
     "Raïs Hamidou", 
     "Djasr Kasentina", 
     "El Mouradia", 
     "Hydra", 
     "Mohammadia", 
     "Bordj El Kiffan", 
     "El Magharia", 
     "Beni Messous",
     "Les Eucalyptus", 
     "Birtouta", 
     "Tessala El Merdja", 
     "Ouled Chebel", 
     "Sidi Moussa", 
     "Aïn Taya", 
     "Bordj El Bahri", 
     "El Marsa", 
     "H'Raoua", 
     "Rouïba", 
     "Reghaïa", 
     "Aïn Benian", 
     "Staoueli", 
     "Zeralda", 
     "Mahelma", 
     "Rahmania", 
     "Souidania", 
     "Cheraga", 
     "Ouled Fayet", 
     "El Achour",
     "El Hamiz", 
     "Draria",
     "Douera",
     "Baba Hassen",
     "Khraicia",
     "Saoula"
]

#some town names abbreviations
town_abbreviations = {
    "bez": "Bab Ezzouar",
    "bek": "Borj El Kiffan",
    "deb": "Dar El Beïda",
    "beb": "Borj El Bahri",
}

#stop words for towns names
town_stop_words = [
    "Apc",
    "Extranet",
    "netcom",
    "net com",
    "EPIC",
    "N IDENTIFIE",
    "ABS CET",
    "CET",
    "ABS",
    "OPERATION AUTOROUTE"
]
