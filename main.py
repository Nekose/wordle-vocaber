from src.word import Word
import enchant
import itertools
wordle = Word()
wordle.grey = input("Input grey letters, or press enter to skip")

def score(word):
    letterFrequency = {'E': 12.0,
                        'T': 9.10,
                        'A': 8.12,
                        'O': 7.68,
                        'I': 7.31,
                        'N': 6.95,
                        'S': 6.28,
                        'R': 6.02,
                        'H': 5.92,
                        'D': 4.32,
                        'L': 3.98,
                        'U': 2.88,
                        'C': 2.71,
                        'M': 2.61,
                        'F': 2.30,
                        'Y': 2.11,
                        'W': 2.09,
                        'G': 2.03,
                        'P': 1.82,
                        'B': 1.49,
                        'V': 1.11,
                        'K': 0.69,
                        'X': 0.17,
                        'Q': 0.11,
                        'J': 0.10,
                        'Z': 0.07}
    score = 0
    for letter in word:
        score += letterFrequency[letter.upper()]
    return score

for object in wordle.letterlist:
    green = input(f"For position {object.position}, Input green letter, or press enter to skip: ")
    if green != "":
        object.letterlist = [green]
        print(object.letterlist)
        continue
    yellows = input(f"For position {object.position}, Input yellow letters, or press enter to skip: ")
    [object.letterlist.remove(x) for x in yellows]
    [object.letterlist.remove(x) for x in wordle.grey]
    wordle.required += yellows
    print(object.letterlist)
dictionary = enchant.Dict("en_US")
generator = itertools.product(wordle.l1.letterlist,wordle.l2.letterlist,wordle.l3.letterlist,wordle.l4.letterlist,wordle.l5.letterlist)
print("working....")
returnlist = []
for element in generator:
    if dictionary.check("".join(element)):
        if all(x in element for x in wordle.required):
            print(f"{''.join(element)}, {score(''.join(element))}")


print("Done")