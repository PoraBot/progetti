# 🚨 Don't change the code below 👇
year = int(input("Which year do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

even_year = year % 4
divisible_100 = year % 100
divisible_400 = year % 400

if even_year == 0:
    if divisible_100 == 0: 
        if divisible_400 == 0:
            print("Leap year.")
        else:
            print("Not leap year.")
    else:
        print("Leap year.")
else:
    print("Not leap year.")


