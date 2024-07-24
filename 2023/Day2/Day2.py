from file import list

no = []

def main():
    parameters = {
        "red" : 12,
        "green" : 13,
        "blue": 14,
    }
    total =5050
    for game in range(len(list)):
        flag = False
        current = list[game]
        for step in range(len(current)):
            if current[step:step+1].isdigit() == True:
                if current[step+1:step+2].isdigit() == True:
                    if int(current[step:step+2]) > parameters["red"]:
                        for x, y in parameters.items():
                            if current[step+3:step+3+len(x)] == x:
                                if int(current[step:step+2]) > y:
                                    no.append(f'game {game+1}')
                                    total = total - game -1
                                    flag = True
                                    break
            if flag == True:
                break
    print(no)
    print(total)

    
main()
