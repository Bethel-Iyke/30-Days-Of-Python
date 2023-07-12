import sys
import math

if sys.version_info.major == 3:
    print("version:", sys.version)
else:
    print("version:", sys.version)

print(3 + 4)        #addition(+)
print(4 - 3)        #subtraction(-)
print(3 * 4)        #multiplication(*)
print(3 % 3)        #modulus(%)
print(4 / 3)        #division(#)
print(4 // 3)       #floor division(//)
print('Bethel')     #name
print('Udeani')     #family name
print('Nigeria')    #country
print('I am enjoying 30 days of python')           #string
print(type(10))     #int
print(type(9.8))    #float
print(type(3.14))   #float
print(type(4 -4j))  #complex
print(type(['Bethel', 'Python', 'Finland']))       #list
print(type('Bethel'))      #string
print(type('Udeani'))      #string
print(type('Nigeria'))     #string
print(type(20))            #int
print(type(4.5))           #float
print(type(1+3j))          #complex
print(type('Mine'))        #string
print(type(True))          #boolean
print(type([1, 2, 3, 'me', 'joy']))           #list
print(type(('January', 'March', 'June')))     #tuple
print(type({'Orange', 'Mango', 7, 'Apple'}))  #set
print(type({'name': 'Bethel', 'country': 'Nigerai' }))    #dictionary

x1,y1 = 2, 3
x2, y2 = 10, 8
distance = math.sqrt(x2 - x1) **2 + (y2 -y1) **2
print("The euclidean distance is:", distance)  