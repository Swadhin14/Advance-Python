balance=0
transaction=[]
a=0
while a!=3:

    passw=int(input("Enter password"))
    if(passw==123):


        while True:
            print("\n Enter amount")
            print("\n withdraw")
            print("\n Statement")
            print("\n check balance")
            a=int(input(" enter choice to do "))
            if(a==1):
                print("enter amount to deposit")
                deposit=int(input("enter value"))
                balance+=deposit
                print("deposited amount")
                transaction.append(deposit)
            
            elif(a==2):
                b=int(input("Enter amount to withdraw"))
                if(b<=balance):
                    balance-=b
                    print("amount withdrawb")
            elif(a==0):
                print("Balance amount",balance)
            elif(a==5):
                break
        break
    else:
        a+=1
        pass