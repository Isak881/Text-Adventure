def start_adventure():
    print("Välkommen till det stora äventyret!")
    print("Du står framför tre mörka gångar.")
    print("Vilken gång väljer du?")
    print("1. Den vänstra gången")
    print("2. Den mittersta gången")
    print("3. Den högra gången")

    choice = input("Skriv 1, 2 eller 3 för att välja: ")

    if choice == "1":
        print("Du går in i den vänstra gången och hör ett mystiskt ljud...")
        # Lägg till mer logik här för gång 1
    elif choice == "2":
        print("Du går in i den mittersta gången och känner en kall vind...")
        # Lägg till mer logik här för gång 2
    elif choice == "3":
        print("Du går in i den högra gången och ser ett svagt ljus i fjärran...")
        # Lägg till mer logik här för gång 3
    else:
        print("Ogiltigt val, försök igen!")
        start_adventure()  # Starta om funktionen om valet är ogiltigt

# Starta spelet
if __name__ == "__main__":
    start_adventure()
    