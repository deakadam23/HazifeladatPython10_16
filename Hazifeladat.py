
def tizenotos():
    while True:
        szam = int(input('Adj meg egy szamot!'))
        if szam < 0 and szam % 3 == 0:
            print('A szam negativ es oszhato harommal, befejezem a bekerest')
def tizenhatos():
    while True:
      szam = int(input('Adj meg egy szamot'))
      if szam > 100 and szam < 999:
        print('A szam haromjegyu es pozitiv, befejezem a szamlalast.')
def tizennyolcas():
 szoveg = input("Adj meg egy szoveget")
 szoveg2 = input("Adj meg egy szoveget")
 szoveg3 = input("Adj meg egy szoveget")
 szoveg4 = input("Adj meg egy szoveget")
 szoveg5 = input("Adj meg egy szoveget")

 eredmeny = ' '.join([szoveg, szoveg2, szoveg3, szoveg4, szoveg5])
 print(eredmeny)

def tizenkilences():
 szamok = []
 for i in range(5):
    num = float(input(f"Ird be az {i + 1} szamot "))
    szamok.append(num)
 eredmeny = min(szamok)
 print(f"A legkisebb szam: {eredmeny}")

def huszas():
    szamok = []
    for i in range(5):
        num = int(input(f"Ird be az {i + 1}. szamot: "))
        szamok.append(num)

    # Ellenőrizzük, hogy van-e páros szám a listában
    paros_van = any(num % 2 == 0 for num in szamok)

    if paros_van:
        print("Van páros szám a megadott számok között.")
    else:
        print("Nincs páros szám a megadott számok között.")

def huszonegy():
    szamok = []
    for i in range(5):
        num = int(input(f"Ird be az {i + 1}. szamot: "))
        szamok.append(num)

    # Ellenőrizzük, hogy van-e páros szám a listában
    paros_van = any(num % 2 == 0 for num in szamok)
    paros_szamok = [num for num in szamok if num %2 == 0]
    if paros_van:
        print("Van páros szám a megadott számok között.")
        print(f"{paros_szamok}")
    else:
         print("Nincs paros szam a megadott szamok kozott")
def kettesBfeladat():
    honap = int(input('Adj meg egy szamot 12 es 1 kozott: '))

    if honap == 12:
        print('December')
    elif honap == 11:
        print('November')
    elif honap == 10:
        print('Oktober')
    elif honap == 9:
        print('Szeptember')
    elif honap == 8:
        print('Augusztus')
    elif honap == 7:
        print('Julius')
    elif honap == 6:
        print('Junius')
    elif honap == 5:
        print('Majus')
    elif honap == 4:
        print('Aprilis')
    elif honap == 3:
        print('Marcius')
    elif honap == 2:
        print('Februar')
    elif honap == 1:
        print('Januar')
    else:
        print('HIBA! Csak 1 - 12 kozotti szamokat adhatsz meg')