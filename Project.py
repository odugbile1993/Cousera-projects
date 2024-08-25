#Nested for loop ! 

print("Hello world!")

for n in range(0,11,2):
    print(n)

for number in range(2,7+1):
    print(number*3)

for x in range(2, -2, -1):
    print(x)

for left in range(7):
  for right in range(left, 7):
    print("[" + str(left) + "|" + str(right) + "]", end=" ")
  print()

teams = [ 'Dragons', 'Wolves', 'Pandas', 'Unicorns']
for home_team in teams:
  for away_team in teams:
    if home_team != away_team:
      print(home_team + " vs " + away_team)

teams = {'Chelsea', 'Barcelona', 'Wolves', 'R.madrid'}
for home_team in teams:
    for away_team in teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)

for i in range(0, 3):
    print("The next value is:", i)

greeting = 'Hello'
for char in greeting:
	print(char)

footbal_teams = {'Chelsea', 'Manchester city', 'Arsenal', 'Mancester united'}
for home_team in footbal_teams:
    for away_team in footbal_teams:
        if home_team != away_team:
            print(home_team + " vs " + away_team)

for x in range(2):
    print("This is the outer loop iteration number " + str(x))
    for y in range(3+1):
        print("Inner loop iteration number " + str(y))
    print("Exit inner loop")


for i in range(12, 37, 6):
    print(i)

for n in range(19):
    if n % 2 == 0:
        print(n)

for n in range(19):
    if n % 2 == 0:
        print(n)

for n in range(19):
    if n % 2 == 0:
        print(n)

for n in range(6,18,3):
  print(n*2)

# 12, 18, 24, 30, 36

for n in range(6,18,3):
  print(n+2)

for n in range(6,18+1,3):
  print(n*2)

for n in range(18+1):
  print(n**2)

for n in range(19):
    if n % 2 == 0:
        print(n)

# recursion

def factorial(n):
  if n < 2:
    return 1
  return n * factorial(n-1)

def factorial(n):
  print("Factorial called with " + str(n))
  if n < 2:
    print("Returning 1")
    return 1
  result = n * factorial(n-1)
  print("Returning " + str(result) + " for factorial of " + str(n))
  return result

# factorial(4)


# This function will accept an integer variable "end" and count by 10
# from 0 to the "end" value.
# def count_by_10(end):
#     # Initializeq the "count" variable as a string.
#     count = ""

#     # The range function parameters instruct Python to start the count  
#     # at 0 and stop at the variable given as the upper end of the range. 
#     # Since the value of the high end of a range is excluded by default,  
#     # you can make Python include the "end" value by adding +1 to it. 
#     # The third parameter tells Python to increment the count by 10.
#     for number in range(0,end+1,10):

#         # Although the variable "count" will hold a count of integers,  
#         # this example will be converted to a string using "str(number)" 
#         # in order to display the incremental count from 0 to the "end" 
#         # value on the same line with a space " " separating each 
#         # number.  
#         count += str(number) + " "
        
#     # The .strip() method will trim the final space " " from the end of 
#     # the string "count"  
#     return count.strip()



# This function uses a set of nested for loops with the range() function 
# to create a matrix of numbers. The upper range value in the range() 
# function should be included in the matrix. The matrix should consist 
# of a set of numbers that fill both rows and columns.
def matrix(initial_number, end_of_first_row):


    # It is an optional code style to assign the long variable names in the
    # function parameters to shorter variable names. 
    # n1 = initial_number 
    # n2 = end_of_first_row+1  # include the upper range value with +1

    # The first for loop will create the columns.
    # for column in range(n1, n2):

        # The nested for loop will create the rows.
        # for row in range(n1, n2):

            # To make the matrix of numbers easier to read, include a space
            # between each number in the rows until the loop reaches the 
            # end of the row. You can override the default behavior of the 
            # print() function (which inserts a new line character after 
            # the print command runs) by using the "end=" "" parameter 
            # inside the print() function.  
            #   print(column*row, end=" ")

        # The row ends when the upper range value is encountered within the 
        # nested for loop. The outer (column) for loop should insert a new line
        # to create the next row. Use the print() function new line default 
        # behavior with an empty print() function:
        print()


# Call the function with 2 integer parameters. 
# matrix(1, 4)
# # Should print:
# # 1 2 3 4 
# # 2 4 6 8 
# # 3 6 9 12 
# # 4 8 12 16 


# For this example, the outer for loop uses an end of range index of 
# 10. The value of index 10 will be 10-1, or 9.  
# for outer_loop in range(10):

#     # Using the "outer_loop" variable as the end of range for the  
#     # inner loop, means the end of range index will be 9. The value 
#     # of index 9 will be 9-1, or 8.
#     for inner_loop in range(outer_loop):

#         # The printed result is the value of "inner_loop". Since  
#         # there aren’t any calculations in this loop, there is a 
#         # simple shortcut for solving what the final value printed 
#         # by the "inner_loop" will be. The solution is to simply use 
#         # the value of the "inner_loop" index, which is 8.
#         print(inner_loop)


# def all_numbers(minimum, maximum):
#     return_string = ""  # Initializes variable as a string

    # Complete the for loop with a range that includes all 
    # numbers up to and including the "maximum" value.
    # for num in  # return return_string.strip()
# range(minimum, maximum + 1):

        # Complete the body of the loop by appending the number
        # followed by a space to the "return_string" variable.
        # return_string += str(num) + " "

    # This .strip command will remove the final " " space 
    # at the end of the "return_string".
   
# print(all_numbers(2,6))  # Should be 2 3 4 5 6
# print(all_numbers(3,10)) # Should be 3 4 5 6 7 8 9 10
# print(all_numbers(-1,1)) # Should be -1 0 1
# print(all_numbers(0,5))  # Should be 0 1 2 3 4 5
# print(all_numbers(0,0))  # Should be 0

# for count in range(1, 6):
#     print(count+1)


# for outer_loop in range(2, 6+1):
#     for inner_loop in range(outer_loop):
#         if inner_loop % 2 == 0:
#             print(inner_loop)

print("Hello World!")

name = "Manny"
number = len(name) * 3
print("Hello {}, your lucky number is {}".format(name, number))


name = "Manny"
print("Your lucky number is {number}, {name}.".format(name=name, number=len(name)*3))





