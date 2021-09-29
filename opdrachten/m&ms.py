import random
MenMs = ['oranje', 'blauw', 'groen', 'bruin']
zak = []
hoeveelkleuren = 0


def randomkleur():
    global hoeveelkleuren
    f = True
    while f:
        try:
            hoeveelkleuren = int(input("Hoeveel M&M's moeten er aan deze zak worden toegevoegd?\n"))
            if int(hoeveelkleuren) <= 0:
                print('Dat is geen getal boven nul!')
        except ValueError:
            print('Dat is geen geldige invoer!')
        if hoeveelkleuren > 0:
            f = False

    for i in range(hoeveelkleuren):
        getal = random.choice(range(0, 4))
        kleur = MenMs[getal]
        zak.append(kleur)


randomkleur()
print(zak)
print(len(zak))
