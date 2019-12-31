import statistics

varList = [1, 2, 3, 9, 10, 5, 4, 2, 3, 6, 7]

x = statistics.mean(varList)
print(x,' = mean\n')

x = statistics.median(varList)
print(x,' = median\n')

x = statistics.stdev(varList)
print(x,' = standard deviation\n')

x = statistics.variance(varList)
print(x,' = variance\n')