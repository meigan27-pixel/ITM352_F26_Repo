#

import csv
csvFileName = "whole_foods_employee_sample.csv"
salaries = []

#read csv file and store salaries in a list
with open(csvFileName, mode ='r') as csvFile:
    reader = csv.reader(csvFile)
    headers = next(reader)  # Skip the header row
    print(f"headers: {headers}")
    salaryIndex = headers.index("Annual_Salary")
    for row in reader:
        salary = float(row[salaryIndex])
        salaries.append(salary)

    #compute salary stats
    aveSalary = sum(salaries) / len(salaries)
    minSalary = min(salaries)
    maxSalary = max(salaries)

    print(f"Average Salary: ${aveSalary:.2f}")
    print(f"Minimum Salary: ${minSalary:.2f}")
    print(f"Maximum Salary: ${maxSalary:.2f}")