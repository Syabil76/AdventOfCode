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

def worditerate():
    for item in range(0,5):
        position = 1000
        position2 = 1000
        final1 = 0
        final2 = 0
        for x, y in valid.items():
            count = 0
            count2 = 0
            while True:
                string = lister[item]
                if string[count:count+len(x)] == x:
                    break
                elif count+len(x) > len(string):
                    break
                count = count + 1
            if count < position and count+len(x)<len(string):
                position = count
                final1 = y
            while True:
                string = lister[item]
                if string[len(string)-len(x)-count2:len(string)-count2] == x:
                    break
                elif count2+len(x) > len(string):
                    break
                count2 = count2 + 1
            if count2 < position2 and count2+len(x)<len(string):
                position2 = count2
                final2 = y
        print(final1*10+final2)
