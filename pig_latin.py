"""
To form Pig Latin, you take an English word that begins with a consonant, 
move that consonant to the end, and then add “ay” to the end of the word. If 
the word begins with a vowel, you simply add “way” to the end of the word.
"""

print("\n\n\nWelcome to the English > Pig Latin translator.")
print("----------------------------------------------")
word = input("\nYour input: ")

while True:
    if word[0].lower() in "aeiouäöü":
        result = word.lower() + "way"
    else:
        result = word[1:len(word)] + word[0].lower() + "ay"
    print(f"Pig Latin:  {result}\n")
    print("----------------------------------------------")
    
    try_again = input("\nAnother one? ")
    if try_again.lower() == "n":
        break
    
    word = input("\nYour input: ")

print(f"\nGood bye, {result.title()}!\n")