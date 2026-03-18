world_cup_finals = [
    {"year": 1930, "winner": "Uruguay", "score": "4-2", "runner_up": "Argentina", "host": "Uruguay"},
    {"year": 1934, "winner": "Italy", "score": "2-1 (aet)", "runner_up": "Czechoslovakia", "host": "Italy"},
    {"year": 1938, "winner": "Italy", "score": "4-2", "runner_up": "Hungary", "host": "France"},
    {"year": 1950, "winner": "Uruguay", "score": "2-1", "runner_up": "Brazil", "host": "Brazil"},
    {"year": 1954, "winner": "West Germany", "score": "3-2", "runner_up": "Hungary", "host": "Switzerland"},
    {"year": 1958, "winner": "Brazil", "score": "5-2", "runner_up": "Sweden", "host": "Sweden"},
    {"year": 1962, "winner": "Brazil", "score": "3-1", "runner_up": "Czechoslovakia", "host": "Chile"},
    {"year": 1966, "winner": "England", "score": "4-2 (aet)", "runner_up": "West Germany", "host": "England"},
    {"year": 1970, "winner": "Brazil", "score": "4-1", "runner_up": "Italy", "host": "Mexico"},
    {"year": 1974, "winner": "West Germany", "score": "2-1", "runner_up": "Netherlands", "host": "West Germany"},
    {"year": 1978, "winner": "Argentina", "score": "3-1 (aet)", "runner_up": "Netherlands", "host": "Argentina"},
    {"year": 1982, "winner": "Italy", "score": "3-1", "runner_up": "West Germany", "host": "Spain"},
    {"year": 1986, "winner": "Argentina", "score": "3-2", "runner_up": "West Germany", "host": "Mexico"},
    {"year": 1990, "winner": "West Germany", "score": "1-0", "runner_up": "Argentina", "host": "Italy"},
    {"year": 1994, "winner": "Brazil", "score": "0-0 (3-2 pen)", "runner_up": "Italy", "host": "United States"},
    {"year": 1998, "winner": "France", "score": "3-0", "runner_up": "Brazil", "host": "France"},
    {"year": 2002, "winner": "Brazil", "score": "2-0", "runner_up": "Germany", "host": "South Korea / Japan"},
    {"year": 2006, "winner": "Italy", "score": "1-1 (5-3 pen)", "runner_up": "France", "host": "Germany"},
    {"year": 2010, "winner": "Spain", "score": "1-0 (aet)", "runner_up": "Netherlands", "host": "South Africa"},
    {"year": 2014, "winner": "Germany", "score": "1-0 (aet)", "runner_up": "Argentina", "host": "Brazil"},
    {"year": 2018, "winner": "France", "score": "4-2", "runner_up": "Croatia", "host": "Russia"},
    {"year": 2022, "winner": "Argentina", "score": "3-3 (4-2 pen)", "runner_up": "France", "host": "Qatar"}
]

# Example: Print all winners
for final in world_cup_finals:
    print(f"In {final['year']}, {final['winner']} defeated {final['runner_up']} with a score of {final['score']}.")
    