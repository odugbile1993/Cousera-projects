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

price = 7.5
with_tax = price * 1.09
print(price, with_tax)
print("Base price: ${:.2f}. With Tax: ${:.2f}".format(price, with_tax))

def to_celsius(x):
  return (x-32)*5/9

for x in range(0,101,10):
  print("{:>3} F | {:>6.2f} C".format(x, to_celsius(x)))
  

# This function accepts a given string and checks each character of 
# the string to see if it is a letter or not. If the character is a
# letter, that letter is added to the end of the string variable
# "forwards" and to the beginning of the string variable "backwards".
def mirrored_string(my_string):

    # Two variables are initialized as string data types using empty 
    # quotes. The variable "forwards" will hold the "my_string"
    # minus any character that is not a letter. The "backwards" 
    # variable will hold the same letters as "forwards", but in  
    # in reverse order.
    forwards = ""
    backwards = ""

    # The for loop iterates through each character of the "my_string"
    for character in my_string:

        # The if-statement checks if the character is not a space.
        if character.isalpha():

            # If True, the body of the loop adds the character to the
            # to the end of "forwards" and to the front of
            # "backwards". 
            forwards += character
            backwards = character + backwards

        # If False (meaning the character is not a letter), no action
        # is needed. This coding approach results prevents any 
        # non-alphabetical characters from being written to the
        # "forwards" and "backwards" variables. The for loop will 
        # restart until all characters in "my_string" have been
        # processed.
        
    # The final if-statement compares the "forwards" and "backwards"
    # strings to see if the letters are the same both forwards and
    # backwards. Since Python is case sensitive, the two strings will 
    # need to be converted to use the same case for this comparison. 
    if forwards.lower() == backwards.lower():
        return True
    return False
 
print(mirrored_string("12 Noon")) # Should be True
print(mirrored_string("Was it a car or cat I saw")) # Should be False
print(mirrored_string("'eve, Madam Eve")) # Should be True

# This function converts measurement equivalents. Output is formatted 
# as, "x ounces equals y pounds", with y limited to 2 decimal places. 
def convert_weight(ounces):

    # Conversion formula: 1 pound = 16 ounces
    pounds = ounces/16 
    
    # The result is composed using the .format() method. There are two
    # placeholders in the string: the first is for the "ounces" 
    # variable and the second is for the "pounds" variable. The second
    # placeholder formats the float result of the conversion 
    # calculation to be limited to 2 decimal places.
    result = "{} ounces equals {:.2f} pounds".format(ounces,pounds)
    return result


print(convert_weight(12)) # Should be: 12 ounces equals 0.75 pounds
print(convert_weight(50.5)) # Should be: 50.5 ounces equals 3.16 pounds
print(convert_weight(16)) # Should be: 16 ounces equals 1.00 pounds

# This function generates a username using the first 3 letters of a
# user’s last name plus their birth year. 
def username(last_name, birth_year):
    
    # The .format() method will use the first 3 letters at index 
    # positions [0,1,2] of the "last_name" variable for the first
    # {} placeholder. The second {} placeholder concatenates the user’s
    #  "birth_year" to that string to form a new string username.
    return("{}{}".format(last_name[0:3],birth_year))


print(username("Ivanov", "1985")) 
# Should display "Iva1985" 
print(username("Rodríguez", "2000")) 
# Should display "Rod2000" 
print(username("Deng", "1991")) 
# Should display "Den1991"


# This function checks a given schedule entry for an old date and, if 
# found, the function replaces it with a new date. 
def replace_date(schedule, old_date, new_date):

    # Check if the given "old_date" appears at the end of the given 
    # string variable "schedule". 
    if schedule.endswith(old_date):

        # If True, the body of the if-block will run. The variable "p" is
        # used to hold the slicing index position. The len() function
        # is used to measure the length of the string "old_date".
        p = len(old_date)

        # The "new_schedule" string holds the updated string with the 
        # old date replaced by the new date. The schedule[:-p] part of 
        # the code trims the "old_date" substring from "schedule" 
        # starting at the final index position (or right-side) counting
        # towards the left the same number of index positions as 
        # calculated from len(old_date). Then, the code schedule[-p:]
        # starts the indexing position at the slot where the first
        # character of the "old_date" used to be positioned. The 
        # .replace(old_date, new_date) code inserts the "new_date" into
        # the position where the "old_date" used to exist.  
        new_schedule = schedule[:-p] + schedule[-p:].replace(old_date, new_date)

        # Returns the schedule with the new date.
        return new_schedule
        
    # If the schedule does not end with the old date, then return the
    # original sentence without any modifications.
    return schedule
 
 
print(replace_date("Last year’s annual report will be released in March 2023", "2023", "2024")) 
# Should display "Last year’s annual report will be released in March 2024"
print(replace_date("In April, the CEO will hold a conference", "April", "May")) 
# Should display "In April, the CEO will hold a conference"
print(replace_date("The convention is scheduled for October", "October", "June")) 
# Should display "The convention is scheduled for June"

