#2. Nested Loops
#Objective: The aim of this assignment is to practice using nested loops in Python. You will correct a nested loop 
#code snippet, simulate a mood tracker, and generate a multiplication table.
#Task 1: Meal Planner Simulate a meal planner that picks a random meal from a meal list for breakfast lunch and dinner
# for each day of the week. Use nested loops to implement this: the outer 
#loop should iterate over the days, and the inner loop should iterate over the meals of the day. 
#For each time, randomly select a meal from a predefined list and print it. 
#Output: ..."Tuesday for Breakfast I'm having Yogurt" "Tuesday for Lunch I'm having Chicken" 
#"Tuesday for Dinner I'm having Pizza" "Wednesday for Breakfast I'm having Tacos" ...


import random
planner =['Breakfast!','Lunch!','Dinner!']# INNERLOOP
days = ['MONDAY','TUESDAY','WEDNESDAY','THURSDAY','FRIDAY','SATURDAY','SUNDAY'] #OUTERLOOP
meal = [['yogurt'],['chicken'],['pizza'],['tacos']]


for day in range(len(days)):
    print(days[day])
    for plan in range(len(planner)):
        
        print('for',planner[plan])
        (meal)
        random.shuffle(meal)
        print('This is what we put in our gut!')
        for meals in meal[0:1]:
           print(meals)


