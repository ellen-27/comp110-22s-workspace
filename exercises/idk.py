if contains_char == True:
            if secret[i] == guess[i]:
                emojis = emojis + "\U0001F7E9" #green
            else:
                emojis +=  "\U0001F7E8" #yellow
        if contains_char == False:
            emojis += "\U00002B1C" #white
        i += 1