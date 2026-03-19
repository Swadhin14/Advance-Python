def sum(list1,target):
    for i in list1:
        diff=target-i
        if diff in list1 and diff != i:
            return diff,i
        
list1=[3,2,4]
print(sum(list1,6))