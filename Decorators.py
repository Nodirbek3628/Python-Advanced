def chek_item(func):
    def wrapper(nums: list):

        if any([type(item) not in (int,float) for item in nums]):
            raise Exception("faqat son kiriting")
        
        result = func(nums)

        return result
    return wrapper

