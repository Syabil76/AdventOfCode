from file import list

no = []

def main():
    parameters = {
        "red" : 12,
        "green" : 13,
        "blue": 14,
    }
    total =5050
    #sets total to maximum amount and subtracts it when itf finds a number
    for game in range(len(list)):
        flag = False
        current = list[game]
        for step in range(len(current)):
            #checks if its a two digit number as maximum values can ONLY be 2 digits
            if current[step:step+1].isdigit() == True:
                if current[step+1:step+2].isdigit() == True:
                    if int(current[step:step+2]) > parameters["red"]:
                        #checks if its above the lowest possible parameter
                        for x, y in parameters.items():
                            #finds the color and checks if it fits the parameter and sets of a flag that ends the loop
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
