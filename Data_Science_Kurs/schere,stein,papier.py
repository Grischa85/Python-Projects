import random

spieler_score = 0
computer_score = 0

while True:
    Computer = ('Schere', 'Stein', 'Papier')
    Computer = random.choice(Computer)
    Spieler = input("Bitte Schere, Stein oder Papier auswählen "
                    "oder 'q' für Beenden: ")
    if Spieler == ('q'):
        print("Endstand:")
        print("Punktestand: Spieler:", spieler_score)
        print("Punktestand: Computer:", computer_score)
        if spieler_score > computer_score:
            print("Spieler hat gewonnen")
        elif spieler_score == computer_score:
            print("Unentschieden")
        else:
            print("Computer hat gewonnen")
        break
    if Spieler == 'Schere' or 'Stein' or 'Papier':
        print("Computer: " + Computer)
        if Spieler == "Spieler hat gewonnen":
            spieler_score = spieler_score+1
        if Computer == "Computer hat gewonnen":
            computer_score = computer_score+1

        # Spieler gewinner
        if Computer == 'Stein' and Spieler == 'Papier':
            print("Spieler hat gewonnen")
            spieler_score = spieler_score+1
            print("Punktestand: Spieler:",spieler_score, "|", "Punktestand: Computer:",computer_score)
        if Computer == 'Schere' and Spieler == 'Stein':
            print("Spieler hat gewonnen")
            spieler_score = spieler_score + 1
            print("Punktestand: Spieler:", spieler_score, "|",  "Punktestand: Computer:", computer_score)
        if Computer == 'Papier' and Spieler == 'Schere':
            print("Spieler hat gewonnen")
            spieler_score = spieler_score + 1
            print("Punktestand: Spieler:", spieler_score, "|",  "Punktestand: Computer:", computer_score)

        # Computer gewinner
        if Computer == 'Stein' and Spieler == 'Schere':
            print("Computer hat gewonnen")
            computer_score = computer_score + 1
            print("Punktestand: Spieler:", spieler_score, "|",  "Punktestand: Computer:", computer_score)
        if Computer == 'Schere' and Spieler == 'Papier':
            print("Computer hat gewonnen")
            computer_score = computer_score + 1
            print("Punktestand: Spieler:", spieler_score, "|",  "Punktestand: Computer:", computer_score)
        if Computer == 'Papier' and Spieler == 'Stein':
            print("Computer hat gewonnen")
            computer_score = computer_score + 1
            print("Punktestand: Spieler:", spieler_score, "|",  "Punktestand: Computer:", computer_score)

        # Unentschieden
        if Computer == 'Stein' and Spieler == 'Stein':
            print("Unentscheiden")
            print("Punktestand: Spieler:", spieler_score)
            print("Punktestand: Computer:", computer_score)
        if Computer == 'Schere' and Spieler == 'Schere':
            print("Unentschieden")
            print("Punktestand: Spieler:", spieler_score)
            print("Punktestand: Computer:", computer_score)
        if Computer == 'Papier' and Spieler == 'Papier':
            print("Unentschieden")
            print("Punktestand: Spieler:", spieler_score)
            print("Punktestand: Computer:", computer_score)