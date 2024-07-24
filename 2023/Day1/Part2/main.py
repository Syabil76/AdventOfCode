from file import lister

valid = {
    "one" : 1,
    "two" : 2,
    "three" : 3,
    "four" : 4,
    "five" : 5,
    "six" : 6,
    "seven" : 7,
    "eight" : 8,
    "nine" : 9,
}

def main():
    val1 = 0
    val2 = 0
    total = 0
    for i in range(len(lister)):
        flag1 = False
        flag2 = False
        string = lister[i]
        for j in range(len(string)):
            if string[j:j+1].isdigit() == True:
                val1 = int(string[j:j+1])
                break
            else:
                for x, y in valid.items():
                    if string[j:j+len(x)] == x:
                        val1 = y
                        flag1 = True
                        break
            if flag1 == True:
                break
        for k in range(len(string)):
            if string[len(string)-k:len(string)-k+1].isdigit() == True:
                val2 = int(string[len(string)-k:len(string)-k+1])
                break
            else:
                for a, b in valid.items():
                    if string[len(string)-len(a)-k:len(string)-k] == a:
                        val2 = b
                        flag2 = True
                        break
            if flag2 == True:
                break          
        total = total + val1*10 + val2
        print(total)

main()
