x = 10
print(x>6 and x<12)
print(x>20 and x>6)
print(x>20 or x>6)
print(x>6 or x<6)
print(not(x>6 or x<6))
print(not(x))

y = 0
print(not(y))

str1 = 'i am learning python'
str2 = 'i'
print('am' in str1)
print(str2 in str1)
print(str1 in str2)

li1 = [1,2,3,4]
print(1 in li1)
print(1 not in li1)
print(5 in li1)
print(6 not in li1)

#identity operator__'is'
a = -8
b = -8
print(id(a))
print(id(b))
print(a is b)

x = 10
y = 10
print(id(x))
print(id(y))
print(x is not y)

#shift_operator
#Right shift>>
#left shift<<
a = 12
print(a<<2)
b = 12
print(b>>2)
c = 7
print(c>>3)

f = 10
g = 4
print(f & g)

a = 10
b = 4
print(a | b)
a = 10
b = 4
print(~a)


#if(a%2 == 0):
  #  print("Even")
#else:
#    print("odd")

v = 20
m = 30
if(v>m):
    print("v is greater")
    print("hello")
a = 10
if(a>=10):
    print("hello")
else:
    print("Less than 10")

num = int(input("Enter a number"))
if(num%7==0):
    print("num is divisible by 7")
    print("hello")
else:
    print("num is not divisible by 7")

a = 27
b = 27.0
if(a==b):
    print("a and b are equal")
else:
    print("a and b are not equal")

a = 1
while(a<=10):
    print(a)
    a += 1

a = "Hello\tworld"
print(a)


