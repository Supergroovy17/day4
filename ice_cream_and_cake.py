#Advanced Looping Techniques (BONUS)
#Objective: Advance your looping skills by exploring more complex list manipulations. You will learn to selectively loop through parts of a list,use list comprehensions for concise code, and generate numerical lists with Python's range and len function.
#Task 1: Ice Cream BO-GO Your local ice cream shop is running a buy-one-get-one on scoops today, create a list of your
 #five favorite scoops. 
#Using a nested for loop print out all the combinations you can make
#Task 2: Double UP! If you land on a the same flavor print "Double <that flavor>" instead of repeating that flavor
#Task 3: No Repeats!  Make it to where you never print the same combinations of flavors, If your printed "Vanilla Chocolate" 
#you shouldn't see "Chocolate Vanilla" . Hint: this can be done by gradually slicing off previous flavors from the inner loops list.

#-- Topping Combination

ice_cream = ['vanilla', 'chocolate', 'mint', 'butterscotch', 'coffee']

for ice_cream_1 in ice_cream:
    for ice_cream_2 in ice_cream:
        if ice_cream_1 == ice_cream_2:
            print('Double up', ice_cream_1)
        else:
            print(ice_cream_1, ice_cream_2)
            

            
            
            
            #List slicing list[start:stop] : returns a sublist from the start index to the stop index
#default for start and stop are the beginning and end of the list
#the stop index is non-inclusive, meaning the item at the stop index wont be included in the slice

key_lime_pie = ['slice1','slice2','slice3','slice4']

my_slice = key_lime_pie[0:1]
print(my_slice)
big_slice = key_lime_pie[1:3] #item at stop index is not included
print(big_slice)
last_slice = key_lime_pie[3:] #sliceing to the end, can use -1
print(last_slice)
