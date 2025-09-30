# Lista de los 10 equipos con más Champions League ganadas
equipos_champions = [
    {"equipo": "Real Madrid", "títulos": 15, "país": "España"},
    {"equipo": "AC Milan", "títulos": 7, "país": "Italia"},
    {"equipo": "Bayern Múnich", "títulos": 6, "país": "Alemania"},
    {"equipo": "Liverpool", "títulos": 6, "país": "Inglaterra"},
    {"equipo": "FC Barcelona", "títulos": 5, "país": "España"},
    {"equipo": "Ajax", "títulos": 4, "país": "Países Bajos"},
    {"equipo": "Manchester United", "títulos": 3, "país": "Inglaterra"},
    {"equipo": "Inter de Milán", "títulos": 3, "país": "Italia"},
    {"equipo": "Chelsea", "títulos": 2, "país": "Inglaterra"},
    {"equipo": "Oporto", "títulos": 2, "país": "Portugal"},
]

# Imprimir índice de equipos
print("🏆 Top 10 Equipos con Más Champions League\n")
for i, club in enumerate(equipos_champions, start=1):
    print(f"{i}. {club['equipo']} - {club['títulos']} títulos ({club['país']})")
