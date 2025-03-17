count =0
while (count <3):
    count = count + 1
    print("Python")

i = 0                           
while ( i < 5 ) :               
    print ( i )                
    i = i + 1                   
print () 


color_list = [ "red", "yellow", "blue", "red", "white" ]   
for i in color_list :               
    print( i )
print ()

fruit_tuple = ( "apple", "mango", "banana", "kiwi", "tomato" )   
for i in fruit_tuple :               
    print( i )
print ()

name_string = "PUNJAB UNIVERSITY"   
for i in name_string :        
    print( i )
# print ()

for i in range ( 5 ) :                          
    print ( i )
print ()

for i in range ( 2, 5 ) :                    
    print ( i )
print ()

for i in range ( 1 , 10 , 2 ) :               
    print ( i )
print ()

for number in range( 1, 10 ) :
    print ( number )
    if ( number == 5 ) :
        break
print()

def myName () :
    print ( "PUNJAB UNIVERSITY" )


myName()                                        
print ()

def fullName ( first_name, last_name ) :      
    print ( f"Your full name is {first_name} {last_name}." )


fullName ( "Abdul" , "Rehman" )
fullName ( "Muhammad" , "Ali" )
fullName ( "Hussain" , "Manj")
print ()

def sum ( num1, num2 ):
    print ( num1 + num2 )


sum ( 10 , 20 )
sum ( 5 , -10 )
print ()


def listSum( full_list ) :
    sum = 0 
    for index in range ( len ( full_list ) ) :
        sum += full_list[ index ]
    print ( "Sum =", sum )


listSum ( [ 10, 20, 30, 40 ] )
listSum ( [ -1, 1, 0, 3, 4 ] )
listSum ( [ 1 + 2j, 2 + 5j ] )
print ()


def countryName ( country = "Pakistan" ) :
    print ( "Your country is", country )


countryName ( "India" )
countryName ( "Australlia" )
countryName ()
print ()


def findValue ( full_list, value ) :
    for i in range ( len ( full_list ) ) :
        if ( full_list[i] == value ) :
            return i
    return -1

numbers_list = [ 5, 10, 15, 0, 12 , "1" ]
index = findValue ( numbers_list, 1 )
if ( index == -1 ) :
    print ( "Not Found" )
else :
    print ( "Found at index", index )
print ()


def num3Value ( num1, num2, num3 ) :           
    print ( "Num3 =", num3 )

    
num3Value ( num3 = -1, num2 = 5, num1 = 100 )
num3Value ( num3 = 1000, num2 = 75, num1 = 2 )
print ()


def product ( *numbers ) :
    prod = 1
    for num in numbers :
        prod = prod * num 
    print ( "Product =", prod )

        
product ( 10, 5 )
product ( 1, 2, 12 )
product ( 5, 4, 0)
product ( 10, "* ")
print ()

class Test :
    x = 5
    
obj1 = Test() 
print ( obj1.x )

class Person :
    def __init__ ( this, name, age ) :                
        this.name = name
        this.age = age
        

per1 = Person ( "Abdul", 19 )
per2 = Person ( "Rehman", 20 )                          
print ( per1.name, per1.age )
print ( per2.name, per2.age )

