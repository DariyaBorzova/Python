n = int(input("Введите количество кустов: "))
berr = list()
for i in range(n):
    x = int(input("Введите количество ягод на кусте: "))
    berr.append(x)
berr_count = list()
for i in range(len(berr) - 1):
    berr_count.append(berr[i - 1] + berr[i] + berr[i + 1])
berr_count.append(berr[-2] + berr[-1] + berr[0])
print(max(berr_count))
