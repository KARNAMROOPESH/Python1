sentence = input("Please Enter a sentence")
print (sentence)
characternum = 0
wordcount = 1
for i in sentence: 
    characternum = characternum+1
    if(i == ' '):
        wordcount = wordcount+1
print ("number of characters")
print (characternum)
print (wordcount)