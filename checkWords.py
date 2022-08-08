from uzwords import words

# print(len(words))
# print(words[0])
# print(words[-1])
# print(words[7777])
# print(words[13213])

from difflib import get_close_matches


def checkWord(word, words=words):
    word = word.lower()
    matches = set(get_close_matches(word, words))
    available = False

    if word in matches:
        available = True
        matches = word
    elif 'ҳ' in word:
        word = word.replace('ҳ', 'х')
        matches.update(get_close_matches(word, words))
    elif 'х' in word:
        word = word.replace('х', 'ҳ')
        matches.update(get_close_matches(word, words))
    elif 'h' in word:
        word = word.replace('h', 'x')
        matches.update(get_close_matches(word, words))
    elif 'x' in word:
        word = word.replace('x', 'h')
        matches.update(get_close_matches(word, words))

    return {'available': available, "matches": matches}




if __name__ == '__main__':
    print(checkWord('ҳато'))
    print(checkWord('тариҳ'))
    print(checkWord('хато'))
    print(checkWord('олма'))
    print(checkWord('ҳат'))
    print(checkWord('ҳайт'))
