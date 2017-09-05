def main():
        lst = [2, 3, 5, 1, -4, 8, 0, -1]
        print(removeBelowAvg(lst))

def removeBelowAvg(lst):
	lstSum = 0
	for x in lst:
		lstSum += x
	lstLen = len(lst)
	lstAvg = lstSum / lstLen
	lstPlus = []
	for z in lst:
		if (z >= lstAvg):
			lstPlus.append(z)
	return lstPlus

main()


