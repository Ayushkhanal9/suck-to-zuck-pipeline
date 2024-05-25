#A program that gives me 3 questions from my already solved leetcode set
#it also picks 2 questions from the leet code available question that I havent attempted for me to try. 
# This can prob be done using a csv or excel sheet of the problems in leet code and it will pick out problems that arent attempted
#can add what level of problem I am looking for later
import random

class RandProbGiv:
    def __init__(self) -> None:
        solved_prob=['Concatenation of Array','Maximum Number of Words Found in Sentence','Check if the Sentence is Pangram', 'Reverse String','Invert Binary Tree', 'Reverse Linked List','Baseball Game']
        choose_prob=[]
        print(solved_prob[0])
        #pick 3 problems
        while len(choose_prob)<3: #using for loop it would run out of 3 iterations so using while loop
            random_item=random.choice(solved_prob)
            if random_item not in choose_prob: #had if in before but this seemed shorter and easier to understand
                choose_prob.append(random_item)
        print(choose_prob)

RandProbGiv()