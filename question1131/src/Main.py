
word = input()

# DO_NOT_EDIT_ANYTHING_ABOVE_THIS_LINE
with open('dataset.txt','r') as f:
     lines=[]
     for line in f:
         lines.append(line.strip())
toplam = 0
for i in lines:
    if word in i:
        for j in i.split():
            try:
                toplam = toplam + int(j)

            except:
                pass
print(toplam)



# DO_NOT_EDIT_ANYTHING_BELOW_THIS_LINE

