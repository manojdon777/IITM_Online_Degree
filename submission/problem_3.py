def main():
	ans=[]
	while True:
	    x = list(map(int, input().split()))
	    if not x:
	    	break
	    else:
	        ans.append(x)
	print('initial:  ',ans)
	x = len(ans) - 1
	total = 0
	while x:
		curr_row = 1
		for i in range(0,curr_row):
			left = i - 1
			right = i
			if left < 0 or left > curr_row -1:
			       left_ans = 0
			else:
			    left_ans = ans[curr_row - 1][left]

			if right > curr_row - 1:
			    right_ans = 0
			else:
			    right_ans = ans[curr_row - 1][right]
			ans[curr_row][i] = ans[curr_row][i] + max(left_ans, right_ans)
			total = max(total, ans[curr_row][i])
		curr_row += 1
		x = x - 1
		print('Modified: ',ans)
	return total
print(main())