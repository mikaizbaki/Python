sentence = input("Enter a sentence: ")

words = sentence.split()      
count = {}                    

for w in words:
    if w in count:
        count[w] += 1         
    else:
        count[w] = 1          

print(count)