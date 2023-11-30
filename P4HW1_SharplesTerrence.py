#CTI-110
#P4HW1
#Terrence Sharples
#11/30/2023

#Create a empty list
mod_list=[]

#Get number of grades from user
num_grades = int(input("How many grades do you want to put"))
for item in range(num_grades):
    grade = int(input(f"Enter your grade for module {item +1}"))
    while grade < 0 or grade > 100:
        print("You entered a invalid grade")
        grade = int(input(f"Enter your grade for module {item +1}"))
#Add grade to the list        
    mod_list.append(grade)         

#Create a module empty list

#Add values to the list


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
