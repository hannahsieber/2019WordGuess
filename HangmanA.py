
import random
import string

word = []

guessed = [" "]
letters = ["e","t","a","o","i","n","s","h","r","d","l","u"]
vowels = ["e","a","o","i","u","y"]
dict = []
len = 0
attempts = 0
found = False


## DO SOMETHING WITH FREQUENCY SO IT GUESSES A MORE LIKELY OPTION FIRST
# PRIORITIZE MOST COMMON WORDS IF I HAVE A SECOND LIST THAT I ONLY LOOK AT IF I RUN OUT

def what_next():
    global dict
    list = {"a":0,"b":0,"c":0,"d":0,"e":0,"f":0,"g":0,"h":0,"i":0,"j":0,"k":0,"l":0,"m":0,
            "n":0,"o":0,"p":0,"q":0,"r":0,"s":0,"t":0,"u":0,"v":0,"w":0,"x":0,"y":0,"z":0}
    for d in dict:
        for let in d:
            if let not in guessed:
                list[let] += 1
    key_max = 0
    current_key = "a"
    for item in list.keys():
        if list[item] > key_max:
            key_max = list[item]
            current_key = item
    return current_key


def is_in(x,where):
    global dict
    original_len = dict.__len__()
    for num in range(0, original_len):
        if x not in dict[original_len - num - 1]:
            dict.pop(original_len - num - 1)
            guessed.append(x)
        else:
            ## makes it so it IS where it should be but also not elsewhere
            for a in range(1,len+1):
                if str(a) in where: # SHOULD BE THERE
                    if x not in dict[original_len-num-1][a-1]:
                        dict.pop(original_len - num - 1)
                        break
                else: # SHOULDN'T BE THERE
                    if x in dict[original_len - num - 1][a-1]:
                        dict.pop(original_len - num - 1)
                        break
            guessed.append(x)


def not_in(x):
    global dict
    original_len = dict.__len__()
    for num in range(0, original_len):
        if x in dict[original_len - num - 1]:
            dict.pop(original_len - num - 1)
            guessed.append(x)
    print(dict.__len__())

def earlyGuess():
    spinning = 0
    guess = random.choice(letters)
    while guess in guessed:
        if spinning == 5:
            guess = what_next()
            while guess in guessed:
                guess = what_next()
            return guess
        else:
            guess = random.choice(letters)
            spinning += 1
    return guess

def spell(wo):
    print(".", end='', flush=True)
    for x in wo:
        print(x+".", end='', flush=True)

def checkPercent():
    have = 0
    for a in word:
        if a.__len__() == 1:
            have += 1
    return have/len

for line in open("words_alpha.txt"):
    dict.append(line.rstrip("\n"))
while len < 4 or len > 9:
    length = input("How many letters are in the word? It must be between 4 and 9\n")
    try:
        len = int(length)
    except ValueError:
        print("You needed to enter a number between 4 and 9.\n")
#print(dict.__len__())
original_len = dict.__len__()
for num in range(0,original_len):
    if dict[original_len-num-1].__len__() != len:
        dict.pop(original_len-num-1)

#print(dict.__len__())
print("Let's play!\n")

for a in range(0,len):
    word.append("."+str(a+1)+".")

while attempts < 18 and not found:
    if checkPercent() < .3:
        e = earlyGuess()
    else:
        e = what_next()

    print("My guess is " + e+"\n\n")

## MAKE SURE THEIR ANSWER IS INTS IN RIGHT RANGE

    print("So far I have...")
    spell(word)
    ans = input("\n\nEnter '0' if the letter is not in the word\nOtherwise,"
              " enter the numbers of spots where it is\n")

    if ans == "0":
        print("\nI guess not... I have guessed " + str(attempts + 1) + " time(s) so far!\n")
        not_in(e)
    else:
        print("\nNice... I have guessed " + str(attempts + 1) + " time(s) so far!\n")
        for ch in ans:
            word[int(ch)-1] = e
        is_in(e,ans)
    attempts += 1
    spell(word)
    print("\n")
    # print(fillIn(word))

    if checkPercent() == 1:
        found = True
        break





if not found:
    print("\n\nYou won... I'm sad now. Thanks a lot.")
else:
    print("\n\nSorry - I figured it out!")