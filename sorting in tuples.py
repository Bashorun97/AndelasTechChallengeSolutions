text = 'the university of lagos is loacated in Akoka lagos-mainland lga'
words = text.split() #split text into words
t = list() # create empty list
for word in words:
    t.append((len(word), word))#append length of the word and the word to the list

t.sort(reverse = True) #reverse the list from biggest to smallest

#create an empty list and append the value of the key in
# the t list into the res from biggest to smallest
res = list()
for length, word in t:
    res.append(word)
print(res)

    

    
