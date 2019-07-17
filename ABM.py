import random

#creates variables y0/x0
#and assigns ramdom start values between 0 and 99
y0 = random.randint(1,99) 
x0 = random.randint(1,99) 

#generates a ramdon number between 0 and 1 and
#makes it the value of varible random_number
#random_number = random.random() #this function could have been written directly into the if function below

#Checks the value of random_number. Where random_number
#is less than 0.5, 1 is added to y0
#otherwise 1 is subtracted from y0
if random.random() < 0.5: #random.random() replaces ramdon_number
    y0 += 1
else:
    y0 -=1

#above codeblock repeated for x0
if random.random() < 0.5: #random.random() replaces ramdon_number
    x0 += 1
else:
    x0 -=1
    
print(y0,x0)

#repeat step
if random.random() < 0.5: #random.random() replaces ramdon_number
    y0 += 1
else:
    y0 -=1

#above codeblock repeated for x0
if random.random() < 0.5: #random.random() replaces ramdon_number
    x0 += 1
else:
    x0 -=1
    
print(y0,x0)


#creates variables y0/x0
#and assigns ramdom start values between 0 and 99
y1 = random.randint(1,99) 
x1 = random.randint(1,99) 

#generates a ramdon number between 0 and 1 and
#makes it the value of varible random_number
#random_number = random.random() #this function could have been written directly into the if function below

#Checks the value of random_number. Where random_number
#is less than 0.5, 1 is added to y0
#otherwise 1 is subtracted from y0
if random.random() < 0.5: #random.random() replaces ramdon_number
    y1 += 1
else:
    y1 -=1

#above codeblock repeated for x0
if random.random() < 0.5: #random.random() replaces ramdon_number
    x1 += 1
else:
    x1 -=1
    
print(y0,x0)

#repeat step
if random.random() < 0.5: #random.random() replaces ramdon_number
    y1 += 1
else:
    y1 -=1

#above codeblock repeated for x0
if random.random() < 0.5: #random.random() replaces ramdon_number
    x1 += 1
else:
    x1 -=1
    
print(y0,x0, y1,x1)

#Calculate distance between xy0/xy1
distance = (((y0-y1)**2) + ((x0-x1)**2))**0.5
print(distance)