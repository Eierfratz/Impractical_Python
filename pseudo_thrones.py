"""The Silly Name Generator 'pseudonyms.py' with Game of Thrones names."""

import random

print("\n--------------------------------------------")
print("Welcome to the \"Game of Thrones\" name picker\".")
print("A name just like Tyrion would pick for Jaime:")
print("--------------------------------------------\n\n")

first = ("Abelar", "Abelon", "Addam", "Arnolf", "Argella", "Argilac", "Argos",
         "Argoth", "Armistead", "Arneld", "Arson", "Arthur", "Artos", "Arya",
         "Asha", "Aubrey", "Axel", "Ayrmidon", "Azor", "Azzak",
         "Bael", "Baela", "Baelon", "Baelor", "Balder", "Baldric", "Baldrick",
         "Ballabar", "Balerion", "Balman", "Bandy", "Bambarro", "Barba", 
         "Barbrey", "Barneby", "Barbara", "Barquen", "Barris", "Barristan",
         "Bartimus", "Barthogan", "Barth", "Bathi", "Bayard", "Bean", "Beans",
         "Beastmaster", "Becca", "Beck", "Bedwyck", "Belandra", "Belaquo",
         "Beldecar", "Beldon", "Belicho", "Belis", "Bella", "Bellegere", 
         "Bello", "Belwas", "Ben", "Belthasar", "Bendamure", "Benedar",
         "Benedict", "Benerro", "Benethon", "Benfred", "Benfrey", "Benifer",
         "Benjamin", "Benjen", "Benjicot")

middle = ("The Thumb", "Protégé", "Clip-On", "Liability", "Giggles",
          "Torchlight", "Snack-Run", "Bail-Bond", "Map-Folder",
          "Ladder-Holder", "The Spare", "Meat-Shield", "Placeholder",
          "Collateral", "Also-Ran", "Just", "Danger-Is-My", "Understudy",
          "Technicality", "Wait-For-It", "The Decoy")

last = ('Ambrose', 'Ambrose', 'Arryn', 'Ashford', 'Baelish', 'Beesbury',
        'Blackfyre', 'Blackwood', 'Blackwood', 'Bracken', 'Broome', 'Bullock',
        'Bulwer', 'Butterwell', 'Caswell', 'Celtigar', 'Cobb', 'Cockshaw', 
        'Connington', 'Costayne', 'Crakehall', 'Dayne', 'Deem', 'Durrandon', 
        'Duskendale', 'Estermont', 'Estermont', 'Eysen', 'Farman', 'Florent', 
        'Frey', 'Graceford', 'Greyjoy', 'Greyjoy', 'Harlaw', 'Harroway', 
        'Hightower', 'Hill', 'Hotah', 'Humble', 'Jast', 'Karstark', 
        'Lannister', 'Lefford', 'Lorch', 'Marbrand', 'Martell', 'Massey', 
        'Mormont', 'Norcross', 'Oakheart', 'Orkwood', 'Osgrey', 'Peake', 
        'Penrose', 'Qhaedar', 'Redfort', 'Reyne', 'Rivers', 'Rosewood', 
        'Royce', 'Runnymud', 'Seaworth', 'Sharp', 'Stackspear', 'Staedmon', 
        'Stark', 'Steelsong', 'Stokeworth', 'Tarbeck', 'Tarbeck', 'Targaryen', 
        'Tarly', 'Terrick', 'Thorne', 'Torrent', 'Tully', 'Turnberry',
        'Tyrell', 'Tyrosh', 'Vance', 'Velarion', 'Velaryon', 'Waynwood', 
        'Weatherwax', 'Whitehead', 'Wynch', 'Yronwood')

while True:
    first_name = random.choice(first)
    middle_name = random.choice(middle)
    last_name  = random.choice(last)

    print("\n\n")
    print(f">>> \033[91m{first_name} '{middle_name}' {last_name}\033[0m <<<")
    print("\n\n")

    try_again = input("\n\nTry again? ")
    if try_again.lower() == "n":
        break

print("\n--------------------------------------------")
input("Alright, mush! Press ENTER to quit the fun.")
print("--------------------------------------------\n")
