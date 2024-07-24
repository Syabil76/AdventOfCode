from file import lister

def iterate():
    total = 0
  #iterates through entire list
    for i in range(1000):
        newstring = ''
        j = 0
        k = 0
        l = 0
      #loops through left side and breaks when a nunmber is found
        while True:
            string = lister[i]
            if (string[j:j+1]).isdigit() == True:
                newstring = newstring + string[j:j+1]
                break
            j = j + 1
          #loops through right side and breaks when a number is found
        while True:
            string = lister[i]
            if (string[len(string)-l:len(string)-l+1]).isdigit() == True:
                newstring = newstring + string[len(string)-l:len(string)-l+1]
                break
            l = l + 1
          #adds total
        total = total + int(newstring)
    print(total)

iterate()
