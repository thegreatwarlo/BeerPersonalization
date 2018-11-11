file = open("D:/Columbia/Fall 2018/PTA/Project/beeradvocate.txt")
file2 = open("D:/Columbia/Fall 2018/PTA/Project/beeradvocate1.csv", "w")
file2.write("beer/name^ beer/beerId^ beer/brewer^ beer/ABV^ beer/style^ review/appearance^ review/aroma^ review/palate^ review/taste^ review/overall^ review/time^ review/profileName^ review/text\n")
count = 0
for i in file:
    count = count + 1 
    line = ""
    while i != '\n':
        line = line + i.split(":", 1)[1].rstrip()
        if(not("review/text" in i)):
            line = line +  "^" 
        i = file.next()
    print line
    file2.write(line + "\n")
    if count > 100:
        break
file.close()

# Please Take out line numbers 4, 6, 15 and 16 to run for the entire dataset
