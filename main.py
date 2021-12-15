import docx  # Importerar modul som läser docx-filer

import os  # Importerar os-modulen


def main():
    searchpath = input('Ange sökväg: ')  # Användaren anger sökvägen

    wordName = input('Ange ett eller flera sökord med mellanslag mellan varje ord: ')  # Användaren anger sökordet

    wordlist = wordName.split()

    searchfolderandfiles(searchpath, wordlist)  # funktionen för att leta efter sökordet i sökvägen körs

    print('Resultat är sparat i resultat.txt!')


def searchfolderandfiles(path, word):  # Funktion som söker igenom mappar och filer
    for filename in os.listdir(path):  # for loop som går igenom allt i sökvägen
        fullPath = os.path.join(path, filename)  # Sätter ihop sökvägen och filen
        if os.path.isfile(fullPath):  # Ifall det är en specific fil körs olika funktioner:
            if fullPath.endswith('.txt'):  # Med txt-filer körs readtextfile funktionen
                readtextfile(fullPath, word)

            elif fullPath.endswith('.csv'):  # Med csv-filer körs readcsvfile funktionen
                readcsvfile(fullPath, word)

            elif fullPath.endswith('.docx'):  # Med plist-filer körs readplistfile funktionen
                readdocxfile(fullPath, word)
        if os.path.isdir(fullPath):  # Om det är en mapp körs funktionen om igen, men i den nya mappen
            searchfolderandfiles(fullPath, word)


def readtextfile(txtpath, word):
    textfile = open(txtpath, 'r')  # Öppnar txt filen
    for searchword in word:
        for textoffile in textfile:  # for loop som kollar texten i filen
            if searchword in textoffile:  # Om sökordet finns i texten sparas sökvägen och sökordet i resultat.txt
                resultat = open('resultat.txt', 'a')
                resultat.write('Sökväg: ' + txtpath + '\n' + 'sökord: ' + searchword + '\n' + '\n')
                resultat.close()
                print(
                    'Sökväg: ' + txtpath + '\n' + 'sökord: ' + searchword + '\n' + '\n')  # Skriver ut resultat till användaren


def readcsvfile(csvpath, word):
    textfile = open(csvpath, 'r')  # Öppnar csv filen
    for searchword in word:
        for textoffile in textfile:  # for loop som kollar texten i filen
            if searchword in textoffile:  # Om sökordet finns i texten sparas sökvägen och sökordet i resultat.txt
                resultat = open('resultat.txt', 'a')
                resultat.write('Sökväg: ' + csvpath + '\n' + 'sökord: ' + searchword + '\n' + '\n')
                resultat.close()
                print(
                    'Sökväg: ' + csvpath + '\n' + 'sökord: ' + searchword + '\n' + '\n')  # Skriver ut resultat till användaren


def readdocxfile(docxpath, word):
    textfile = getdocxtext(docxpath)  # Kallar på funktionen som omvandlar docx-filen till text
    for searchword in word:
        for textoffile in textfile:  # for loop som kollar texten i filen
            if searchword in textoffile:  # Om sökordet finns i texten sparas sökvägen och sökordet i resultat.txt
                resultat = open('resultat.txt', 'a')
                resultat.write('Sökväg: ' + docxpath + '\n' + 'sökord: ' + searchword + '\n' + '\n')
                resultat.close()
                print(
                    'Sökväg: ' + docxpath + '\n' + 'sökord: ' + searchword + '\n' + '\n')  # Skriver ut resultat till användaren


def getdocxtext(docxpath):  # Funktion som omvandlar docx-filen till en lista
    doc = docx.Document(docxpath)  # Öppnar docx-filen
    fullText = []
    for para in doc.paragraphs:  # for loop som plockar ut ord ur filens paragrafer in till den tomma listan
        fullText.append(para.text)
    return fullText  # returnerar listan


main()
