#A program that gives me 3 questions from my already solved leetcode set
#it also picks 2 questions from the leet code available question that I havent attempted for me to try. 
# This can prob be done using a csv or excel sheet of the problems in leet code and it will pick out problems that arent attempted
#can add what level of problem I am looking for later
import random
import tkinter
from tkinter import ttk

# import sv_ttk

class RandProbGiv:
    def __init__(self) -> None:
        solved_prob=['Two Sum','Palindrome Number', 'Roman to Integer','Longest Common Prefix','Valid Parentheses','Merge Two Sorted Lists','Remove Duplicates from Sorted Array','Remove Element',
                     'Find the Index of the First Occurrence in a String','Search Insert Position','Length of Last Word','Plus One','Sqrt(x)','Climbing Stairs','Remove Duplicates from Sorted List'
                     ,'Merge Sorted Array','Binary Tree Inorder Traversal','Pascals Triangle','Best Time to Buy and Sell Stock','Valid Palindrome','Single Number','Linked List Cycle','Binary Tree Pre-post-in order Traversal',
                     'Intersection of Two Linked Lists','Two Sum II - Input Array Is Sorted','Majority Element','Excel Sheet Column Number','Reverse Linked List','Contains Duplicate','Contains Duplicate II',
                     'Invert Binary Tree','Valid Anagram','Missing Number','Move Zeroes','Reverse String','Reverse Vowels of a String','Guess Number Higher or Lower','Is Subsequence','Max Consecutive Ones',
                     'Maximum Average Subarray I','Baseball Game','Binary Search','Monotonic Array','Unique Email Addresses','Squares of a Sorted Array','Max Consecutive Ones III','Replace Elements with Greatest Element on Right Side'
                     'Check if the Sentence Is Pangram','Substrings of Size Three with Distinct Charac','Concatenation of Array','Maximum Number of Words Found in Sentences']
        choose_prob=[]
        print(solved_prob[0])

        #pick 3 problems
        while len(choose_prob)<3: #using for loop it would run out of 3 iterations so using while loop
            random_item=random.choice(solved_prob)
            if random_item not in choose_prob: #had if in before but this seemed shorter and easier to understand
                choose_prob.append(random_item)
        print(choose_prob)
RandProbGiv()       
# root=tkinter.Tk()
# label1=ttk.Label(root,"Press below to pick 3 problems")
# label1.grid(row=2,column=2)

# sv_ttk.set_theme("dark")
# RandProbGiv()
# root.mainloop()
