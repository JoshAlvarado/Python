# Joshua Alvarado 09/28/2019
# www.linkedin.com/in/joshua-alvarado/

import random
def main():
    global s #gives me the ability to use S in other functions
    s = float(input("""What is the highest number possible?
                    """))
    output()
    
def output():
    roll = random.randint(1,s) #Picks a random number in between the given numbers
    print("You rolled the number " +str(roll)+".")
    x = float(input("""Would you like to roll again? Entering 1 will reroll, entering 2 will give you the ability to change the highest number and entering any other number will close the program.
              """))
    if x==1: 
        print("You decided to roll again.")
        output()
    elif x==2:
        print("You decided to change the highest number.")
        main()
    else: 
        exit()  
        
if __name__ == '__main__':
	main() 
    
