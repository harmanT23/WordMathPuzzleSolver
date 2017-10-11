# -*- coding: utf-8 -*-
"""TatlaHarmanpritA4Q1
￼￼

COMP 1012 SECTION A01
INSTRUCTOR Terrance H. Andres
ASSIGNMENT: A4 Question 1
AUTHOR Harmanprit Tatla
VERSION 2015 - March - 14

PURPOSE: To create a program that solves user selected and user entered puzzles 
by trying all possible solutions. """

#Imports
import time
import string
import sys 

#Tuple of word math puzzles along with prompt to enter own puzzle
PUZZLES = ("2BANANA == 102020", "3HE + ME == WE", 
           "7TWO + TWO == FOUR", "7FIVE + FIVE == SEVEN",
           "8SIX + SEVEN + SEVEN == TWENTY", 
           "9SEND + MORE == MONEY", 
           "9SPRING + RAINS + BRING + GREEN == PLAINS",
           "9CLOCK + TELLS + TIME == CHIMES",
           "9TERRIBLE + NUMBER == THIRTEEN",
           "0ENTER YOUR OWN MATHWORD PUZZLE")

def main():
    """When called this function executes the word math puzzle solving program.
    """
    
    #Prints title with each letter single spaced
    print '%45s' % (' '.join('WORD MATH PUZZLES')) 
    
    #Later used to print time and date before and after a puzzle solved
    DATE = '\nDate: ' + '...' * 10 # * 10 so to print 30 dots.
    
    STOP_CODE = 'Q' #Code to quit program
    
    #Call to menu, displays menu of choices to user and returns their choice.
    choice = menu(PUZZLES) 
    
    #Keeps looping for input, until user enters Q to quit.
    while choice != STOP_CODE:
        
        #If first character of puzzle in position choice in PUZZLES is 0; user 
        #wants to enter own puzzle.
        if PUZZLES[choice][0:1] == '0':
            
            #Calls getPuzzle to let user enter own puzzle; returns user puzzle
            #with largest digit allowed to solve it as first character.
            userPuzz = getPuzzle() 
            
            #If largest digit allowed to solve user puzzle < '4', then solve.
            if userPuzz[0:1] < '4':
                print DATE + time.ctime() + '\n' #Begin time for solution
                
                #solves user entered puzzle using largest digit allowed.
                #prints and returns solutions. 
                solvePuzzle(userPuzz[1:], int(userPuzz[0:1])) 
            
            #If largest digit allowed to solve user puzzle > '4', then print
            #wait message and solve puzzle.
            else:
                print DATE + time.ctime() + '\n' #Begin time for solution
                
                #Tells user to wait for solution; since many solutions to check
                print 'Solving the puzzle: %s' % userPuzz[1:]
                print 'Calculating permutations of %d items; please wait ...'%(
                      int(userPuzz[0:1]) + 1) # +1; since num of items to 
                                              # permute is largest digit + 1.

                #Causes above output to be printed before solutions printed
                sys.stdout.flush() 
                
                #Solves user entered puzzle, prints and returns solutions
                solvePuzzle(userPuzz[1:], int(userPuzz[0:1])) 
        
        #If first character of puzzle in position choice in PUZZLES < '5' user
        #wants a predefined puzzle solved that has largest digit allowed
        #to solve it < '5'
        elif PUZZLES[choice][0:1] < '5':
            print DATE + time.ctime() + '\n' #Begin time for solution
           
            #Solves user selected puzzle, prints and returns solutions.
            solvePuzzle(PUZZLES[choice][1:], int(PUZZLES[choice][0:1])) 
        
        #Else first character of puzzle in position choice in PUZZLES > '5'
        #this means user wants a predefined puzzle solved that has largest 
        #digit allowed to solve it > '5'. 
        else:
            print DATE + time.ctime() + '\n' #Begin time for solution
           
            #Tells user to wait for solution, as it will take time.
            print 'Solving the puzzle: %s' % PUZZLES[choice][1:]
            print 'Calculating permutations of %d items; please wait ...'% (
                   int(PUZZLES[choice][0:1]) + 1) # +1; since num of items 
                                                  #to permute is largest digit
                                                  #+1.
          
            sys.stdout.flush() #Causes above output to print before solution
           
            #Solves user selected puzzle, prints and returns solutions
            solvePuzzle(PUZZLES[choice][1:],int(PUZZLES[choice][0:1])) 
        
        print DATE + time.ctime()  #Finish time when all solutions found
        choice = menu(PUZZLES) #Asks user again for input.
           
    theEnd() #Termination output, called once user quits program.
    
    return

