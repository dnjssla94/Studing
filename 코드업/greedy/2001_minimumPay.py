
pastaPrices = list()
juicePrices = list()

pasta1 = int(input())
pastaPrices.append(pasta1)
pasta2 = int(input())
pastaPrices.append(pasta2)
pasta3 = int(input())
pastaPrices.append(pasta3)

juice1 = int(input())
juicePrices.append(juice1)
juice2 = int(input())
juicePrices.append(juice2)

pastaPrices.sort()
juicePrices.sort()

minimumCombination = 1.1*(pastaPrices[0]+juicePrices[0])

#print(type(minimumCombination))
print(format(minimumCombination,'.1f'))