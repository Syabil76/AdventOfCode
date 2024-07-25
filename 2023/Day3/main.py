with open("test.txt") as file:
    data = file.read()
    text = data.strip().split("\n")

def main():
    total = 0
    for line in range(len(text)):
        haspart = False
        current = text[line]
        j = 0
        while j < len(current):
            count = 0
            if current[j:j+1].isdigit() == True:
                while True:
                    if current[j:j+1+count].isdigit() == True:
                        count = count+1
                    else:
                        num = current[j:j+count]
                        while True:
                            if int(line) > 0 and int(line) < len(text)-2:
                                if j > 0 and j < len(current):
                                    for i in range(3):
                                        a = j
                                        while haspart == False:
                                            if not current[a:a+1].isdigit() and current[a:a+1] != '.':
                                                haspart = True
                                            a = a + 1
                                            if a == 3:
                                                break
                                        print(text[line-1+i][j-1:j+count+1])
                                    break
                            else:
                                break
                        break
                    j = j+count
            j = j + 1
    print("total =",total)

            
main()
