#PYTHON FINAL CHAPTER 12-7 RECURSIVE POWER METHOD
# BY, JEFF BRATANOV 7/22/2019
#BEGIN PROGRAM
#FUNCTIONS
def Main ():
    # Call and reset variables to prompt for input and run function with. 
    # First part user sees when running and rerunning program.
    global RAISE
    global EXPONENT
    global COUNT
    global RESULT
    RAISE = 0
    EXPONENT = 0
    ANSWER = 0
    RESULT = 0
    COUNT = 0
    print ("Welcome to Recursive Power Program, Where Power comes without a big bill!")
    RAISE = input("Let's start with a number to RAISE to a power :")
    EXPONENT = input("Now Let's pick an EXPONENT: ")
    if int(EXPONENT) < 1:
        # Function repeats again if unusable numeric values are given.
        print ("Cannot use 0 or Negative Numbers!")
        Main ()
    print ("")
    RESULT = RAISE
    print (RAISE, "to the power of:", EXPONENT, ".")
    # With variables set by user call Power function to run.
    Power (EXPONENT)
def Power (EXPONENT):
    # Take in EXPONENT call RAISE & RESULT variables.
    global RAISE
    global RESULT
    # Useing EXPONENT as countdown, Check for 0 value.
    # finish up if 0, or run again if not.
    if EXPONENT == 0:
        print ("Finished!")
        PlayAgain ()
    else:
        # Power raising part, RESULT keeps previous TOTAL value.
        # Shows the math involved with raising to power.
        # EXPONENT reduces by 1 to count down, function calls itself again.
        TOTAL = (int(RESULT)) * (int(RAISE))
        print (RESULT, "x", RAISE, "=", TOTAL)
        RESULT = TOTAL
        EXPONENT = (int(EXPONENT)) - 1
        Power (EXPONENT)
def PlayAgain ():
    # Courtasy function for easy restart or finish.
    print ("\n")
    AGAIN = input("Do you want to try again? (Y/N)").upper()
    if AGAIN == "Y":
        Main ()
    else:
        print ("Goodbye")
#START PROGRAM
#Kicks off main function to start program
Main ()

#END OF PROGRAM
