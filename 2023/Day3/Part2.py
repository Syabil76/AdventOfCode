with open("test.txt") as file:
    data = file.read()
    text = data.strip().split("\n")

def main():
    for line in range(2):
        i = 0
        cl = text[line]
        while i < len(cl):
            if cl[i:i+1].isdigit() == False and cl[i:i+1] != ".":
                lookaround(cl, i, line)
            i = i+1

def lookaround(cl, i, line):
    x = i-1
    y = i+2
    z = line-1
    w = line+2
    if i < 1:
        x = i
    if i > len(cl) - 2:
        y = i
    if line < 1:
        z = line
    if line > len(text) - 2:
        w = line
    print(f"{cl[i:i+1]} | {x, y, z, w}")
    for j in range(z, w):
        for k in range(x, y):
            if text[j][k].isdigit() == True:
                cur = text[j]
                print(findfull(cur, k))
                temp = findfull(cur, k)


def findfull(cur, k):
    left = 0
    right = 0
    while True:
        if cur[k:k+1+right].isdigit() == True:
            right = right+1
        elif cur[k-1-left:k].isdigit() == True:
            left = left + 1
        else:
            return cur[k-left:k+right]


main()
