import random

def getanswer(answerNumber): #creating a function called getAnswer() that requires one parameter to be passed through it
    if answerNumber ==1:
        return 'It is certain' #"return" makes the "value" of the function become whatever is returned, almost like the function itself becomes a variable 
    elif answerNumber ==2:
        return "It is decidedly so"
    elif answerNumber == 3:
        return "yes"
    elif answerNumber == 4:
        return "reply hazy try again"
    elif answerNumber ==5:
        return "Ask again later"
    elif answerNumber == 6:
        return "Concentrate and ask again"
    elif answerNumber == 7:
        return "My reply is no"
    elif answerNumber == 8:
        return "Outlook not so good"
    elif answerNumber == 9:
        return "Very doubtful"

#remember, this just DEFINES the function, the function isnt actually being run yet 

r = random.randint(1,9) #this sets the result of running this function to the variable r
                        #random.randint is the function, and the 2 numbers in the parenthesis are the parameters being passed through it 
                        #The value that this function returns is being set to r 
fortune = getanswer(r) #doing it this way means we dont have to type "print" under every single if statement
                        #the string that the function returns is being assigned to the variable fortune

tellmethefuture = print(fortune)

tellmethefuture

    