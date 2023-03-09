
def Ussd():
    Dialer = input("Please dial a code to Start: ")
    if Dialer == "*123#":
        print("1.Buy Airtime\n2.Buy Data\n3.Transfer")
        first_option = int(input("Enter your option: "))
        if first_option == 1:
            print("1.Self\n2.Third Party")
            second_option = int(input("Enter another option: "))
            if second_option == 1:
                Amount = int(input("Enter an amount:"))
                print("You have purchased the sum of",Amount,"to your own Phone Number.")
            elif second_option == 2:
                Phone_Number = int(input("Enter a phone number: "))
                Amount = int(input("Enter an Amount: "))
                print("You have successfully purchased Airtime of",Amount,"to",Phone_Number)
            else:
                print("Incorrect entry.")
        elif first_option == 2:
            Data_Network = input("Enter a network type: ")
            Data_Size = int(input("Please enter the number of GB you want? "))
            Phone_Number = int(input("Please enter a number: "))
            print("You have successfully purchased",Data_Network,Data_Size,"GB","to",Phone_Number)
        elif first_option == 3:
            Bank_Name = input("Enter your Bank Name: ")
            Bank_Account = int(input("Enter an Account Number: "))
            Amount = int(input("Enter an Amount: "))
            print("You have successfully transfered",Amount,"to",Bank_Name,Bank_Account)
        else:
            print("Wrong entry please retry")
    else:
        return Ussd()
Ussd()