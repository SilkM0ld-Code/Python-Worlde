import random
print("[===========================]")
print("'G' means it is there,")
print("'Y' means it is in the word but not there,")
print("'B' means it is not in the word.")
print("[===========================]")
while True:
    wordle=[]
    word=[]
    result=[]
    alpha=["a","b","c","d","e","f","g","h","i","j","k","l","m","n","o","p","q","r","s","t","u","v","w","x","y","z"]
    attempt=0
    attempt_tot=0
    def end():
        print("Attempst:",attempt)
        attempt_tot=+attempt
        print("Total Attempts:",attempt_tot)

    with open('Words.txt', 'r') as file:
        a = [line.strip() for line in file]

    target =random.choice(a)
    for char in target:
        wordle.append(char)
    def worlde_game():
        global attempt
        print("[===========================]")
        print("".join(alpha))
        print("[===========================]")
        word.clear()
        inputedx=input("")
        print("[------------------------------------------------]")
        inputed=inputedx.lower()
        for char in inputed:
            word.append(char)
        with open('Words.txt', 'r') as file:
            content = file.read()
            if inputed not in a:
                worlde_game()
            elif len(word) == 5:
                print("".join(word).upper())
                for i in range(len(word)):
                    if word[i] == wordle[i]:
                        result.append("G")
                    elif word[i] in wordle:
                        result.append("Y")
                    else:
                        result.append("B")
                        if word[i] in alpha:
                            alpha.remove(word[i]) 
                print("".join(result))
                print("[===========================]")
                result.clear()
                attempt+=1

                if inputed==target:
                    end()
                else:

                    worlde_game()
    worlde_game()
