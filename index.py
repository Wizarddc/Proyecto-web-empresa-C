# Lista de partidos simulados de fútbol
partidos_futbol = [
    {"equipos": "Valencia vs Real Oviedo", "hora": "20:00", "competición": "LaLiga EA Sports"},
    {"equipos": "Atalanta vs Club Brujas", "hora": "18:45", "competición": "Champions League"},
    {"equipos": "Real Madrid vs Kairat Almaty", "hora": "18:45", "competición": "Champions League"},
    {"equipos": "Chelsea vs Benfica", "hora": "21:00", "competición": "Champions League"},
    {"equipos": "Colombia Sub-20 vs Arabia Saudí Sub-20", "hora": "Finalizado", "competición": "Mundial Sub-20"},
    {"equipos": "Espanyol vs Real Betis", "hora": "05/10", "competición": "LaLiga EA Sports"},
    {"equipos": "Palermo vs Venezia", "hora": "20:30", "competición": "Serie B"},
    {"equipos": "Orlando vs TS Galaxy", "hora": "19:30", "competición": "Betway Premiership"},
    {"equipos": "Napoli vs Milan", "hora": "17:30", "competición": "Betway Premiership"},
    {"equipos": "Napoli vs Lecce", "hora": "19:30", "competición": "Betway Premiership"},
    {"equipos": "Bodo vs Tottenham Hotspurs", "hora": "19:30", "competición": "Champions League"},
]

# Lista de partidos simulados de la NBA
partidos_nba = [
    {"equipos": "Lakers vs Warriors", "hora": "02:00", "competición": "NBA Regular Season"},
    {"equipos": "Celtics vs Heat", "hora": "01:30", "competición": "NBA Regular Season"},
    {"equipos": "Bulls vs Bucks", "hora": "02:00", "competición": "NBA Regular Season"},
    {"equipos": "Nuggets vs Suns", "hora": "03:00", "competición": "NBA Regular Season"},
    {"equipos": "Knicks vs Raptors", "hora": "01:00", "competición": "NBA Regular Season"},
    {"equipos": "76ers vs Cavaliers", "hora": "01:30", "competición": "NBA Regular Season"},
    {"equipos": "Mavericks vs Clippers", "hora": "03:30", "competición": "NBA Regular Season"},
    {"equipos": "Grizzlies vs Pelicans", "hora": "02:30", "competición": "NBA Regular Season"},
    {"equipos": "Hawks vs Magic", "hora": "00:30", "competición": "NBA Regular Season"},
    {"equipos": "Trail Blazers vs Timberwolves", "hora": "04:00", "competición": "NBA Regular Season"},
]

# Lista de partidos simulados de tenis
partidos_tenis = [
    {"equipos": "Carlos Alcaraz vs Jannik Sinner", "hora": "16:00", "competición": "ATP Tokio"},
    {"equipos": "Novak Djokovic vs Daniil Medvedev", "hora": "18:00", "competición": "ATP Pekín"},
    {"equipos": "Casper Ruud vs Holger Rune", "hora": "14:30", "competición": "ATP Shanghái"},
    {"equipos": "Stefanos Tsitsipas vs Andrey Rublev", "hora": "17:15", "competición": "ATP Viena"},
    {"equipos": "Taylor Fritz vs Alexander Zverev", "hora": "15:45", "competición": "ATP Basilea"},
    {"equipos": "Rafael Nadal vs Dominic Thiem", "hora": "20:00", "competición": "Exhibición Mallorca"},
    {"equipos": "Frances Tiafoe vs Ben Shelton", "hora": "13:00", "competición": "ATP Estocolmo"},
    {"equipos": "Karen Khachanov vs Lorenzo Musetti", "hora": "12:30", "competición": "ATP Amberes"},
    {"equipos": "Hubert Hurkacz vs Alex de Minaur", "hora": "19:00", "competición": "ATP París"},
    {"equipos": "Matteo Berrettini vs Félix Auger-Aliassime", "hora": "21:00", "competición": "ATP Turín"},
]

# Imprimir índice de partidos de fútbol
print("📅 Índice de Partidos de Fútbol\n")
for i, partido in enumerate(partidos_futbol, start=1):
    print(f"{i}. {partido['equipos']} - {partido['hora']} ({partido['competición']})")

# Imprimir índice de partidos NBA
print("\n🏀 Índice de Partidos NBA\n")
for i, partido in enumerate(partidos_nba, start=1):
    print(f"{i}. {partido['equipos']} - {partido['hora']} ({partido['competición']})")

# Imprimir índice de partidos de tenis
print("\n🎾 Índice de Partidos de Tenis\n")
for i, partido in enumerate(partidos_tenis, start=1):
    print(f"{i}. {partido['equipos']} - {partido['hora']} ({partido['competición']})")
