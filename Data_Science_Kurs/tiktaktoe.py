import random
import time

Feld = ["0",
        "1", "2", "3",
        "4", "5", "6",
        "7", "8", "9"]

run = True

def Spielfeld():
    print(Feld[1] + "|" + Feld[2] + "|" + Feld[3])
    print(Feld[4] + "|" + Feld[5] + "|" + Feld[6])
    print(Feld[7] + "|" + Feld[8] + "|" + Feld[9])


def Spiel():
    Spieler1 = int(input("Spieler 1 \nbitte Zahl eingeben: "))
    if Spieler1 >= 1 and Spieler1 <= 9:
        if Feld[Spieler1] == "X" or Feld[Spieler1] == "O":
            print("Spielzug nicht moeglich")
            return
        Feld[Spieler1] = "X"
    else:
        print("Spielzug nicht moeglich")
        return
    Spielfeld()
    print()
    time.sleep(0.25)

    # Computer
    print("Spieler 2 \nwaehlt ein Feld aus")
    time.sleep(1)
    Spieler2 = random.randint(1, 9)
    for i in range(1, 9):
        if Spieler2 >= 1 and Spieler2 <= 9:
            if Feld[Spieler2] == "X" or Feld[Spieler2] == "O":
                Spieler2 = Spieler2 + 1
                if (Spieler2 > 9):
                    Spieler2 = 1
            else:
                Feld[Spieler2] = "O"
                break;

        if (i == 8):
            print("Spielzug nicht moeglich")
            return


def check_win():
    if  Feld[1] == Feld[2] == Feld[3]:
        return Feld[1]
    if Feld[4] == Feld[5] == Feld[6]:
        return Feld[4]
    if Feld[7] == Feld[8] == Feld[9]:
        return Feld[7]

    #Spalten prüfen
    if Feld[1] == Feld[4] == Feld[7]:
        return Feld[1]
    if Feld[2] == Feld[5] == Feld[8]:
        return Feld[2]
    if Feld[3] == Feld[6] == Feld[9]:
        return Feld[3]

    # Diagonale prüfen
    if Feld[1] == Feld[5] == Feld[9]:
        return Feld[1]
    if Feld[3] == Feld[5] == Feld[7]:
        return Feld[3]


while run:
    Spielfeld()
    Spiel()
    winner = check_win()
    if winner:
        print("Spieler" + winner + " hat gewonnen")
        Neues_Spiel = input("Neues Spiel ? ")
        if Neues_Spiel == "ja":
            run = False