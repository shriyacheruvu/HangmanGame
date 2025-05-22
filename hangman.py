
#importing the time and random module
import time
import random

#welcoming the user
name = input("What is your name? ")

print ("Hello, " + name, "Time to play hangman!")

#wait for 1 second
time.sleep(1)

print ("Start guessing...")
time.sleep(0.5)

#making list of words
l=['tiger','lavender','castle','butcher','cycle','embezzle','espionage','frizzled','witchcraft','yummy','zombie','vampire','fluffy','butterfly','peekaboo','python']
word = random.choice(l)

#creates an variable with an empty value
guesses = ''

#determine the number of chances
turns = 10

# Create a while loop

#check if the turns are more than zero
while turns > 0:         

    # make a counter that starts with zero
    failed = 0             

    # for every character in secret_word    
    for char in word:      

    # see if the character is in the players guess
        if char in guesses:    
    
        # print then out the character
            print (char,end=""),    

        else:
    
        # if not found, print a dash and increase the failed counter with one
            print ("_",end=""),     
            failed += 1    

    # if failed is equal to zero
    if failed == 0: 
        # print won       
        print (" Congratulations,You won!")
    # exit the script
        break            
    # ask the user go guess a char
    guess = input(" guess a character:") 

    # set the players guess to guesses
    guesses += guess                    

    # if the guess is not found in the secret word
    if guess not in word:  
 
     # turns counter decreases with 1 (initially  9)
        turns -= 1        
 
    # print wrong
        print ("Oops!Wrong character")  
 
    #print how many turns are left
        print ("You have", + turns, 'more guesses')
 
    # if the turns are equal to zero
        if turns == 0:           
    
        # print lose
            print ("You Lose")