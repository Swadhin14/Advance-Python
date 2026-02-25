# event tracker
entered_std = set()
rejected_std = set()

n = int(input("Enter no of student: "))

for i in range(n):
    name = input("Enter number of student: ")

    if name in entered_std:
        print(name, "already entered. entry rejected")
        rejected_std.add(name)

    else:
        print(name, "entry accepted")
        entered_std.add(name)
print(len(entered_std))
for a in entered_std:
    print(a)
for b in rejected_std:
    print(b) 
