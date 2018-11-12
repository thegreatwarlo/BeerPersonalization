import gzip
    
file_in = gzip.open('Beeradvocate.txt.gz', 'r')
file_out = open("beeradvocate.csv", "w")
file_out.write("beer/name^ beer/beerId^ beer/brewer^ beer/ABV^ beer/style^ review/appearance^ review/aroma^ review/palate^ review/taste^ review/overall^ review/time^ review/profileName^ review/text\n")

for i in file_in:
    line = ""
    while i != '\n':
        i = i.decode('utf-8', errors = 'ignore')
        line = line + i.split(":", 1)[1].rstrip()
        if(not("review/text" in i)):
            line = line +  "^" 
        i = file_in.next()
    #print line
    file_out.write(line.encode('utf-8') + "\n")

file_in.close()

# Please Take out line numbers 4, 6, 15 and 16 to run for the entire dataset
