def print_upper_words(strList):
    for str in strList:
        print(str.upper())


def print_upper_words2(strList):
    for str in strList:
        if str[0] == 'e' or str[0] == 'E':
            print(str.upper())


def print_upper_words3(strList, startLetters):
    for str in strList:
        for letter in startLetters:
            if str[0] == letter:
                print(str.upper())
                break
