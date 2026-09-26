str1="this is a string" 
str2='''this is also a string'''
print(str1)
#Esacpe sequence characters
str3="this is a string . \twe are creating it in python."
print(str3)
str4="basketball"
str5="football"
final_str=str4+str5
#lenght command 
print(final_str)
len1=len(str1)
print(len1)
len2=len(str3)
print(len2)
final_str = str4 + " " + str5
print(final_str)
print(len(final_str))
#indexing 
name='shaarav'
name="B" + name[5:]
print(name)
str = "cristiano ronaldo "
print(str[1:4])
ch=str[3:8]
print(ch)
print(str[5:len(str)])
print(str[5:])
print(str[:4])
print(str[4:])
# negative indexing
str = "apple"
print(str[-3:-1])
#string functions
str= "iam a coder."
print(str. endswith("er."))
print(str .endswith("cod"))
print(str.capitalize())
print(str)
str = (str.capitalize())
print(str)
print(str.replace("o" , "a"))
print(str.replace("coder", "developer "))
print(str.find("coder"))
print(str.find("r"))
print(str.find("z"))
print(str.count("a"))
print(str.count("cr"))
str2 = input("enter ur name:")
print("lenght of ur name is:" , len(str2))
sentence= "hi iam$ a musician$"
print(sentence.count("$"))
# conditonal statments
age = 21
if(age >= 18):
    print("can vote")
    print("can drive")
if(False):
    print("can drive and vote")
light = "blue"

if(light == "red"):
    print("stop")

elif(light == "green"):
    print("go")

elif(light == "yellow"):
    print("look")

else:
    print("light. is broken ")

print("end of code ")
marks = int(input("enter student marks:"))

if marks >= 90:
    grade = "Grade A"
elif marks >= 80:
    grade = "Grade B"
elif marks >= 70:
    grade = "Grade C"
else:
    grade = "Grade D"

print("Grade of the student =", grade)

age = int(input("enter your age :"))
#nesting
if (age >= 18 and age <=79 ):
    print("can drive ")
    if (age >=80 and  age <=90):
     print("cannot drive ")

else:
    print("dont drive")

number = int(input("enter your number: "))
if(number % 2 == 0):
   print("even")
else:
   print("odd")

a = int(input("enter first number: "))
b = int(input("enter second number: "))
c = int(input("enter third number: "))
d = int(input("enter fourth number:"))

if(a>=b and a>=c and a>=d):
    print("a is the greatest number",a)
elif(b>=c and b>=d):
   print("b is the greatest number", b)
elif(c>=d):
    print( " c is the greatest number",c)
else:
    print("d is the greates number", d) 
 
number = int(input("enter your number:"))

if(number %7 == 0):
    print("multiple of 7")
else:
    print("not a multiple of 7")













 







