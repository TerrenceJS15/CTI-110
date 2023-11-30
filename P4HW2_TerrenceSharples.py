#CTI-110
#P3HW2-Salary
#TJ Sjarples
#11/30/2023
#Use if/else to determine an employees pay

#Create variables to holf totals paid to employees
num_em = 0
total_reg = 0
total_ot = 0
total_gross = 0

emp_name = input("Enter Employee Name or type Done to quit:")
#Loop to control adding employess
while emp_name != "Done":
    num_em += 1
    emp_hours = int(input("Enter Employee hours: "))
    emp_pay = float(input("Enter the Employee's pay rate: "))

    #Calculations
    if emp_hours > 40:
        ot_hours = emp_hours - 40
        reg_hours = 40

    #This represents if emp_hours is 40 or less
    else:
        ot_hours = 0
        reg_hours = emp_hours

    #Calculate Pay
    ot_pay = (emp_pay * 1.5) * ot_hours
    total_ot += ot_pay
    
    reg_pay = emp_pay * reg_hours
    total_reg += reg_pay
    
    gross_pay = ot_pay + reg_pay
    total_gross += gross_pay

    print(f"Employee Name: {emp_name}")
    print(f"Regular Hours: {reg_hours}")
    print(f"OT hours: {ot_hours}")
    print(f"OT pay: {ot_pay}")
    print(f"Gross Pay: {gross_pay}")
    print()
    emp_name = input("Enter Employee Name or type Done to quit:")
    
#This code executes atfer look breaks    
print("Done adding employees")
print()
print(f"Total number of employees: {num_em}")
print(f"Total regular pay to employees: {total_reg}")
print(f"Total OT pay to employees: {total_ot}")
print(f"Total gross pay to employees: {total_gross}")
