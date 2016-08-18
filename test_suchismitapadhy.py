#!/usr/bin/env python3
# Note:
#   Please save this as test_GitHubusername.py
#       (replace GitHubusername w/ your GitHub username)
#   Do not edit lines with comments that start with: "# Last line in"
###############################################################################
# Imports  # there will only be two imports added here.
import math
import os
import sys


###############################################################################
# Write f01 that prints "Hello World!" and calls f02. (three lines)
def f01():
    print("Hello World!")
    f02()


###############################################################################
# Write f02 that sets the variables x, y, and z equal to the words
# necessary to have the f03 print "i love python!" (five lines)
def f02():
    x = "i"
    y = "love"
    z = "python"


    f03(x, y, z)  # Last line in f2()


###############################################################################
# Finish f03 (replace the ????).
def f03(*words):
    truth = " ".join(words)  # This is broken.
    truth_emphasized = truth + "!"
    print(truth_emphasized)
    f04(truth)  # Last line in f03()


###############################################################################
# Write f04 that prints truth backwards (edit one line only)
# Ex. f4("Littlest Bear") prints "raeB tselttiL"
def f04(string):
    print(string[::-1])
    f05(string)  # Last line in f04()


###############################################################################
# Write f05 that for each char in a word passed as a parameter, prints that
# word on a new line, and for each consecutive print, prints it indented by one
# more char. (possibly a few lines)
# Ex. f05("Info")
# Info
#  Info
#   Info
#    Info
def f05(word):
    for i in range(len(word)):
        print(i * " " + word)
    f06("South Hall", "Python Rocks!")  # Last line in f05()


###############################################################################
# Write f06 that takes two strings:
# (1) prints: "'string' is longer than 'string' by x chars"
#   replace string and string w/ the actual strings, replace x w/ proper value
# (2) prints: "'string' has only xx.xx% the number of chars of 'string'"
#   replace string and string w/ the actual strings
#   replace xx.xx w/ proper value
# (several lines)
# Ex. f06("short_string", "longer_string")
# 'longer_string' is longer than 'short_string' by 1 chars
# 'short_string' has only 92.31% the number of chars of longer_string
def f06(string1, string2):
    size_string1 = len(string1)
    size_string2 = len(string2)
    diff = size_string1 - size_string2
    if diff >= 0:
        print("{} is longer than {} by {} chars".format(string1, string2, diff))
        percent = (float(size_string2) / size_string1)
        print('{} has only {}% of the number of chars of {}'.format(string1, percent, string2))

    else:
        print("{} is longer than {} by {} chars".format(string2, string1, abs(diff)))
        percent = (float(size_string1) / size_string2)
        print('{} has only {}% of the number of chars of {}'.format(string1,percent,string2))

    various_solutions()  # Last line in f06()


###############################################################################
# Write f07, f08, f09, f10 to find the sum of all the multiples of 3 or 5
# below 500 (starting at 1)
# f07 should demonstrate a while loop, returning the sum
# f08 should demonstrate a for loop, returning the sum
# f09 should demonstrate list comprehension, returning the sum
# f10 should demonstrate recursion, returning the sum
# check_solution_vals() will call the functions and check solutions.
# only edit the parameters in the function calls (if you want to)
###############################################################################
def various_solutions():
    """ This checks solutions. ONLY EDIT PARAMETERS PASSED TO FUNCTIONS. """
    while_ = f07()
    for_ = f08()
    list_comprehension = f09()
    recursion = f10(500)
    # DO NOT EDIT BELOW THIS LINE
    vals = [while_, for_, list_comprehension, recursion]
    for val in vals:
        print(val)
    if len(set(vals)) == 1:
        print("Not sure if it's right, but all your solutions agree!")
    else:
        print("Oops...")
    f11_args = [1, "2", 3.0, '4', 5.0, 6]  # Last lines in various_solutions()
    for arg in f11_args:
        f11(arg)
    f12()


###############################################################################
def f07():
    num = 1
    total = 0
    while num < 500:
        if num % 3 == 0 or num % 5 == 0:
            total += num
        num += 1
    return total


###############################################################################
def f08():
    total = 0
    for num in range(1, 500):
        if num % 3 == 0 or num % 5 == 0:
            total += num
    return total


###############################################################################
def f09():
    total = sum([num for num in range(500) if num % 3 == 0 or num % 5 == 0])
    return total


