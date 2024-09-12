m = 0
res = 0
allowed = "ab"
words = ["abbadabab"]
words_len = len(words)

for i in range(words_len):  # Loop over words
    word = words[i]  # Get the current word
    for j in range(len(words)):
        if word[m:len(allowed)+m] == allowed:
            print("yes")

        m += 1
