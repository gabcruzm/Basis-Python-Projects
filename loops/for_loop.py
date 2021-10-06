#Print inefficiently numbers from 1 to 1000
# print(1)
# print(2)
# print(3)
# .....
# print(1000)

#While Loop
# counter = 1 #Define counter variable - assign the value 1
# print(counter) 
# while counter < 1000: #While counter is less than 1000, the loop is executed
#     # counter = counter + 1 #When we do this, the variable increase in the number we put after =
#     counter += 1 #This is exactly the same as above
#     print(counter)

# a = range(1000)
# print(a) #When we print a, it will show the range: range(0, 1000)
#Now, we need to convert the range into a list. The same as we convert a string to number or we convert decimals to integers numbers, we can convert a range to a list.
#To make a list we do:
#a = list(range(1000)) 
# print(a) The numbers from 0 to 999 are printed in the console. The RANGE reaches until the previous number.
#For Loop
# for counter in range(1001): #For the counter in the range between 0 to 1001, the variable counter in the loop will take the range values.
#     print(counter)

for i in range(10): 
    print(11 * i)