# def chek_item(func):
#     def wrapper(nums: list):

#         if any([type(item) not in (int,float) for item in nums]):
#             raise Exception("faqat son kiriting")
        
#         result = func(nums)

#         return result
#     return wrapper




def requers_login(func):
    user_name = "ali"
    user_password = "1"

    def wrapper():
        username = input("username: ")
        password = input("password: ")

        if username != user_name or user_password!= password :
            print("Login qilishingz shart")
        else:
            func()

    return wrapper