def convert_distance(miles):
    km = miles * 1.6 
    result = "{} miles equals {} km".format(miles, km)
    return result


print(convert_distance(12))  # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11))  # Should be: 11 miles equals 17.6 km

def nametag(first_name, last_name):
    return "{} {}.".format(first_name, last_name[0])


print(nametag("Jane", "Smith")) 
# Should display "Jane S." 
print(nametag("Francesco", "Rinaldi")) 
# Should display "Francesco R." 
print(nametag("Jean-Luc", "Grand-Pierre")) 
# Should display "Jean-Luc G." 

def replace_ending(sentence, old, new):
    # Check if the old substring is at the end of the sentence 
    if sentence.endswith(old):
        # Using i as the slicing index, combine the part
        # of the sentence up to the matched string at the 
        # end with the new string
        i = len(sentence) - len(old)
        new_sentence = sentence[:i] + new
        return new_sentence

    # Return the original sentence if there is no match 
    return sentence

print(replace_ending("It's raining cats and cats", "cats", "dogs")) 
# Should display "It's raining cats and dogs"
print(replace_ending("She sells seashells by the seashore", "seashells", "donuts")) 
# Should display "She sells seashells by the seashore"
print(replace_ending("The weather is nice in May", "may", "april")) 
# Should display "The weather is nice in May"
print(replace_ending("The weather is nice in May", "May", "April")) 
# Should display "The weather is nice in April"

def is_palindrome(input_string):
    # Two variables are initialized as string data types using empty 
    # quotes: "reverse_string" to hold the "input_string" in reverse
    # order and "new_string" to hold the "input_string" minus the 
    # spaces between words, if any are found.
    new_string = ""
    reverse_string = ""

    # Complete the for loop to iterate through each letter of the
    # "input_string"
    for letter in input_string:

        # The if-statement checks if the "letter" is not a space.
        if letter != " ":

            # If True, add the "letter" to the end of "new_string" and
            # to the front of "reverse_string". If False (if a space
            # is detected), no action is needed. Exit the if-block.
            new_string += letter
            reverse_string = letter + reverse_string

    # Complete the if-statement to compare the "new_string" to the
    # "reverse_string". Remember that Python is case-sensitive when
    # creating the string comparison code. 
    if new_string.lower() == reverse_string.lower():

        # If True, the "input_string" contains a palindrome.
        return True
	
    # Otherwise, return False.
    return False


print(is_palindrome("Never Odd or Even")) # Should be True
print(is_palindrome("abc")) # Should be False
print(is_palindrome("kayak")) # Should be True

def convert_distance(miles):
    km = miles * 1.6 
    result = "{} miles equals {:.1f} km".format(miles, km)
    return result


print(convert_distance(12))  # Should be: 12 miles equals 19.2 km
print(convert_distance(5.5)) # Should be: 5.5 miles equals 8.8 km
print(convert_distance(11))  # Should be: 11 miles equals 17.6 km


# List

x = ["Now", "we", "are", "cooking!"]
type(x)
print(x)
["Now", "we", "are", "cooking!"]
len(x)

print(x[0])
print(x[1])
print(x[2])
print(x[3])

fruits = ["pineappple", "Banana", "Apple", "Melo"]
fruits.append("kiwi")
print(fruits)
fruits.insert(0, "Orange")
print(fruits)
fruits.insert(25, "Peach")
print(fruits)
# to remove items from the list
fruits.remove("Melo")
print(fruits)

# To add new list
fruits[2] = "strawberry"
print(fruits)
fruits[5] = "juice"
print(fruits)

# tuple
def convert_seconds (seconds):
    hours = seconds // 3600
    minutes = (seconds - hours * 3600) // 60
    remaining_seconds = seconds - hours * 3600 - minutes * 60
    return hours, minutes, remaining_seconds
result = convert_seconds(5000)
print(result)

# iterating over lists and tuples
animals = ["Lion", "Zebra", "Dolphin", "Monkey"]
chars = 0
for animal in animals:
    chars += len(animal)
    
print("Total characters: {}, Average length: {}". format(chars, chars/len(animals)))

winners = ["Ashley", "Dylan", "Reese"]
for index,  person in enumerate(winners):
    print("{} - {}". format(index + 1, person))

def full_emails(people):
    result = []
    for email, name in people:  # Missing colon
        result.append("{} <{}>".format(name, email))  # Improper space before the dot and formatting
    return result
print(full_emails([("drolalekan.ayodele@gmail.com", "Ayodele Odugbile"), ("udumary1993@gmail.com", "Olalekan Ayodele")]))

# List comprehension
multiples = []
for x in range (1, 11):
    multiples.append(x*7)
    print(multiples)

languages = ['python', 'perl', 'ruby', 'go', 'java', 'c']
lengths = [len(language) for language in languages]
print(lengths)

