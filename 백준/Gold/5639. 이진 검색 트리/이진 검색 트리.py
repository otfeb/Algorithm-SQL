import sys
input = sys.stdin.readline
# recursion error 방지
sys.setrecursionlimit(10**9)

arr = []

while True:
	try:
		a = int(input())
		arr.append(a)
	except:
		break
	
def binary_tree(arr):
	if len(arr) == 0:
		return
	
	root = arr[0]
	tempL, tempR = [], []
	
	for i in range(len(arr)):
		if arr[i] > root:
			tempL = arr[1:i]
			tempR = arr[i:]
			break
	else:
		tempL = arr[1:]
	
	binary_tree(tempL)
	binary_tree(tempR)
	print(root)
	
binary_tree(arr)