import sys


def syntactic_check(lexemes):
    state = "start"

    for lexeme in lexemes:
        if lexeme[1] == "space":
            continue

        elif state == "start":
            if lexeme[1] == "identifier":
                state = "identifier1"
            else:
                sys.exit("REJECT")

        elif state == "identifier1":
            if lexeme[1] == "assignment operator":
                state = "assignment operator"
            else:
                sys.exit("REJECT")

        elif state == "assignment operator":
            if lexeme[1] == "identifier":
                state = "identifier2"
            else:
                sys.exit("REJECT")

        elif state == "identifier2":
            if lexeme[1] == "opening square bracket":
                state = "opening square bracket"
            else:
                sys.exit("REJECT")

        elif state == "opening square bracket":
            if lexeme[1] == "integer constant":
                state = "integer constant list"
            else:
                sys.exit("REJECT")

        elif state == "integer constant list":
            if lexeme[1] == "comma":
                state = "comma"
            elif lexeme[1] == "closing square bracket":
                state = "closing square bracket"
            else:
                sys.exit("REJECT")

