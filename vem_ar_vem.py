import random

medlemmar = ["MangeMungo", "Borksson", "Flarmenko", "Viking Line", "C-mannen", "ShwindelyShwundely"]
roller = ["Mamma", "Pappa", "Joel", "Märta", "Klara", "Farfar"]

priser = ["Paketpris 1", "Paketpris 2", "Sista ner 1", "Sista ner 2", "Första hem 1", "Första hem 2"]

random.shuffle(medlemmar)

for i in range(len(medlemmar)):
    print(roller[i] + " spelas dennan resa av " + medlemmar[i])

print()

random.shuffle(roller)

for i in range(len(medlemmar)):
    print(priser[i] + " vanns denna gången av " + roller[i])
