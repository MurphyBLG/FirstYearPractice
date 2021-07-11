import sys


def syntactic_check(lexemes):
    state = "start"
    acceptable = False

    for lexeme in lexemes:
        if state == "start":
            if lexeme[1] == "variable name":
                state = "r_as_op"
            else:
                return "REJECT"

        elif state == "r_as_op":
            if lexeme[1] == "assignment operator":
                state = "r_arr_name"
            else:
                return "REJECT"

        elif state == "r_arr_name":
            if lexeme[1] == "array name":
                state = "r_int_const_chain"
            else:
                return "REJECT"

        elif state == "r_int_const_chain":
            if lexeme[1] == "integer constant chain":
                state = "r_ar_op"
            else:
                return "REJECT"

        elif state == "r_ar_op":
            if lexeme[1] == "arithmetic operation":
                state = "r_f_name"
            else:
                return "REJECT"

        elif state == "r_f_name":
            if lexeme[1] == "function name":
                state = "r_id_chain"
            else:
                return "REJECT"

        elif state == "r_id_chain":
            if lexeme[1] == "identifier chain":
                state = "r_semicolon"
            else:
                return "REJECT"

        elif state == "r_semicolon":
            if lexeme[1] == "semicolon":
                state = "finish"
                acceptable = True
            else:
                return "REJECT"

        else:
            return "REJECT"

    if acceptable:
        return "ACCEPT"
    else:
        return "REJECT"
