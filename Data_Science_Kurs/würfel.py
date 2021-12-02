import random
import time

"""Das Ziel ist es die eingegebene Zahl zu würfeln"""


spieler_score = 0

while True:

    Würfel = ("1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12")
    Würfel = random.choice(Würfel)
    Spieler = input("Wähle deine Zahl die du würfeln möchtest : ")
    print("Spieler würfelt")
    time.sleep(3)
    print(Würfel)

    if Würfel == Spieler:
        spieler_score = spieler_score+100
        print("Punktestand: Spieler:", spieler_score)
    else:
        spieler_score = spieler_score-100
        print("Punktestand: Spieler:", spieler_score)
        print()
