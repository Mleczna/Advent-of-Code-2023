passwords = open("AoC-day1.txt", "r")

tab = []
sum = 0
linia = ""

for x in passwords:

    for i in x:
        if i.isdigit():
            tab.append(i)
    

    if(len(tab) > 1):
        firstDigit = tab[0]
        firstDigit = str(firstDigit)
        lastDigit = tab[len(tab)-1]
        lastDigit = str(lastDigit)

        result = firstDigit + lastDigit
        result = int(result)

        sum = sum + result

        print("First digit: " + str(firstDigit) + " Last digit: " + str(lastDigit) + " Result: " + str(result) + " Sum: " + str(sum))
    elif(len(tab) == 1):
        firstDigit = tab[0]
        firstDigit = str(firstDigit)
        result = firstDigit + firstDigit
        result = int(result)

        sum = sum + result
        
        print("First digit: " + str(firstDigit) + " Last digit: " + str(firstDigit) + " Result: " + str(result) + " Sum: " + str(sum))

    tab = []

print("Sum:", sum)

passwords.close()