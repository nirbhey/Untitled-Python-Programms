import statistics as sts

varList = [1, 2, 3, 9, 10, 5, 4, 2, 3, 6, 7]

x = sts.mean(varList)
print(x,' = mean\n')

x = sts.median(varList)
print(x,' = median\n')

x = sts.stdev(varList)
print(x,' = standard deviation\n')

x = sts.variance(varList)
print(x,' = variance\n')
