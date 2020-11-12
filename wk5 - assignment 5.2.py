5.2 Write a program that repeatedly prompts a user for integer numbers until the user enters 'done'. 
Once 'done' is entered, print out the largest and smallest of the numbers. 
If the user enters anything other than a valid number catch it with a try/except and put out an appropriate message and ignore the number.
Enter the numbers from the book for problem 5.1 and Match the desired output as shown.
'

largest = None
smallest = None
while True:
    inp = raw_input("Enter a number: ")
    if inp == "done" : break
    try:
        num = int(inp)
    except ValueError: #and not all errors!
        print('Invalid input')
    else: 
        # This block will execute if no exception is caught.
        # Yes, this is valid python.
        if smallest is None: #first number!
            smallest = num
            largest = num
        elif num < smallest:
            smallest = num
        elif num > largest:
            largest = num

print('Maximum is', largest)
print('Minimum is', smallest)
