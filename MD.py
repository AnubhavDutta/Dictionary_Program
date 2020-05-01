# URL - https://youtu.be/a8Vp9amg5bs
words={} # Dictionary / Hashmap
while(True):
    try:
        print("1 : Add Word\n2 : Search Word\n3 : Delete Word:\n4 : Display All Words\n5 : Exit\nEnter your option:",end=" ")
        option=int(input())
        if (option>5 or option<1):
            raise Exception() #In case the option is out of range
    except: 
        #In case of input can not be converted to string or is out of range
        print("Invalid Input. Please check your input and try again.\n")
        continue

    if (option==1): # To Add Word
        w=input("Enter the word: ")
        w=w.upper()
        meaning=input("Enter the meaning: ")
        words[w]=meaning
        print("The word has been added to the dictionary\n")

    elif (option==2): # To Search Word
        w=input("Enter the word to search: ")
        w=w.upper()
        try:
            meaning=words[w]
            print(w,":",meaning,"\n")
        except:
            print("The word does not exist\n")

    elif (option==3): # To Delete Word
        w=input("Enter the word to delete: ")
        w=w.upper()
        try:
            del words[w]
            print("The word has been deleted\n")
        except:
            print("The word does not exist\n")
            
    elif (option==4): # To display all Words
        for item in words.keys():
            print(item,":",words[item])
        print()
    else: # To Exit the program
        break