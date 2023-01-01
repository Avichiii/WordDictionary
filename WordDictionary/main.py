def my_Dictionary():
    
    ask_dictionary = {
        "hello": "is a way to greet",
        "goodbye": "when you part your way with someone",
        "happy" : "feeling good :)",
        "sad" : "feeling uneasy and not in your usual self :(",   
        }
     
    word = input("enter a word: ")
    for x in ask_dictionary:
        if word == "":
            print("enter a valid word!")

            break
        
        elif word == x:
            print(word + ": " + ask_dictionary[word])

            break


            
        
my_Dictionary()