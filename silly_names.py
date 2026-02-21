"""My very own Silly Name Generator for German language names."""

import random
from colorama import init, Fore

init(autoreset=True)

print(f"\n\n{Fore.LIGHTGREEN_EX}--------------------------------------------")
print(f"{Fore.LIGHTGREEN_EX}Herzlich Willkommen zu Kabille Ebirbertmanns ")
print(f"{Fore.LIGHTGREEN_EX}           \"Lustige Namen\".")
print(f"{Fore.LIGHTGREEN_EX}--------------------------------------------\n")

first = ("Jörgito", "Kalle", "Nikolaus", "Hannes", "Hinnerk", "Heini",
         "Krischi", "Deeze", "Detlef", "Sarah", "Pitter", "Jupp", "Mehmet",
         "Dingo", "Sabine", "Gotthilf", "Ephraim", "Alberto", "Roberto", 
         "Akki", "Atti", "Marianne", "Naima", "Yolanda", "Ernesto", "Karl",
         "Carletto", "Daniel", "Maritsa", "Steffen", "Achmed", "Ilona",
         "Maurizio", "Jakobus", "Thaddeus", "Wolfgang", "Amadeus", "Ingwer",
         "Engbert", "Ewald", "Fernando", "Arnulf", "Dorothea", "Annette",
         "Berta", "Bertold", "Burda", "Roswita", "Drehbert", "Herbert")

last =  ("Geils-Lindemann", "Schedensack", "Käseberg", "Gellenbert", "Fickfotz",
         "Schönblau", "Stöhnsau", "Zumthor", "Özdemir", "Özil", "Tamtam",
         "Petrisack", "Hosentod", "Rabimmelt", "Rammelt", "Drehbert",
         "Brotkorb", "Furzbirne", "Bremsbirne", "Türknauf", "Teppichwech",
         "Klingbeil", "Quälgeist", "Wendehals", "Planlos", "Schießmichtot",
         "Schwerenot", "Turbobraun", "Miefsack", "Bergmann", "Vollpfosten",
         "Klapptor", "Dennebier", "Knappsack", "Logimann", "Dummbatz",
         "Tummpattel", "Geizknüppel", "Fischkopp", "Klingelsack", "Hartung",
         "Hauknecht", "Eulenberg", "Summser", "Stroganoff", "Steckrinski",
         "Brillenraub", "Lücke", "Risse", "Rüssel", "Hundeangst", "Luftikuss",
         "Flausen-im-Kopf", "Flusensack", "Ölschläger", "Schwimmbutz",
         "Lotzfeck", "Tanzgoll", "Ganztroll", "Schwurbelstar")

spruch_1 = f"\n{Fore.BLUE}Und hier die weitere Auswahl...\n"
spruch_2 = f"\n{Fore.GREEN}Und noch einmal fünf Schenkelklopfer:\n"
spruch_3 = f"\n{Fore.YELLOW}Halt dich fest, jetzt wird's lustelig!\n"
spruch_total = [spruch_1, spruch_2, spruch_3]

print(f"{Fore.CYAN}Hier sind unsere ersten fünf Auserwählten!\n")
while True:
    for name in range(0, 5):
        first_name = random.choice(first)
        last_name  = random.choice(last)
        print(f"\t{Fore.RED}- {first_name} {last_name}\033[0m")
    print("\nNee, wat häbbt wi lacht!")

    try_again = input("\nNoch ein paar Namen? ")
    if try_again.lower() == "n":
        break
    print(random.choice(spruch_total))

print("\n--------------------------------------------")
input("Genug gelacht? Drücke <EINGABE> zum Beenden.")
