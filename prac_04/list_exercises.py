def main():
    numbers = []
    usernames = ['jimbo', 'giltson98', 'derekf', 'WhatSup', 'NicolEye', 'swei45', 'BaseInterpreterInterface', 'BaseStdIn', 'Command', 'ExecState', 'InteractiveConsole', 'InterpreterInterface', 'StartServer', 'bob'] 
    
    username = input("What is your name: ").lower()

    if username in usernames:
        print("Access granted")
    else:
        print("Access denied")
        return
    
    for _ in range(0,5):
       num = float(input(f"Enter a number :"))
       numbers.append(num)

    print(f"The first number is {numbers[0]}")
    print(f"The last number is {numbers[4]}")
    print(f"The smallest number is {min(numbers)}")
    print(f"The largest number is {max(numbers)}")
    print(f"The average of the numbers is {sum(numbers)/len(numbers)}")
    

main()