from file import list

def main():
    colors = ["red", "green", "blue"]
    total = 0
    for game in range(len(list)):
        #use a list to store MAXIMUM POSSIBLE number
        score = [0, 0, 0]
        current = list[game]
        for step in range(len(current)):
            #finds highest possible single digit number 
            if current[step:step+1].isdigit() == True and current[step+1:step+2].isdigit() == False:
                for i in range(len(colors)):
                    if current[step+2:step+2+len(colors[i])] == colors[i] and int(current[step:step+1]) > score[i]:
                        score[i] = int(current[step:step+1])
            #finds highest possible two digit number
            if current[step:step+2].isdigit() == True:
                for j in range(len(colors)):
                    if current[step+3:step+3+len(colors[j])] == colors[j] and int(current[step:step+2]) > score[j]:
                        score[j] = int(current[step:step+2])
        print(score)
        total = total + score[0]*score[1]*score[2]
        print(total)
main()

                                  
