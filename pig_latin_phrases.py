"""
To form Pig Latin, you take an English word that begins with a consonant, 
move that consonant to the end, and then add “ay” to the end of the word. If 
the word begins with a vowel, you simply add “way” to the end of the word.
"""

print("\n\n\nWelcome to the English > Pig Latin translator.")
print("-" * 30)


while True:
    phrase = input("\nYour input: ")
    words = phrase.split()
    pig_latin_phrase = []
    
    for word in words:
        if word[0].lower() in "aeiouäöü":
            result = word.lower() + "way"
        else:
            result = word[1:] + word[0].lower() + "ay"
        
        pig_latin_phrase.append(result)

    # Join the list back into a single string with spaces
    final_output = " ".join(pig_latin_phrase)
        
    print(f"Pig Latin:  {final_output.capitalize()}\n")
    print("-" * 30)
    
    try_again = input("\nAnother one? ")
    if try_again.lower() == "n":
        break

    print(f"\nGood bye, {result.title()}!\n")