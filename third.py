# once  = {'a': 1, 'b': 2}
# twice = {'a': 2, 'b': 4}
# for key in once:
#   print "Once: %s" % once[key]
#   print "Twice: %s" % twice[key]
# ========================================================================
# prices = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3,
# }
# stock = {
#     "banana": 6,
#     "apple": 0,
#     "orange": 32,
#     "pear": 15,
# }
# total = 0
# for key in prices:
#     print key
#     print "price: %s" % prices[key]
#     print "stock: %s" % stock[key]
#     total += prices[key] * stock[key]
# print total
# ========================================================================
# shopping_list = ["banana", "orange", "apple"]
# stock = {
#     "banana": 6,
#     "apple": 0,
#     "orange": 32,
#     "pear": 15
# }
# prices = {
#     "banana": 4,
#     "apple": 2,
#     "orange": 1.5,
#     "pear": 3
# }
# def compute_bill(food):
#     total = 0
#     for x in food:
#         if stock[x] > 0:
#             total += prices[x]
#             stock[x] -= 1         #removes 1 from stock
#     return total
# print compute_bill(shopping_list)
# ========================================================================
# lloyd = {
#   "name": "Lloyd",
#   "homework": [90.0, 97.0, 75.0, 92.0],
#   "quizzes": [88.0, 40.0, 94.0],
#   "tests": [75.0, 90.0]
# }
# alice = {
#   "name": "Alice",
#   "homework": [100.0, 92.0, 98.0, 100.0],
#   "quizzes": [82.0, 83.0, 91.0],
#   "tests": [89.0, 97.0]
# }
# tyler = {
#   "name": "Tyler",
#   "homework": [0.0, 87.0, 75.0, 22.0],
#   "quizzes": [0.0, 75.0, 78.0],
#   "tests": [100.0, 100.0]
# }
# def average(numbers):
#   total = float(sum(numbers))
#   return total / len(numbers)
# def get_average(student):
#   homework = average(student['homework'])
#   quizzes = average(student['quizzes'])
#   tests = average(student['tests'])
#   return 0.1 * homework + 0.3 * quizzes + 0.6 * tests
# def get_letter_grade(score):
#   if score >= 90:
#     return "A"
#   elif score >= 80:
#     return "B"
#   elif score >= 70:
#     return "C"
#   elif score >= 60:
#     return "D"
#   else:
#     return "F"
#
# print get_letter_grade(get_average(lloyd))
#
# def get_class_average(class_list):
#   results = []
#   for x in class_list:
#     results.append(get_average(x))
#   return average(results)
#
# print get_class_average([lloyd, alice, tyler])
# print get_letter_grade(get_class_average([lloyd, alice, tyler]))
# ========================================================================
# n = [3, 5, 7]
# def double_list(x):
# 	# type: (object) -> object
# 	for i in range(0, len(x)):
#   	    x[i] = x[i] * 2
#         return x
# print double_list(n)
# ========================================================================
# n = [3, 5, 7]
# def total(numbers):  # first method
#   result = 0
#   for x in numbers:
#     result += x
#   return result
# n = [3, 5, 7]
# def total(numbers):     #second method
#   result = 0
#   for x in range(len(numbers)):
#     result += numbers[x]
#   return result
# print total(n)
# ========================================================================
# n = [[1, 2, 3], [4, 5, 6, 7, 8, 9]]  #multidimansional print
# def flatten(lists):
#   results = []
#   for i in lists:     # numbers is
#     for ii in i:
#       results.append(ii)
#   return results
# print flatten(n)
# ========================================================================
# from random import randint      #battleship game
# board = []
# for x in range(5):              #makes field 5 x 5
#   board.append(["O"] * 5)       #appends 5 lists into one parent list board
# def print_board(board):
#   for row in board:             #board is a list of 5 lists
#     print " ".join(row)         #prints field 5 x 5
# print_board(board)
# def random_row(board):
#   return randint(0, len(board) - 1)
# def random_col(board):
#   return randint(0, len(board[0]) - 1)
# ship_row = random_row(board)
# ship_col = random_col(board)
# #print ship_row
# #print ship_col
# # Everything from here on should go in your for loop!
# # Be sure to indent four spaces!
# for turn in range(4):
#   print "Turn ", turn + 1
#   guess_row = int(raw_input("Guess Row: "))
#   guess_col = int(raw_input("Guess Col: "))
#   if guess_row == ship_row and guess_col == ship_col:
#     print "Congratulations! You sunk my battleship!"
#     break
#   else:
#     if (guess_row < 0 or guess_row > 4) or (guess_col < 0 or guess_col > 4):
#       print "Oops, that's not even in the ocean."
#     elif(board[guess_row][guess_col] == "X"):
#       print "You guessed that one already."
#     else:
#       print "You missed my battleship!"
#       board[guess_row][guess_col] = "X"
#       if turn == 3:
#         print "Game Over"
#   	  # Print (turn + 1) here!
#   print_board(board)
# ========================================================================
# choice = raw_input('Enjoying the course? (y/n)')      #while loop example
# while choice != 'y' or choice != 'n':  # Fill in the condition (before the colon)
#   if choice == 'y' or choice == 'n':
#     break
#   else:
#   	choice = raw_input("Sorry, I didn't catch that. Enter again: ")
# ========================================================================
# import random
# print "Lucky Numbers! 3 numbers will be generated."
# print "If one of them is a '5', you lose!"
# count = 0
# while count < 3:              #while/else example
#   num = random.randint(1, 6)
#   print num
#   if num == 5:
#     print "Sorry, you lose!"
#     break
#   count += 1
# else:                     # else will execute is no break, if break, so else is not executed
#   print "You win!"
# ========================================================================
# from random import randint
# # Generates a number from 1 through 10 inclusive
# random_number = randint(1, 10)
# guesses_left = 3                          # guess game
# # Start your game!
# while guesses_left > 0:                   #while/else example
#   guess = int(raw_input("Your guess: "))
#   if guess == random_number:
#     print "You win!"
#     break
#   guesses_left -= 1
# else:
#   print "You lose."
# ========================================================================
# hobbies = []
# for hobby in range(3):
#     hobby = raw_input("List a Hobby: ")
#     hobbies.append(hobby)
# print hobbies
# ========================================================================
# word = "Marble"
# for char in word:
#   print char,       #prints all in one line because of ","
# ========================================================================
# d = {'a': 'apple', 'b': 'berry', 'c': 'cherry'}    #dictionaries
# print d['apple']
# for key in d:
#   print key, d[key]
# ========================================================================
# choices = ['pizza', 'pasta', 'salad', 'nachos']     #enumerate function
# print 'Your choices are:'
# for any_index, any_name in enumerate(choices):
#   print any_index + 1, any_name
# ========================================================================
# list_a = [3, 9, 17, 15, 19]                           # zip function
# list_b = [2, 4, 8, 10, 30, 40, 50, 60, 70, 80, 90]
# for a, b in zip(list_a, list_b):
#   print max(a, b)
# ========================================================================
# print (1234%10)
# print (1234.534//10)
# print len(str(1234))
# # ========================================================================
# def digit_sum(n):       # sum of all digits
#   my_str = str(n)
#   y = 0
#   for x in my_str:
#     y += int(x)
#   return y
# print digit_sum(1234)
# ========================================================================
# def reverse(text):          #reverse string
#   new_text = ""
#   for i, ii in enumerate(text):
#     y = ""
#     y = text[len(text)-(i+1)]
#     new_text = new_text + y
#   return new_text
# print reverse("abcd")
# ========================================================================
# def anti_vowel(text):           #removes vowels from the string
#     message = ""
#     vowels = "aeiou"            #vowels
#     for i in text:
#         if not(i.lower() in vowels):
#             message = message + i
#     return message
# print anti_vowel("serKUFIuoagbh")
# ========================================================================
# def check_in(x, i):         #checks if the string "i" exists in string "x"
#     if i in x:
#         return True
#     else:
#         return False
# print check_in("324564", "2")
# print check_in("Any string", "a")
# ========================================================================
# def censor(text, word):     #replace word in text by asterisks
#     if word in text:
#         text = text.replace(word, "*" * len(word))
#     return text
# ========================================================================
# def purify(numbers):        #removes odd numbers
#     new_list = []
#     for i in numbers:
#         if i % 2 == 0:
#             new_list.append(i)
#     return new_list
# print purify([4,5,5,4])
# ========================================================================
# def product(listofintegers):    #product of list
#     total = 1
#     for each in listofintegers:
#             total *= each
#     return total
# print product([2,3,4,5])
# ========================================================================
# def remove_duplicates(lst):     #removes duplicates from the list
#     result = []
#     for item in lst:
#         if item not in result:
#             result.append(item)
#     return result
# print remove_duplicates([1,3,1,2,1,2])
# ========================================================================
# def median(list_num):           #returns median of the list
#   s = sorted(list_num)          #The median is the middle number in a sorted sequence of numbers
#   if len(s)%2 == 0:
#     return (s[len(s)/2] + s[(len(s)/2) - 1]) / 2.0
#   else:
#     return s[(len(s)-1)/2]
# ========================================================================
# grades = [100, 100, 90, 40, 80, 100, 85, 70, 90, 65, 90, 85, 50.5]    #statistics
# def print_grades(grades_input):
#     for grade in grades_input:
#         print grade
# print_grades(grades)
# def grades_sum(scores):
#     total = 0
#     for score in scores:
#         total += score
#     return total
# print grades_sum(grades)
# def grades_average(grades_input):
#     sum_of_grades = grades_sum(grades_input)
#     average = sum_of_grades / float(len(grades_input))
#     return average
# print grades_average(grades)
# def grades_variance(scores):                        #variance
#     average = 0
#     average = grades_average(scores)
#     variance = 0
#     for score in scores:
#         variance += (average - score) ** 2
#     return variance / len(scores)
# print grades_variance(grades)
# def grades_std_deviation(variance):                 #standard deviation
#     return variance ** 0.5
# variance = grades_variance(grades)
# print grades_std_deviation(variance)
# ========================================================================
# l = [1, 4, 9, 16, 25, 36, 49, 64, 81, 100]          #list slicing
# print l[2:9:2]
# my_list = range(1, 11) # List of numbers 1 - 10
# print my_list[::2]
# ========================================================================
# doubles_by_3 = [x * 2 for x in range(1, 10) if (x * 2) % 3 == 0]     #list comprehension
# print doubles_by_3
# ========================================================================
# squares = [x ** 2 for x in range(1, 11)]              #list comprehension and lambda
# print filter(lambda x: x >= 30 and x <= 70, squares)
# ========================================================================
# garbled = "IXXX aXXmX aXXXnXoXXXXXtXhXeXXXXrX sXXXXeXcXXXrXeXt mXXeXsXXXsXaXXXXXXgXeX!XX"
# message = filter(lambda x: x != "X", garbled)
# print message
# ========================================================================
# class Car(object):
#   condition = "new"
#   def __init__(self, model, color, mpg):
#     self.model = model
#     self.color = color
#     self.mpg   = mpg
#   def display_car(self):
#     return "This is a %s %s %s with %d MPG" % (self.condition, self.color, self.model, self.mpg)
#   def drive_car(self):
#     self.condition = "used"     #change the initial class variable
#
# class ElectricCar(Car):             #inheritance
#   def __init__(self, model, color, mpg, battery_type):
#     self.model = model
#     self.color = color
#     self.mpg   = mpg
#     self.battery_type = battery_type
#   def drive_car(self):              #overriding
#     self.condition = "like new"
#
# my_car = Car("DeLorean", "silver", 88)
# my_ecar = ElectricCar("Mazda", "grey", 90, "molten salt")
#
# print my_car.display_car()
# print my_ecar.display_car()
# print my_car.condition
# print my_ecar.condition
# my_car.drive_car()              #change the initial class variable from new to used
# my_ecar.drive_car()
# print my_car.display_car()
# print my_ecar.display_car()
# print my_car.condition
# print my_ecar.condition
# ========================================================================
class Point3D(object):
  def __init__(self, x, y, z):
    self.x = x
    self.y = y
    self.z = z
  def __repr__(self):
    return "(%d, %d, %d)" % (self.x, self.y, self.z)

my_point = Point3D(x=1, y=2, z=3)
print my_point
# ========================================================================

# ========================================================================

# ========================================================================

# ========================================================================

# ========================================================================

# ========================================================================

# ========================================================================

# ========================================================================