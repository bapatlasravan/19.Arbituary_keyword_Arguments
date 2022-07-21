# ARBITARY keyword Arguments(**kwarg)
#we don't know how many arguments in the data so we use one *
"""def mydata(*data):
    print(data)
mydata("bapatla sravan",25,8247025669)""" #output:('bapatla sravan', 25, 8247025669)


#By using kwarg we print the above function in the form of dictinory
"""def mydata(**data):
    print(data)
mydata(name="bapatla sravan",age=25,mobile_number=8247025669)"""
#output={'name': 'bapatla sravan', 'age': 25, 'mobile_number': 8247025669}

#We are using .iteams() function to print the items inside the dictinory
"""def mydata(**data):
    for k,v in data.items():
        print(k,':',v)
mydata(name="bapatla sravan ",age=25,mobile_number=8247025669)"""
#output
# name : bapatla sravan 
# age : 25
# mobile_number : 8247025669


#by using if elif else statement getting output in the neat appearence
"""def mydata(**data):
    for k,v in data.items():
        if k == "name":
           print(k,'   :',v)
        elif k== "age":
            print(k,"    :",v)
        else:
            print(k,":",v)
mydata(name="bapatla sravan ",age=25,mob_num=8247025669)"""
#output
# name    : bapatla sravan 
# age     : 25
# mob_num : 8247025669 


#enetering kwarg arguments using input method
"""def mydata(**data):
    for k,v in data.items():
        if k == "name":
           print(k,'   :',v)
        elif k== "age":
            print(k,"    :",v)
        else:
            print(k,":",v)
mydata(name=input("enter name here: ") ,age=input("enter age here: "),mob_num=input("enter your mobile number: "))
"""

#user entering both key and values in dictinory

"""def mydata(data):
    for k,v in data.items():
        print(k,":",v)
userdata={}
e=1
while e != "0":
    key=input("enter key here : ")
    value=input("enter value here : ")
    userdata[key]=value
    print(mydata)
    e=input("enter 0 to escape 'or' press any key to continue ")
mydata(userdata)
"""


 