#xuexi
def calc(*numbers):
    sum = 0
    for n in numbers:
        sum = sum + n * n
    return sum

nums = [1, 2, 3]    
print(calc(nums[0], nums[1], nums[2]))
print(*nums)
	        
print()	        