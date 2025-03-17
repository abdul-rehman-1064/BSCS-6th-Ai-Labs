print ('hello world')

x=1
if x>0:
    print ('x is positive')

var = input("Enter a Number")
print("You entered: ", var)  

print("Output 1")
print("Output 2")

print("Output 01"); print("Output 02")

x=1
if x>0:
    print ('x is positive') 
# ->Error bcz of indentation

x=1
if x>0:
 print ('x is positive') 
# ->One space indentation

x=1
if x>0:
  print ('x is positive') 
# -> One tab Indentation

x="Hello"
print (type(x)) 
# ->Datatype str

x=12
print (type(x)) 
# -> Datatype int   

x=-12
print (type(x))
#  -> Datatype int

x=22.26
print (type(x)) 
# ->Datatype float

x=complex(1,2)
print (type(x))
#  -> Datatype Complex

x=1+2j
print (type(x)) 
# -> Datatype Complex

x=True
print(type(x)) 
# -> Datatype Bool

myList = [2,3,4,5]
print (myList)

myList = ["Abdul Rehman","Hussain","Usman","Luqman"]
print (myList)

myList = [2,"Abdul Rehman",1.12]
print (myList)

myList = []
print (myList)

myList = [2,3,4,5]
print (myList[0],myList[3])

myList = [2,3,4,5]
print (myList[-4],myList[0])

# String slicing
string1 = "PUNJAB UNIVERSITY"
print ( string1[ 1 : 5 ] )
print ( string1[ 6 : ] )
print ( string1[ : 6 ] )

# List
list1 = [ "List", 12, True ]

print ( list1 )

# List indices
print ( list1[0] )

print ( type ( list1[0] ) )
print ( type ( list1[1] ) )
print ( type ( list1[-1] ) )

# List slicing
print ( list1[ 0: 1 ] )
print ( list1[ 0 : 2 ] )

