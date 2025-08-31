from Decorators import chek_item

@chek_item
def yigindi(nums):
    return sum(nums)

print(yigindi([1,2,2457]))