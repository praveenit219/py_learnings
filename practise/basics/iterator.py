
nums = [7,8,9,5]

print(nums)
print(nums[0])
print(nums[3])

#print(nums[8]) #IndexError: list index out of range

for i in nums:
    print(i)

it = iter(nums) #converting list of nums to iterator
print(it) #prints object of it

print(it.__next__()) #this __next__ return the cursor pointer value by iterator
print(it.__next__()) 
print(it.__next__()) 
print(it.__next__()) 
#print(it.__next__()) # it fails with StopIteration, becz iter reached the limit of list
#print(next(it))

#create your own iterator

class TopTen:
    def __init__(self):
        self.num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.num <= 10:
            val = self.num
            self.num += 1
            return val
        else:
            raise StopIteration # this is to stop iterator even after 10

values = TopTen()
print('custom iterator')
print(values.__next__())
print(next(values))
print('for loop iterator')
for i in values:
    print(i)