def getPuzzle():
    """When called, prompts the user to enter a word math puzzle to be solved, 
       and the largest digit allowed to solve it. Thereafter, returns the user 
       entered puzzle with the largest digit allowed to solve it at front."""
    
    userPuzzle = '' #later holds user puzzle with largest digit at front
    
    PUZZLE_PROMPT = 'Enter a word math puzzle:\n' #Prompt to enter puzzle
    warning = '\b' #used in error checking.
   
    #Loops until length of warning is 0, occurs once user enters valid puzzle
    while len(warning) > 0:
        
        #Asks user to enter puzzle
        inputPuzzle = raw_input(warning + PUZZLE_PROMPT).strip() 
        warning = ''
        
        #If user puzzle does not contain '==' then puzzle is invalid.
        if '==' not in inputPuzzle:
            warning += "Puzzle '%s' does not contain '=='\n\n" % inputPuzzle
        
        #If user puzzle has more than 10 unique letters it is invalid.
        if len(lettersIn(inputPuzzle)) >  10:
            warning += ('Puzzle can have at most 10 unique letters;'
                        ' %s has more than 10 unique letters.\n\n') % (
                        inputPuzzle)
        
        #If len(warning) == 0 then user has entered a valid puzzle and will now 
        #ask user to enter largest digit to solve puzzle.
        if len(warning) == 0:
            
            #Prompt to user to enter largest digit
            DIGIT_PROMPT = 'What is the largest digit allowed?\n'
            warning  = '\b' #reset warning to use in error checking in new case
            
            #Loops until len(warning) == 0, occurs once user enters valid digit
            while len(warning) > 0:
                
                #Asks user to enter largest digit to solve puzzle.
                inputDigit= raw_input(warning + DIGIT_PROMPT).strip()
                warning = ''
                
                #If len(inputDigit) > 1 character, or if it is not between
                #‘0’ and ‘9’ then invalid.
                if len(inputDigit) > 1 or not ('0' <= inputDigit<= '9'):
                    warning  += '%s is not a valid digit between 0 - 9\n\n' % (
                                inputDigit)
                
                #If (inputDigit + 1) < number of unique letters in entered 
                #puzzle then invalid.
                elif (int(inputDigit) + 1) < len(lettersIn(inputPuzzle)):
                    warning += ('Largest digit + 1 must be greater than or ' 
                                'equal to %d, the number of unique letters in' 
                                ' your puzzle.\n\n')  % (
                                len(lettersIn(inputPuzzle)))
                                
                #Else, user digit valid; add it to front of user puzzle that 
                #has all letters capitalized. 
                else:
                    userPuzzle = inputDigit + inputPuzzle.upper()
                    
    return userPuzzle
    

def lettersIn(text):
    """Given a string, returns a list of all the distinct letters in it 
       capitalized and alphabetically ordered. """
    
    #Set of the unique characters in text with letters capitalized.
    textSet = set(text.upper()) 
    
    #Set of the capital letters in the alphabet
    UPPER_CASE_SET =  set(string.ascii_uppercase) 
    
    #Takes intersection of textSet and UPPER_CASE_SET to obtain the set,
    #comprised solely of the capital letters in text, then converts that set to 
    #list with the letters sorted alphabetically. 
    sortedLetterList = sorted(textSet.intersection(UPPER_CASE_SET))
    
    return sortedLetterList


def menu(listPuzzles):
    """Given a list of puzzles, creates a formatted menu with choices referring 
       to the puzzles in the list. Returns the users choice as either an 
       integer, or the stop code 'Q'. """
    
    #Largest digit choice can be in the menu; -1 since choices begin at 0.
    MAX_CHOICE = str(len(listPuzzles) - 1) 
    
    #Later assigned a formatted menu with choices, and used as a prompt.
    formattedMenu = 'Enter the number of one of these puzzles (Q to quit):\n\n'
    
    #Formats puzzles in listPuzzles into a list of choices; if digit in front
    #of any puzzle is 0 then don't add "using digits from 0 to" + \n.
    for loc, wordPuzzle in enumerate(listPuzzles):
        formattedMenu += (('%d. ' % loc + wordPuzzle[1: ]) +
                          (' using digits from 0 to %s' % wordPuzzle[0:1] + 
                           '\n') * (wordPuzzle[0:1] != '0' ))

    warning = '\b' #used in error checking
    
    #Loops until length of warning == 0, occurs when user enters either a
    #valid digit or the stop code (q or Q). 
    while len(warning) > 0:
        
        #Prints warning, then formatted menu, which asks user for input.
        print warning
        print formattedMenu    
        #Prints a symbol that next to, the user can enter input.
        userInput = raw_input(U"\N{BLACK RIGHTWARDS ARROWHEAD} ").strip()
        warning = ''
       
        #If user enters either 'q' or 'Q',  capitalize it and return.
        if userInput.upper() == 'Q':
            userInput = userInput.upper()
        
        #Else if,len(userInput) > 1 character, or userInput not a digit between 
        #'0' and MAX_CHOICE then userInput is invalid.
        elif len(userInput) > 1 or not ('0' <= userInput <= MAX_CHOICE):
	     warning += 'You entered %s; enter a valid digit, or Q\n' % (
	                userInput)
        
        #Else, userInput is a valid digit; convert to an integer then return.
        else:
            userInput = int(userInput)
           
    return userInput

