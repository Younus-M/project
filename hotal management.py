
def tamil_foods():
    tamilfoods=["dosha","parotta","biriyani","pongal","itli","kuska","kotuparotta"]
    your_order=(input("enter your order:"))
    dosha_amount=30
    parotta_amount=20
    biriyani_amount=100
    pongal_amount=30
    itli_amount=10
    kuska_amount=30
    kothuparotta_amount=50

    if your_order in tamilfoods:
        print(f"yes your {your_order} is available")

        how_many=int(input(f"how many {your_order} you want:"))

        if your_order=="dosha":
            total=dosha_amount*how_many
            print(f"your total bill is Rs.{total}")
        elif your_order=="parotta":
            total=parotta_amount*how_many
            print(f"your total bill is Rs.{total}")
        elif your_order=="biriyani":
            total=biriyani_amount*how_many
            print(f"your total bill is Rs.{total}")
        elif your_order=="pongal":
            total=pongal_amount*how_many
            print(f"your total bill is Rs.{total}")
        elif your_order=="itli":
            total=itli_amount*how_many
            print(f"your total bill is Rs.{total}")
        elif your_order=="kuska":
            total=kuska_amount*how_many
            print(f"your total bill is Rs.{total}")
        elif your_order=="kothuparotta":
            total=kothuparotta_amount*how_many
            print(f"your total bill is Rs.{total}")

    else:
        print(f"sorry your {your_order} is not avaliable")



def kerala_foods():
    
    keralafoods=["appam","karimeen","malabarparotta","fishmoilee","paladapayasam","chikencurry","puttu"]

    your_order=(input("enter your order:"))

    appam_amount=40
    karimeen_amount=100
    malabarparotta_amount=50
    fishmoilee_amount=100
    paladapayasam_amount=70
    chikencurry_amount=150
    puttu_amount=60

    if your_order in keralafoods:
        print(f"yes your {your_order} is available")

        how_many=int(input(f"how many {your_order} you want:"))

        if your_order=="appam":
            total=appam_amount*how_many
            print(f"your total bill is Rs.{total}")
        elif your_order=="karimeen":
            total=karimeen_amount*how_many
            print(f"your total bill is Rs.{total}")
        elif your_order=="malabarparotta":
            total=malabarparotta_amount*how_many
            print(f"your total bill is Rs.{total}")
        elif your_order=="fishmoilee":
            total=fishmoilee_amount*how_many
            print(f"your total bill is Rs.{total}")
        elif your_order=="paladapayasam":
            total=paladapayasam_amount*how_many
            print(f"your total bill is Rs.{total}")
        elif your_order=="chikencurry":
            total=chikencurry_amount*how_many
            print(f"your total bill is Rs.{total}")
        elif your_order=="puttu":
            total=puttu_amount*how_many
            print(f"your total bill is Rs.{total}")
    else:
        print(f"sorry your {your_order} is not avaliable")       

def chinese_foods():
    
    chinesefoods=["kadaichicken","butterchicken","chickenmasala","chickenafgani"]

    your_order=(input("enter your order:"))

    kadaichicken_amount=250
    butterchicken_amount=250
    chickenmasala_amount=250
    chickenafgani_amount=250

    if your_order in chinesefoods:
        print(f"yes your {your_order} is available")

        how_many=int(input(f"how many {your_order} you want:"))

        if your_order=="kadaichicken":
            total=kadaichicken_amount*how_many
            print(f"your total bill is Rs.{total}")
        elif your_order=="butterchicken":
            total=butterchicken_amount*how_many
            print(f"your total bill is Rs.{total}")
        elif your_order=="chickenmasala":
            total=chickenmasala_amount*how_many
            print(f"your total bill is Rs.{total}")
        elif your_order=="chickenafgani":
            total=chickenafgani_amount*how_many
            print(f"your total bill is Rs.{total}")

    else:
        print(f"sorry your {your_order} is not avaliable")

print("1- Tamil Foods       2- Kerala Foods       3- Chinese Foods")
cate= int(input("Enter Category You Want: \n"))
if cate==1:
    print("Welcome To Tamil Foods")
    tamil_foods()
elif cate ==2:
    print("Welcome to Kerala Foods")
    kerala_foods()
elif cate==3:
    print("Welcome TO Chinese Foods")
    chinese_foods()












