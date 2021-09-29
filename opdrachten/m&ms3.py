import random

MenMs = ['oranje', 'blauw', 'groen', 'bruin']
zak = []
hoeveelkleuren = 0

mnmDictionaryBag = {'oranje': 0, 'blauw': 0, 'groen': 0, 'bruin': 0, }


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

if not'oranje' in zak:
    mnmDictionaryBag.pop('oranje')
if not'blauw' in zak:
    mnmDictionaryBag.pop('blauw')
if not'groen' in zak:
    mnmDictionaryBag.pop('groen')
if not'bruin' in zak:
    mnmDictionaryBag.pop('bruin')

print(zak)
print('')
for key, value in mnmDictionaryBag.items():
    print(key, value)
print('')
print(len(zak))

print('-----------!gesorteerd!------------')


def sorteren(soort):
    if soort == 'lijst':
        print(sorted(zak))
    elif soort == 'boek':
        sort_orders = sorted(mnmDictionaryBag.items(), key=lambda x: x[1])
        for i in sort_orders:
            print(i[0], i[1])


sorteren(soort='lijst')
print('')
sorteren(soort='boek')
