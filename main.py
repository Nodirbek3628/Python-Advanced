from Decorators import requers_login

# @chek_item
# def yigindi(nums):
#     return sum(nums)

# print(yigindi([1,2,2457]))


@requers_login
def show_profil():
    print("Your profil")


show_profil()