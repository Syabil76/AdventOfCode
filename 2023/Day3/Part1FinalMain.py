with open("final.txt") as file:
    data = file.read()
    text = data.strip().split("\n")

def main():
    final = 0
    for r in range(len(text)):
        cl = text[r]
        i = 0
        while i < len(cl):
            if cl[i:i+1].isdigit() == True:
                a = checkdigit(i ,cl)[0]
                num = checkdigit(i ,cl)[1]
                final = final + lookaround(i, r, a, cl, num)
                
                i = i + a
            i = i + 1
    print("total:",final)

def checkdigit(i, cl):
    a = 0
    while True:
        print(cl[i:i+a+2])
        if cl[i:i+a+1].isdigit() == True and i+a+1 < len(cl)+1:
            a = a + 1
        else:
            num = int(cl[i:i+a])
            return a, num


def lookaround(i, r, a, cl, num):
    x = i-1
    y = i+1+a
    z = r-1
    w = r+1
    if i < 1:
        x = i
    if i+a+1 > len(cl) - 2:
        y = i+a
    if r < 1:
        z = r
    if r > len(text) - 2:
        w = r
    print(f"{num} | {x, y, z, w}")
    for j in range(z, w+1):
        for k in range(x, y):
            if text[j][k].isdigit() == False and text[j][k] != '.':
                return num
    return 0
main()