###############################################################################
def f10(num):
    if num <= 1:
        return 0

    num -= 1
    if num % 3 == 0 or num % 5 == 0:
        return num + f10(num)
    return f10(num)


###############################################################################
# Write f11() to take arguments, printing them as floats if they started as
# strings, integers if they started as floats, and as the value 0 if they
# started as ints.
def f11(args):
    if type(args) == "<class 'float'>":
        print(int(args))

    elif type(args) == "<class 'int'>":
        print(0)

    elif type(args) == "<class 'string'>":
        print(float(args))


###############################################################################
# Write f12() to ask for raw_input from the user. Change the input to a float.
# Create log_file.txt to log the input that cannot be changed to a float.
#   - write one faulty input per line
# Print, as a list, all converted input.
# Proceed to the last line, calling f13, when the user types done or "done"
# Ex. log_file.txt
#   TEST
#   123abc
#   python rules
# Ex. printing
#   [1.0, 1.3, 2.443]
def f12():

    user_list = []
    while True:
        user_num = (input("Enter a number: "))
        if user_num=="done":
            break
        try:
            user_num = float(user_num)
            user_list.append(user_num)

        except:
            with open('log_file.txt', 'w') as fh:
                fh.write(str(user_num) + "\n")
    print(user_list)
    f13()  # Last line in f12()


###############################################################################
# Fix the error in f13:
def f13():
    for each in "string":
        print(each)
    f14()  # Last line in f13()


###############################################################################
# Write f14 to print the path and filename of this script. DO NOT HARD CODE.
# You may nee to add two import statements.
# Please do so at the top of the file.
# Ex. /Users/dsg/pbc_2016/test/test_danielsgriffin.py
def f14():
    script_name = sys.argv[0]
    abs_path = os.path.abspath(script_name)
    print(script_name)
    print(abs_path)
    f15()  # Last line in f14()


###############################################################################
# Write f15 to print the goal below. Do not print any strings.
# Do not take more than nine lines to code.
# Goal:
# [[0], [], [], [], [], [], [], [], [], []]
# [[], [0], [], [], [], [], [], [], [], []]
# [[], [], [0], [], [], [], [], [], [], []]
# [[], [], [], [0], [], [], [], [], [], []]
# [[], [], [], [], [0], [], [], [], [], []]
# [[], [], [], [], [], [0], [], [], [], []]
# [[], [], [], [], [], [], [0], [], [], []]
# [[], [], [], [], [], [], [], [0], [], []]
# [[], [], [], [], [], [], [], [], [0], []]
# [[], [], [], [], [], [], [], [], [], [0]]
def f15():
    l = []
    for i in range(10):
        for j in range(10):
            if i == j:
                l.append([0])
            else:
                l.append([])
            print()

    f16([1, 2, 3], [4, 5, 6])  # Last line in f15()


###############################################################################
# Write f16() that takes two lists and prints a list with the nth elements of
# each list sharing a tuple.
# Ex.
# [1,2,3] and [4,5,6] would produce [(1, 4), (2, 5), (3, 6)]
def f16(list1, list2):
    [(list1[i], list2[i]) for i in range(len(list1))]
    f17()  # Last line in f16()


###############################################################################
# Write f17() to take the 2nd line from few_words.txt, and print a list
# with the index of the word in that line and the word, sharing tuples.
# Ex. [(0, 'To'), (1, 'be'), (2, 'or'), (3, 'not'), (4, 'to'), (5, 'be')]
def f17():
    second_tuples=[]
    with open("few_words.txt", "r") as fh:
        first_line = fh.readline()
        second_line = fh.readline().split()
        for index in range(len(second_line)):
            second_tuples.append((index, second_line[index]))
        print(second_tuples)

    # Be sure to save the list that you print to list_
    list_ = second_tuples  # Change to your list variable name
    f18(list_)  # Last line in f17()


# Write f18 to take the list above and create a dictionary, use the words as
# keys and the numbers as values. Some keys will be replaced b/c duplicates.
# Print the dictionary.
# Call the dictionary in f19()
def f18(list_):
    word_list = {}
    for item in list_:
        word_list[item[1]] = item[0]
    print(word_list)
    d = word_list
    f19(d)  # Last line in f18()


