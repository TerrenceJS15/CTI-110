#CTI-110
#P2HW2
#Terrence Sharples
#11/16/2023

#Get grades from user
Module1= float(input("Enter grade for Module 1:"))
Module2= float(input("Enter grade for Module 2:"))
Module3= float(input("Enter grade for Module 3:"))
Module4= float(input("Enter grade for Module 4:"))
Module5= float(input("Enter grade for Module 5:"))
Module6= float(input("Enter grade for Module 6:"))

#Create a module empty list
mod_list=[]

#Add values to the list
mod_list.append(Module1)
mod_list.append(Module2)
mod_list.append(Module3)
mod_list.append(Module4)
mod_list.append(Module5)
mod_list.append(Module6)

#Print the list to ensure values are added
print(mod_list)

#Call methods on the list to get sum and product
max_grade = max(mod_list)
min_grade = min(mod_list)
sum_grade = sum(mod_list)
average_grade = sum_grade/len(mod_list)
#Output to user formatted with f-string
print(f"-----Results-----")
print(f"Lowest Grade: {min_grade:.1f}")
print(f"Highest Grade: {max_grade:.1f}")
print(f"Sum of Grades: {sum_grade:.1f}")
print(f"Average: {average_grade:.2f}")
