# Finite State Automaton (FSA) to recognize strings ending with "ab"

def finite_state_automaton(string):
    # Initial state
    state = "q0"

    print("\nState Transitions:")
    print("------------------")

    for ch in string:
        if state == "q0":
            if ch == 'a':
                state = "q1"
            else:
                state = "q0"

        elif state == "q1":
            if ch == 'a':
                state = "q1"
            elif ch == 'b':
                state = "q2"
            else:
                state = "q0"

        elif state == "q2":
            if ch == 'a':
                state = "q1"
            elif ch == 'b':
                state = "q0"
            else:
                state = "q0"

        print(f"Read '{ch}' --> Current State: {state}")

    print("\nFinal State:", state)

    if state == "q2":
        print("Result: Accepted (String ends with 'ab')")
    else:
        print("Result: Rejected (String does not end with 'ab')")


# Main Program
text = input("Enter a string containing only 'a' and 'b': ")
finite_state_automaton(text)
