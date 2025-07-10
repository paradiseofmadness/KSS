import random

def zza(wechseln=True):
    # die 3 Türen (0, 1, 2)
    türen = [0, 1, 2]
    # wählt zufällig eine der Türen für da Auto aus
    auto = random.randint(0, 2)
    # Spieler wählt eine der Türen
    choise = random.randint(0, 2)
    # Moderator öffnet eine der Türen,
    # außer der mit dem Auto und der Wahl des Spielers
    reveal = random.choice([t for t in türen if t != auto and t != choise])
    # Spieler Wechselt oder nicht je nach Strategie
    if wechseln:
        # setz die Wahl des Spielers auf die Türe die nicht geöffnet wurde
        # und er vorher nicht gewählt hatte
        choise = [t for t in türen if t != choise and t != reveal][0]
    # gibt zurück ob der Spieler gewonnen hat
    return choise == auto

if __name__ == "__main__":
    mw = 0
    ow = 0
    for _ in range(1000):
        if zza():
            mw += 1
        if zza(False):
            ow += 1
    print("Prozent Gewonnen (nicht Wechseln):", ow/1000)
    print("Prozent Gewonnen (Wechseln):", mw/1000)