# Step 1: Read text from file
with open("input.txt", "r") as f:
    text = f.read()

# Step 2: Turn text into words
words = text.lower().split()

# Step 3: Count words in a dictionary
count = {}
for w in words:
    count[w] = count.get(w, 0) + 1

# Step 4: Sort dictionary into list of tuples (word, count)
sorted_words = sorted(count.items())

# Step 5: Save result to file
with open("word_count.txt", "w") as f:
    f.write(str(sorted_words))

print("Done! Check word_count.txt")