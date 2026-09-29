import getpass 

users = [
    ["melisa", "1234"],
    ["lucky", "abcd" ]
]

books = [
    ["Harry Potter", True],              #True=verfügbar False=ausgeliehen
    ["Der Hobbit", True],
    ["Python lernen", False]
]


# Start
programm_laeuft = True
while programm_laeuft:
    print("Willkommen in der Bibliothek")
    print("1. Login\n2. Beenden")
    Auswahl = input("> ")
    eingeloggter_user = None
    login = False
    if Auswahl == "2":
        programm_laeuft = False
        break

# 1. Login 
    while not login:
        benutzer = input("Benutzername: ")
        benutzer_passwort = getpass.getpass("Password: ")

        for user in users:   
            if user[0] == benutzer and user[1] == benutzer_passwort:
                print("Login erfolgreich")
                eingeloggter_user = user
                login = True
                break
        else:
            print("Benutzer oder Passwort falsch")

#2. Menü
    while login:
        print("Hallo", eingeloggter_user[0],"\n1. Bücher anzeigen\n2. Buch ausleihen\n3. Buch zurückgeben\n4. Passwort ändern\n5. Logout")
        Auswahl = input("> ")
    
        if Auswahl == "1":
            for book in books:
                if book[1] == True:
                    print(book[0], "- vorhanden")
                else:
                    print(book[0], "- ausgeliehen")
            
        elif Auswahl == "2":
            buch = input("Welches Buch möchtest du ausleihen?: ")
            buch_gefunden = False

            for book in books:
                if buch.lower() == book[0].lower():
                    buch_gefunden = True

                    if book[1] == True:
                        book[1] = False
                        print("Buch erfolgreich ausgeliehen")
                    else:
                        print("Bereits ausgeliehen")

            if not buch_gefunden:
                print("Buch nicht gefunden.")

                
        elif Auswahl == "3":
            buch = input("Welches Buch möchtst du zurückgeben?: ")
            buch_gefunden = False
            for book in books:
                if buch.lower() == book[0].lower():
                    buch_gefunden = True

                    if book[1] == False:
                        book[1] = True
                        print("Erfolgreich zurückgegeben")
                    else:
                        print("Das Buch ist bereits verfügbar")

            if not buch_gefunden:
                print("Buch nicht gefunden.")


        elif Auswahl == "4":
            neues_passwort = None

            while not neues_passwort:
                neues_passwort = getpass.getpass("Gib dein neues Password ein: ")

            eingeloggter_user[1] = neues_passwort
            print("Passwort erfolgreich geändert!")

        elif Auswahl == "5":
            login = False
            print("Erfolgreich ausgeloggt. Bis zum nächsten Mal!")

        else:
            print("Ungültige Auswahl.")
            

    