def permutations(NN):
    """Given a positive integer NN, returns a list comprising all the 
       permutations of the digits from 0 to NN-1."""
    
    #If NN a positive integer then compute permutations.
    if NN > 0 and type(NN) == int:
       
        #Following blocks of code use
        #"A Pseudo-Code Representation (Countdown)", an algorithm, to compute 
        #permutations. Created by: Dhr. Phillip Paul Fuchs available at 
        #http://www.quickperm.org/
       
        #list of single chararacter strings from 0 to NN-1; whose permutations 
        #will be computed.
        itemList = ['%d' % num for num in range(NN)]  
       
        #List of digits from 0 to NN+1; used to control loop iterations.
        intList = range(NN + 1) 
       
        i_= 1 #index variable; later used to swap items in itemList
       
        #List that will hold the permutations, with first permutation added
        permutedDigitList = [''.join(itemList)]
       
        #Loops until i_ is larger than NN.
        while i_< NN:
           
            intList[i_] = intList[i_] - 1 #Reduces value at position i_ by 1
           
            j_ = 0 #index variable; later used to swap items in itemList.
           
            #If i_ is odd, assign integer at position i_ in intList to j_ 
            if i_ % 2 != 0:
                j_ = intList[i_]
          
            #Swap items at position j_ and i_ in itemList with one another;
            #Then join the new sequence of items in itemList to form a new 
            #permutation, and then add to list of permutations..  
            swap(itemList, j_, i_)
            permutedDigitList += [''.join(itemList)]
           
            i_= 1 #reset index variable to 1
           
            #loops until element at position i_ in intList is != 0. 
            while intList[i_] == 0:
                intList[i_] = i_ #assigns element at position i_ value of i_
                i_ += 1 #increments index variable by 1
    
    
    #Else NN is invalid, cause program to fail fast to avoid bad output 
    else:
        assert False, 'ERROR: Cannot compute permutations for NN = %r' % NN
    
    return permutedDigitList                                            

def solvePuzzle(wordMath, maxDigit):
    """Given a word math puzzle and the maximum digit allowed to solve it; 
       prints the solutions to the puzzle, and additionally returns a list of 
       the solutions."""
   
    #Calls permutations to obtain list of all permutations of digits from 0 to 
    #maxDigit. Use maxDigit+1 in call to permutations so largest digit used to
    #compute each permutation is maxDigit.
    permutationList = permutations(maxDigit + 1) 
    
    #list of distinct capital letters in puzzle
    distinctLetters = lettersIn(wordMath) 
    
    INVALID = ' 0' #An invalid sequence of characters a solution cannot have
    solutionList = [] #Will hold all unique solutions to the puzzle
    puzzleSolve = ' ' #Later holds solutions to the given word math puzzle.
    
    #Prints the puzzle whose solutions are to be found.
    print 'PUZZLE:    %s' % wordMath
    
    #Assigns each permutation in permutationList to digits
    for digits in permutationList:
        
        #Blank space added to left of puzzle, in order to check if INVALID 
        #sequence present in beginning of puzzle.
        puzzleSolve = ' ' + wordMath 
        
        #Replaces all occurrences of a letter in the puzzle with a digit from 
        #digits
        for letter, digit in zip(distinctLetters, digits):
            puzzleSolve = puzzleSolve.replace(letter, digit)      
            
        #if invalid is not in puzzleSolve and eval is true then puzzleSolve
        #is a valid solution. 
        if (INVALID not in puzzleSolve) and eval(puzzleSolve):
            
            #If puzzleSolve not a repeated solution then print and add to list.
            if puzzleSolve not in solutionList:
                print 'SOLUTION: %s' % puzzleSolve
                solutionList += [puzzleSolve]
                
    #If len(solutionList) == 0; this means there are no solutions for given 
    #puzzle using the digits form 0 to maxDigit.
    if len(solutionList) == 0:
        print 'NO SOLUTION USING DIGITS FROM 0 TO %d' % maxDigit
    
    return solutionList

def swap(aList, pos0, pos1):
    """Given a list and the index of two elements in it, swaps those two 
       elements with one another in the list. """ 
       
    #Swaps elements at pos0 and pos1 with one another in aList
    aList[pos0], aList[pos1] = aList[pos1], aList[pos0]
    
    return 
                                                                                                                                                                                
def theEnd():
    """Prints termination message to indicate succesful completion of 
       program."""
    
    print '\nProgrammed by Harmanprit Tatla'
    print 'Date:', time.ctime()
    print 'End of processing...' 
    
    return

main() #Call to main, used to start puzzle solving program