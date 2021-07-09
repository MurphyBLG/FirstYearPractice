from transliterator import transliterate
from lexic import convert_to_lexemes
from syntax import syntactic_check

def main():
    s = input()
    temp = transliterate(s)
    lexemes = convert_to_lexemes(temp)

    syntactic_check(lexemes)


if __name__ == '__main__':
    main()
