import random

medlemmar = ["MangeMungo", "Borksson", "Flarmenko", "Viking Line", "C-mannen", "ShwindelyShwundely"]
roller = ["Mamma", "Pappa", "Joel", "Märta", "Klara", "Farfar"]

# priser = ["Paketpris 1", "Paketpris 2", "Sista ner 1", "Sista ner 2", "Första hem 1", "Första hem 2"]
priser = ["Första ner", "Andra ner", "Första hem", "Andra hem"]

random.shuffle(medlemmar)

redteam = ["Tom", "Tom"]
goldteam = []

for i in range(len(medlemmar)):
    print(roller[i] + " spelas dennan resa av " + medlemmar[i])
    # Special hack for special people
    if medlemmar[i] == "MangeMungo":
        redteam[0] = roller[i]
    elif medlemmar[i] == "ShwindelyShwundely":
        redteam[1] = roller[i]
    else:
        goldteam.append(roller[i])
    if medlemmar[i] == "Viking Line":
        TibbeChar = roller[i]

print()

# random.shuffle(roller)
random.shuffle(goldteam)
while goldteam[-1] == TibbeChar:
    random.shuffle(goldteam)

print("Paketpris vanns denna gången av " + redteam[0])
print("Sista ner vanns denna gången av " + redteam[1])
for i in range(len(goldteam)):
    print(priser[i] + " vanns denna gången av " + goldteam[i])
