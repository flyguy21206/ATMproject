#This is ATM project for Reskill Americans
#Get Username and Password
name = input("What is your name? \n")
allowedUsers = ['Richard','Mike','Love']
allowedPassword = ['passwordRichard','passwordMike','passwordLove']

if(name in allowedUsers) :
    password = input("Your password? \n")
    userId = allowedUsers.index(name)
    
    #Request action from user if Password and UserName are correct
    if(password == allowedPassword[userId]) :
        print('Welcome %s' % name)
        from datetime import datetime
        now = datetime.now()
        print("now =", now)
        dt_string = now.strftime("%m/%d/%Y %H:%M:%S")
        print("date and time =", dt_string)
        print('These are the available options:')
        print('1. Withdrawal')
        print('2. Deposit')
        print('3. Complaint')
        

        selectedOption = int(input('Please select an option:'))

        print(selectedOption)
        #These are the steps for Withdrawal
        if(selectedOption == 1):
            print('You selected %s.' % selectedOption)
            withdrawal=input('How much would you like to withdraw? \n')
            print('Please take your cash')

         #Go Back to main menu after Withdrawal completed
           
            print('These are the available options:')
            print('1. Withdrawal')
            print('2. Deposit')
            print('3. Complaint')
            
        #These are the steps for Deposit

        elif(selectedOption == 2):
            print('You selected %s.' % selectedOption)
            deposit=input('How much would you like to Deposit? \n')
            print('Your current balance is 5,000')
        
        #Go Back to main menu after Deposit completed
           
            print('These are the available options:')
            print('1. Withdrawal')
            print('2. Deposit')
            print('3. Complaint')
        
        #These are the steps for Complaint
        
        elif(selectedOption == 3):
            print('You selected %s.' % selectedOption)
            complaint=input('What issue would you like to report? \n')
            print('Thank you for contacting us with your issue!')

        #Go Back to main menu after Complaint completed
           
            print('These are the available options:')
            print('1. Withdrawal')
            print('2. Deposit')
            print('3. Complaint')

        else:
            print('Invalid Option selected, please try again')
            
    else:
        print('Password Incorrect, please try again')

else:

    print('Name not found, please try again')




