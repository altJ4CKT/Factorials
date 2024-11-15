number = int(input("Enter a number to calculate the factorial: "))

def Factorial(number):
    a = number
    if number < 2:
        a = 1
        return a
    else:
        while number > 1:
            a = a * (number - 1)
            number -= 1
        return a

if number <= 1558 and number >= 0:
    print(f"The factorial of {number} is {Factorial(number)}")z

else:
    print("Please enter a valid number")

    


        

        
    
    


    