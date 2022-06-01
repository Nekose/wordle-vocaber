from src.word import Word
import enchant
import itertools
wordle = Word()
wordle.grey = input("Input grey letters, or press enter to skip")

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
for element in generator:
    if dictionary.check("".join(element)):
        if all(x in element for x in wordle.required):
            print("".join(element))