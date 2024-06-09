def Balance(balance):
    print(f"Balance is ${balance:.3f}")
def deposit():
    deposit_amount=float(input(" Enter the amount to deposit: $ "))
    if deposit_amount <= 0 :
        print('***********************************************')
        print('You cannot deposit must be positive/greater than zero')
        return 0
    else:
        return deposit_amount      
    
    
def withdraw(balance):
    withdrawal_amount=float(input(" Enter the amount to withdraw: $ "))
    if withdrawal_amount > balance :
        print("You have insufficient funds to withdraw, try another amount")
        return 0
    elif withdrawal_amount< 5:
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print("You must withdraw at least $ 5 , please try again")
        return 0
    else:
        return withdrawal_amount
    
def main_function():    

    Running=True
    balance=0

    while Running:
        print('Welcome to our banking system')
        print('@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@@')
        print('Please enter the number as guided below')
        print('*****************************************')
        print("1. balance")
        print("2. withdraw")
        print("3. deposit")
        print("4. Exit")
        user_choice=input("Enter the number: ")
        if user_choice=='1':
            print('********************************')
            Balance(balance)
            
        elif user_choice=='2':
            print('$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$')
            balance-=withdraw(balance)
        elif user_choice=='3':
            print('################################')
            balance+=deposit()
        elif user_choice=='4':
            print('!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!')
            Running=False
            # exit()
        else:
            print("Invalid user choice", user_choice)
            print('%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%%')
    print("Thank you for using our system")
    print('~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~')
        
if __name__ is main_function():
    main_function()