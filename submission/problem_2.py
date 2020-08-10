#9791563725
def getSelectAsMinister():
	"""
			Python program to free the country from the dictator.
			Submitted by Manoj Dongare - manojdon777@gmail.com 
	"""
	testcases = int(input())
	for test in range(testcases):
		n, k = map(int, input().split())
		position = 1
		while n//k > 0:
			n = n//k
			position = position * k
		print(position)
getSelectAsMinister()