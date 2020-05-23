squire_of_sum = sum(list(range(1,101)))
sum_of_squires = []
for x in range(1,101):
	sum_of_squires.append(x**2)
answer = squire_of_sum**2 - sum(sum_of_squires)
print(str(answer))





