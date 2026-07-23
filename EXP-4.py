# Finite State Machine for English Noun Plural Generation

def plural_fsm(word):
    # Words ending with s, x, z, ch, sh -> add "es"
    if word.endswith(("s", "x", "z", "ch", "sh")):
        return word + "es"

    # Words ending with consonant + y -> replace y with ies
    elif word.endswith("y") and len(word) > 1 and word[-2].lower() not in "aeiou":
        return word[:-1] + "ies"

    # Default rule -> add s
    else:
        return word + "s"


# User Input
noun = input("Enter a singular noun: ")

# Generate plural
plural = plural_fsm(noun)

# Display Result
print("Singular :", noun)
print("Plural   :", plural)
