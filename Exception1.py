
"""print("Hello")
print("My Dear")
print("Friend")
print(5/0)
print("I am")
print("Shiva")

print("Hello")
print("My Dear")
print("Friend")
try:
 print(5/0)
except ZeroDivisionError:
    print("sorry not executing code")
else:    
 print("I am")
 print("Shiva")


print("Hello")
print("My Dear")
print("Friend")
try:
 print(5/2)
except ZeroDivisionError:
    print("sorry not executing code")
else:    
 print("I am")
 print("Shiva")

stu={"sno":100,"sname":"shashi","sage":25}
print("stu:",stu)

key=input("Enter a key;")
value=stu[key]
print("value is:",value)


stu={"sno":100,"sname":"shashi","sage":25}
print("stu:",stu)

key=input("Enter a key;")
try:
 value=stu[key]
except KeyError:
    print("KE : specified key not found")
else:    
 print("value is:",value)

lst=[10,12.12,"shashi","nani",30,"sudha"]
print("lst is:",lst)

pos=int(input("Enter index pos:"))
item=lst[pos]
print("item is:",item)"""




lst=[10,12.12,"shashi","nani",30,"sudha"]
print("lst is:",lst)

pos=int(input("Enter index pos:"))
try:
 item=lst[pos]
except IndexError:
    print("IE: sorry index pos is invalid")
else:    
 print("item is:",item)












