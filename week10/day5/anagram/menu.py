import anagram_checker


def validate_word(word):
    if "".isalpha() and len(word.split()) == 1:
        return word.strip()
    else:
        return None


def manu():
    while True:
        choice = input("Welcome to the anagram checker,\n A. enter word to get anagrams.\n X. Exit")
        if choice in "Xx":
            print("Bye Bye")
            exit()
        elif choice in "Aa":
            user_word = input("type a word to search: ")
            validated_word = validated_word(user_word)
            if validated_word:
                print(validated_word)
                if anagram_checker.ac.is_valid_word(validated_word):
                    anagrams = anagram_checker.ac.get_anagrams(validated_word)
                    print(f"your word : {validated_word} is a valid English word.\n Anagrams for your word: "
                          f"{' '.join(anagrams)}\n\n")
                else:
                    print('word not in dictionary\n\n')
            else:
                print('Invalid input detected\n\n')

        else:
            print('invalid input\n\n')


manu()