z = [x for x in range (0, 101) if x % 3 ==0]
print(x)

# This block of code changes the year on a list of dates.
# The "years" list is given with existing elements. 
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]

# The variable "updated_years" is initialized as a list data type 
# using empty square brackets []. This list will hold the new list
# with the updated years. 
updated_years = []
# The for loop checks each "year" element in the list "years".
for year in years:
    # The if-statement checks if the "year" element ends with the 
    # substring "2023". 
    if year.endswith("2023"):
        # If True, then a temporary variable "new" will hold the 
        # modified "year" element where the "2023" substring is 
        # replaced with the substring "2024".
        new = year.replace("2023","2024")
        # Then, the list "updated_years" is appended with the changed
        # element held in the temporary variable "new".
        updated_years.append(new)
    # If False, the original "year" element will be appended to the 
    # the "updated_years" list unchanged.
    else:
        updated_years.append(year)
        print(updated_years) 
     # Should print ["January 2024", "May 2025", "April 2024", "August 2024", "September 2025", "December 2024"]
     
     # This list comprehension creates a list of squared numbers (n*n). It
    # accepts two integer variables through the function’s parameters.
    
def squares(start, end):
    # The list comprehension calculates the square of a variable integer 
    # "n", where "n" ranges from the "start" to "end" variables inclusively.
    # To be inclusive in a range(), add +1 to the end of range variable.
    return [n*n for n in range(start,end+1)] 

print(squares(2, 3))  # Should print [4, 9]
print(squares(1, 5))  # Should print [1, 4, 9, 16, 25]
print(squares(0, 10)) # Should print [0, 1, 4, 9, 16, 25, 36, 49, 64, 81, 100]

# This block of code also changes the year on a list of dates using a
# different approach than demonstrated in Skill Group 1. By using a 
# list comprehension, you can see how it is possible to refactor the
# code to a shorter, more efficient code block. 

# The "years" list is given with existing elements.
years = ["January 2023", "May 2025", "April 2023", "August 2024", "September 2025", "December 2023"]

# The list comprehension below creates a new list "updated_years" to
# hold the command to replace the "2023" substring of the "year"
# element with the substring "2024". This action will be executed if
# the last 4 indices of the "year" string is equal to the substring
# "2023". If false (else), the "year" element will be included in the
# new list "updated_years" unchanged.
updated_years = [year.replace("2023","2024") if year[-4:] == "2023" else year for year in years]

print(updated_years) 
# Should print ["January 2024", "May 2025", "April 2024", "August 2024", "September 2025", "December 2024"]

# This function splits a given string into a list of elements. Then, it
# modifies each element by moving the first character to the end of the 
# element and adds a dash between the element and the moved character. 
# For example, the element "2two" will be changed to "two-2". Finally,
# the function converts the list back to a string, and returns the
# new string.
def change_string(given_string):

    # Initialize "new_string" as a string data type by using empty quotes.`
    new_string = ""

    # Split the "given_string" into a "new_list", with each "element"
    # holding an individual word from the string.
    new_list = given_string.split()

    # The for loop iterates over each "element" in the "new_list".
    for element in new_list:
        # Convert the list into a "new_string" by using the assignment
        # operator += to concatenate the following items: 
        # + Each list "element" (starting at index position [1:]), 
        # + a dash "-", 
        # + append the first character of the "element" (using the index 
        # [0]) to the end of the "element", and finally,
        # + a space " " to separate each "element" in the "new_string".
        new_string += element[1:] + "-" + element[0] + " "

    # Return the list that has been converted back into a string.
    return new_string

print(change_string("1one 2two 3three 4four 5five")) # Should print "one-1 two-2 three-3 four-4 five-5"  
 
 
# Dictionary 
file_counts = {"jpg":10, "txt":14, "csv":2, "py":23}
print(file_counts)

# updating and deleting file in dic 
del file_counts["jpg"]
print(file_counts)

file_counts ["txt"] = 100
print(file_counts)

# iterating over the content dictionary

file_count = {"jpg":10, "txt":14, "csv":2, "py":2}
for extension in file_count:
    print(extension)
    
    
file_count = {"jpg":10, "txt":14, "csv":2, "py":2}   
for ext, amount in file_count.items():
 print("There are {} files with the . {} extension". format(amount, ext))
for value in file_count.values():
    print(value)
    
def count_letters(text):
    result = {}
    for letter in text:
        if letter not in result:
            result[letter] = 0
            result[letter] +=1
            return result
        count_letters("aaaaa")
        count_letters("tenant")
        count_letters("a long string with a lot of letters")
        

# Define the dictionary first
myDictionary = {'apple': 3, 'orange': 5, 'banana': 7}

key = 'banana'
if key in myDictionary:
    print(f"The value of {key} is {myDictionary[key]}")
else:
    print(f"{key} is not found in the dictionary")






  


















