import numpy as np

#create array of tuples of household incomes and percentiles
hhIncome = [
	(10, 14629),
	(20, 25600),
	(30, 37002),
	(40, 50000),
	(50, 63179),
	(60, 79542),
	(70, 100162),
	(80, 130000),
	(90, 184292),
]

hhIncomeArray = np.array(hhIncome)

print(f"dimensions of the array: {hhIncomeArray.ndim}")
print(f"number of elements in the array: {hhIncomeArray.size}")

for i in range(hhIncomeArray.shape[0]):
    percentile, income = hhIncomeArray[i]
    print(f"percentile: {percentile}, income: {income}")

    