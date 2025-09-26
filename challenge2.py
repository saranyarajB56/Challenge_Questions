# create a list of first 100 numbers from that list                                                                                                                                                                                                               create a list of first 100 numbers 
# create a  list for all even numbers
# create a list for all odd numbers
# create a list for numbers that are divisible by both 5 and 3.
num=[]
even=[]
odd=[]
div=[]
for i in range(1,101):
    num.append(i) 
print("List of numbers 1-100 : ",num)
for i in num:
    if(i%2==0):
        even.append(i)   
    else:
        odd.append(i)    
    if(i%3==0 and i%5==0):
        div.append(i)    

print("List of Even numbers are :\n ",even)
print("List of Odd numbers are :\n",odd)
print("List of Numbers Divisible by both 3 and 5 are :\n", div)