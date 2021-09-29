import random
MenMs = ['oranje', 'blauw', 'groen', 'bruin']
zak = []
hoeveelkleuren = 0

mnmDictionaryBag = {'oranje': 0,'blauw': 0,'groen': 0,'bruin': 0,}


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
        if kleur == 'oranje':
            mnmDictionaryBag['oranje'] += 1
        elif kleur == 'blauw':
            mnmDictionaryBag['blauw'] += 1
        elif kleur == 'groen':
            mnmDictionaryBag['groen'] += 1
        elif kleur == 'bruin':
            mnmDictionaryBag['bruin'] += 1


randomkleur()
print(zak)
print(mnmDictionaryBag)
print(len(zak))