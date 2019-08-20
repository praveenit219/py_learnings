#swap for every iteraion if number is greater than the other
#iterate until teh highest values becomes the last one
# do repeat until highest of every iteration reach last element


def sort(nums):
    for i in range(len(nums)-1,0,-1): #negative order from back to 
        for j in range(i):
            if nums[j] > nums[j+1]:
                temp = nums[j]
                nums[j] = nums[j+1]
                nums[j+1] = temp




nums = [5,3,8,6,7,2]
sort(nums)

print(nums)