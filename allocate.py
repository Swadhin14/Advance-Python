rooms ={
    101:None,
    102:None,
    103:None,
    104:None,
}

occupied = set()

while True: 
    print("\n1.Allocated Rooms")
    print("2.Vacate Rooms")
    print("3.Room Info")
    print("Exit")

    choice = int(input("Enter Your Choice: "))

    if choice == 1:
        name = input("Enter Your Name: ")
        room = int(input("Enter room no: "))

        if room in rooms:
            if room in occupied:
                print("room occupied")
            else:
                occupied.add(room)
                rooms[room]=name
                print(f"Room {room} is allocated")
    if choice==2:
        roomno=int(input("enter room no to vacate"))
        if(roomno in occupied):
            print("room is already vaccated")
        else:
            occupied.remove(roomno)
            rooms[roomno]=None
            print("room vacated")
    if choice ==3:
        print("enter roomno to see iinfo")
        roomno=int(input())
        if roomno in occupied:
            print("room no",roomno,"is occupied by",rooms[roomno])
        else:
            print("not occupied")
    if choice==4:
        break
    
    