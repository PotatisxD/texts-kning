import os  # Importerar os-modulen


def main():
    searchpath = input('Ange sökväg: ')  # Användaren anger sökvägen
    wordName = input('Ange sökord: ')  # Användaren anger sökordet

    searchfolderandfiles(searchpath, wordName)  # funktionen för att leta efter sökordet i sökvägen körs

    print('Resultat är sparat i resultat.txt!')


def searchfolderandfiles(path, word):  # Funktion som söker igenom mappar och filer
    for filename in os.listdir(path):  # for loop som går igenom allt i sökvägen
        fullPath = os.path.join(path, filename)  # Sätter ihop sökvägen och filen
        if os.path.isfile(fullPath):  # Ifall det är en specific fil körs olika funktioner:
            if fullPath.endswith('.txt'):  # Med txt-filer körs readtextfile funktionen
                readtextfile(fullPath, word)

            elif fullPath.endswith('.csv'):  # Med csv-filer körs readcsvfile funktionen
                readcsvfile(fullPath, word)

            elif fullPath.endswith('.plist'):  # Med plist-filer körs readplistfile funktionen
                readplistfile(fullPath, word)
        if os.path.isdir(fullPath):  # Om det är en mapp körs funktionen om igen, men i den nya mappen
            searchfolderandfiles(fullPath, word)


def readtextfile(txtpath, word):
    textfile = open(txtpath, 'r')  # Öppnar txt filen
    for textoffile in textfile:  # for loop som kollar texten i filen
        if word in textoffile:  # Om sökordet finns i texten sparas sökvägen och sökordet i resultat.txt
            resultat = open('resultat.txt', 'a')
            resultat.write(
                'Sökväg: ' + txtpath + '\n' + 'sökord: ' + word + '\n' + '\n')
            resultat.close()
            print('Sökväg: ' + txtpath + '\n' + 'sökord: ' + word + '\n' + '\n')  # Skriver ut resultat till användaren


def readcsvfile(csvpath, word):
    textfile = open(csvpath, 'r')  # Öppnar csv filen
    for textoffile in textfile:  # for loop som kollar texten i filen
        if word in textoffile:  # Om sökordet finns i texten sparas sökvägen och sökordet i resultat.txt
            resultat = open('resultat.txt', 'a')
            resultat.write(
                'Sökväg: ' + csvpath + '\n' + 'sökord: ' + word + '\n' + '\n')
            resultat.close()
            print('Sökväg: ' + csvpath + '\n' + 'sökord: ' + word + '\n' + '\n')  # Skriver ut resultat till användaren


def readplistfile(plistpath, word):
    textfile = open(plistpath, 'r')  # Öppnar filen
    for textoffile in textfile:  # for loop som kollar texten i filen
        if word in textoffile:  # Om sökordet finns i texten sparas sökvägen och sökordet i resultat.txt
            resultat = open('resultat.txt', 'a')
            resultat.write(
                'Sökväg: ' + plistpath + '\n' + 'sökord: ' + word + '\n' + '\n')
            resultat.close()
            print(
                'Sökväg: ' + plistpath + '\n' + 'sökord: ' + word + '\n' + '\n')  # Skriver ut resultat till användaren


main()
