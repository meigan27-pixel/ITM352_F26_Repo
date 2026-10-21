import csv
import os

#check if the file exists and is readable
if not os.path.exists("whole_foods_employee_sample.csv"):
    print("Error: File 'whole_foods_employee_sample.csv' does not exist.")
    exit(1)

if not os.access("whole_foods_employee_sample.csv", os.R_OK):
    print("Error: File 'whole_foods_employee_sample.csv' is not readable.")
    exit(1)
else:
    fileSize = os.path.getsize("whole_foods_employee_sample.csv")
    print(f"File 'whole_foods_employee_sample.csv' exists and is readable. Size: {fileSize} bytes.")


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

    print(f"Average Salary: {round(aveSalary, 2)}")
    print(f"Minimum Salary: {round(minSalary, 2)}")
    print(f"Maximum Salary: {round(maxSalary, 2)}")