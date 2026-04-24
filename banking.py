def createAccount():
    accountNo=int(input("Enter Valid Account Number:"))
    CustomerName=input("Enter Your Name:")
    BranchCode=int(input("Enter Valid Branch Code:"))
    Mobile=int(input("Enter Your Mobile Number:"))
    
def show_balance(balance):
    print(f"Your Available Balance is ₹{balance:.2f}")

def deposit():
    amount=float(input("Enter Amount You Want to Deposit:"))

    if amount<0:
        print("Please Enter a Valid Amount")
    else:
        return amount

def withdraw(balance):
    amount=float(input("Enter Amount to Withdraw:"))

    if amount>balance:
        print("Insuficiant Balance")
        return 0
    elif amount<0:
        print("Please Enter Valid Amount to Withdraw")
        return 0
    else:
        return amount

def main():
    balance=0
    is_running=True

    while is_running:
        print("Banking Program")
        print("1.createAccount")
        print("2.Show Balance")
        print("3.Deposit")
        print("4.Withdraw")
        print("5.Exit")

        choice=input("Please Enter Your Choice from(1-5):")

        if choice=='1':
            createAccount()
        if choice=='2':
            show_balance(balance)
        elif choice=='3':
            balance+=deposit()
        elif choice=='4':
            balance-=withdraw(balance)
        elif choice=='5':
            is_running=False
        else:
            print("Please Enter Valid Choice")

    print("Thank you!! Have a Good Day.")
    print("Visit Again")

        
if __name__=='__main__':
    main()
    
