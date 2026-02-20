"""Generate funny names by randomly combining names from three separate lists."""

import random

print("\n--------------------------------------------")
print('Welcome to the Psych "Sidekick Name Picker".')
print("A name just like Sean would pick for Gus:")
print("--------------------------------------------\n\n")

first = ("Ben", "Bill", "Bob", "Bud", "Chuck", "Chas", "Charlie", "Chad",
         "Charly", "Dennis", "Elphonso", "Jack", "Jim", "Daniel", "Joe",
         "Johnny", "Ben", "Sam", "Sid", "Steve", "Winston")

middle = ("Beenie-Weenie", "Stinkbug", "Bowel Noises", "Boxelder",
          "Butterbean", "Big Burps", "Buttermilk", "Buttocks",
          "Chesterfield", "Chewy", "Chigger", "Cinnabuns", "Cleet", "Cornbread",
          "Crab Meat", "Crapps", "Dark Skies", "Clawhammer", "Dicman",
          "Fancypants", "Figgs", "Foncy", "Gootsy", "Greasy", "Huckleberry",
          "Huggy", "Ignatious", "Jimbo", "Pottin' Soil", "Lemongrass",
          "Lil Debil", "Longbranch", "Lunch Money", "Pealike", "Mergatroid",
          "Peabody", "Oil-Can", "Oinks", "Old Scratch", "Ovaltine",
          "Pennywhistle", "Pitchfork", "Potato Bug", "Pushmeet", "Rock Candy",
          "Schlomo", "Scratchensniff", "Scut", "The Squirts", "Skidmark",
          "Slaps", "Snakes", "Snoobs", "Snorki", "Soupcan", "Spitzitout",
          "Squids", "Stinky", "Storyboard", "Sweet Tea", "Baby Oil",
          "Bad News", "TeeTee", "Wheezy", "Worms", "Jazz Hands")

last = ("Appleyard", "Bigmeat", "Bloominshine", "Boogerbottom",
        "Breedslovetrout", "Butterbaugh", "Clovenhoof", "Clutterbuck",
        "Cocktoasten", "Endicott", "Fewhairs", "Gooberdapple", "Goodensmith",
        "Goodpasture", "Guster", "Henderson", "Hooperbag", "Hoosenater",
        "Hootkins", "Jefferson", "Jenkins", "Jingley-Schmidt", "Johnson",
        "Kingfish", "Listenbee", "M'Bembo", "McFadden", "Moonshine", "Nettles",
        "Noseworthy", "Olivetti", "Outerbridge", "Overpeck", "Overturf",
        "Oxhandler", "Peterson", "Pieplow", "Pinkerton", "Porkins", "Putney",
        "Quakenbush", "Rainwater", "Rosenthal", "Rubbins", "Sackrider",
        "Snuggleshine", "Splern", "Stevens", "Stroganoff", "Sugar-Gold",
        "Swackhamer", "Tippins", "Turnipseed", "Vinaigrette", "Walkingstick",
        "Wallbanger", "Weewax", "Weiners", "Whipkey", "Wigglesworth",
        "Wimplesnatch", "Winterkorn", "Woolysocks")

while True:
    first_name = random.choice(first)
    middle_name = random.choice(middle)
    last_name = random.choice(last)

    print("\n\n")
    print(f">>>>> \033[91m{first_name} '{middle_name}' {last_name}\033[0m <<<<<")
    print("\n\n")

    try_again = input("\n\nTry again? ")
    if try_again.lower() == "n":
        break

print("\n--------------------------------------------")
input("Alright, mush! Press ENTER to quit the fun.")
print("--------------------------------------------\n")
