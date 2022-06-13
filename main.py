# random number chosen 
computer_result = False

import random
# User has number in mind - between 0 and 100 

# Computer guesses
# create dictionary with numbers
first = list(range(0,101))
second = list(range(0,101))
number_dict = dict(zip(first, second))
del first
del second

while computer_result == False:
    guess = (random.choice(list(number_dict.values())))
    user_answer = input(f"Is {guess} your number? Tell me if it's 'too high', 'too low', 'my number' ")
    if user_answer == "too high" or user_answer == 'high':
        # remove from guessed number, till end of dict (x, :)
        # by creating list, finding guessed number, slicing list till the end
        list1 = list(number_dict.keys())
        for element in list1:
            if element == guess:
                list1_index = list1.index(element)
                new_list1 = list1[:list1_index]
                new_list2 = new_list1
                number_dict = dict(zip(new_list1,new_list2))
                break
    elif user_answer == "too low" or user_answer == 'low':
        #remove from beginning to dict to end number
        # by creating list, finding guessed number, slicing list from the beginning
        list1 = list(number_dict.keys())
        for element in list1:
            if element == guess :
                list1_index = list1.index(element)
                new_list1 = list1[list1_index:]
                new_list2 = new_list1
                number_dict = dict(zip(new_list1,new_list2))
                break
    else: 
        computer_result = True
        the_list = list(number_dict.values())
        results_list = (' '.join(map(str, the_list)))
        print(f"I win! I guessed your number! It was {guess}")