nums = []

with open ("C:/Users/Артём/Desktop/НТ Performance/numbers.txt", "r") as file:
    for line in file:
        num = line.strip()
        nums.append(int(num))
print(nums)


nums.sort()
print(nums)
mean = nums[len(nums) // 2]
print(mean)
step = sum(abs(num - mean) for num in nums)
print(step)