# Write f19 to update that dictionary by changing the values by adding the
# number of chars in the word to the current value (if the resulting value
# would be even), otherwise change the value to the ascii number for the last
# char in the word. Print the new dictionary.
def f19(d):
    for k, v in d.items():
        if v + len(k) % 2 == 0:
            d[k] += len(k)
        else:
            last_char = k[-1]
            d[k] = ord(last_char)

    f22()  # Last line in f19()


# Write f21() to find if a word is capitalized. Return True/False.
# Ex.
# f21("Yes") = True, f21("NO") = False,
# f21("nope") = False, f21("nADA") = False
def f21(word):
    return word == word.title()


# Write f22() to use f21() to (1) print a list of all capitalized words in
# few_words.txt sorted by length. Then (2) remove all duplicate words.
# (3) If our favorite word (Python) is in the list, move it to the front of the
# list (because it deserves to be there). (4) Make Python all uppercase.
# (5) If Magic is in the list. Delete it.
# (6) Add an exlamation mark to Python.
# (7) To show how special Python is to us, put all the other words in a nested
# list so they don't contaminate Python.
# (8) Print this latest version (the second print in this function)
# Ex. second print:
# ['PYTHON!', ['Other1', 'Other_2']]
def f22():
    capitalized_list = []
    with open("few_words.txt", "r") as fh:
        lines = fh.readlines()
        for line in lines:
            for word in line.split():
                if f21(word):
                    capitalized_list.append(word)

    capitalized_list = sorted(capitalized_list, key=len)
    print(capitalized_list)
    capital_set = set()
    unique_list = []
    for word in capitalized_list:
        if word not in capital_set:
            unique_list.append(word)
    capitalized_list = unique_list

    for index in range(len(capitalized_list)):
        if capitalized_list[index] == "Python":
            capitalized_list[index] = capitalized_list[index].upper() + "!"
            capitalized_list[0], capitalized_list[index] = capitalized_list[index], capitalized_list[0]
    
    capitalized_list=[x for x in capitalized_list if x != "Magic"]
    capitalized_list = [capitalized_list[0], capitalized_list[1:]]
    print
    capitalized_list
    # Last lines in f22()
    f23([["o", "o", "x"], ["x", "o", "x"], ["o", "", "x"]])
    f23([["o", "", "o"], ["x", "o", "x"], ["o", "x", "x"]])
    f23([["o", "o", "x"], ["x", "x", "x"], ["o", "", "o"]])


# Write f23() that takes a list of three lists of len 3, and says who won in
# tic-tac-toe (you can expect all moves to have been legal, made turn-by-turn)
# you can expect there is a winner. Print the x or o and the type of win:
# "col1", "col2", "row3", "falling_back_diag", "falling_front_diag"
# Ex. of rows (not a finished game)
# row1 = ["o", "", ""]
# row2 = ["", "x", ""]
# row3 = ["", "", ""]
# Ex. of print: x, col2
def f23(lists_):
    for i in range(3):
        if lists_[i].count('o') == 3:
            print("{}, row{}".format('o', i + 1))
            return
        elif lists_[i].count('x') == 3:
            print("{}, row{}".format('x', i + 1))
            return
    for i in range(3):
        for j in range(3):
            count_x = 0
            count_o = 0
            if lists_[j][i] == "x":
                count_x += 1
            elif lists_[j][i] == "o":
                count_o += 1
        if count_o == 3:
            print("{}, col{}".format('o', i + 1))
            return
        elif count_x == 3:
            print("{}, col{}".format('x', i + 1))
            return
    count_x = 0
    count_o = 0
    for i in range(3):
        for j in range(3):

            if i == j:
                if lists_[j][i] == "x":
                    count_x += 1
                elif lists_[j][i] == "o":
                    count_o += 1


    if count_o == 3:
        print("{}, maindiag{}".format('o', i + 1))
        return
    elif count_x == 3:
        print("{}, maindiag{}".format('x', i + 1))
        return
    count_x = 0
    count_o = 0

    for i in range(3):
        for j in range(3):

            if i + j == len(lists_):
                if lists_[j][i] == "x":
                    count_x += 1
                elif lists_[j][i] == "o":
                    count_o += 1

    if count_o == 3:
        print("{}, col{}".format('o', i + 1))
        return
    elif count_x == 3:
        print("{}, col{}".format('x', i + 1))
        return


# Write main() that calls f01, then prints the The Zen of Python, by Tim Peters.
# (three lines)
def main():
    f01()


# Write the boilerplate code. (two lines, plus empty line at end)
if __name__ == "__main__":
    main()



