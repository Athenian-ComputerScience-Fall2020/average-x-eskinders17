# Collaborators (including web sites where you got help: (enter none if you didn't need help)
#

#def avg(user_list):
n = int(input("Enter how many numbers you wanted to be averaged: "))
a = []
for i in range(0,n):
    num = int(input("Enter a number: "))
    a.append(num)
avg = sum(a)/n
print("Average of the numbers is",round(avg,2))
#   return average


#if __name__ == '__main__':
    # test your fucntion with this print statement before writing the input loop
    #print(avg([x, y, z]))    # Put the values you want to test in for x,y and z

    # Now, comment out the print statement and work on the code below
    # Remember to indent in this section
    #user_list = [] # start with an empty list
    # Write a loop to allow the user to input the values to be averaged
