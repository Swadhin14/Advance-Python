print("lets start")

catelog={
    "grocery":{},
    "clothes":{},
    "Cell phones":{},
    "House appliances":{},
    "Furniture":{}
}
count=0
additems=[]
total=0
while True:
    choice=int(input("enter choice: "))
    if choice==1:
        print(catelog.keys())
        key=input("Enter key to store values")
        item=input("enter item name")
            #catelog[key]=item 
        value=int(input("enter value of the item") )      
        catelog[key][item]=value
    ## BUY ITEM   
    elif choice ==2:
        print(catelog)
        
        cate=input("enter catelog")
        things=input("enter elemets to buy by seeing the catelog")
        if things in catelog[cate].keys():
            additems.append(catelog[cate][things])
    elif choice==3:
        print("Items to buy :",end="/n")
        print(additems)
        for sum in additems:
            total+=sum
        print("total amount is :",total)
    elif choice==0:
        break