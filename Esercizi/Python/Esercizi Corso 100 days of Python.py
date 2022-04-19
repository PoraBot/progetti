print("Riga 1 \nRiga 2")
print("Ciao " + input("Come ti chiami?\n"))

#Write your code below this line 👇
nome = input("What is your name?")
lun = len(nome)
print(lun)

#Puoi selezionare il carattere singolo come se fosse un array
print("Ciaone"[2])
#Puoi mettere i _ nei int per separare e renderlo più leggibile, il sw li ignorerà
print(123_456)

num_char = len(input("Come ti chiami? "))
new_num_char = str(num_char)

print("Il tuo nome è lungo " + new_num_char +" caratteri.")

# Esercizio di sommare i numeri dei due caratteri in un numero di due caratteri

# 🚨 Don't change the code below 👇
two_digit_number = input("Type a two digit number: ")
# 🚨 Don't change the code above 👆

####################################
#Write your code below this line 👇

type(two_digit_number)
num_1 = int(two_digit_number[0])
num_2 = int(two_digit_number[1])

print(num_1 + num_2)

# Per elevare un numero puoi fare
print(3**3)

# Per arrotondare si usa una funzione, il valore dopo la virgola serve per dire quante cifre arrotondare
print(round(8 / 2, 2))

# Per ottenere invece un numero intero senza convertirlo da float ad int
print(8 // 3)

# += -= /= *= per eseguire le moltiplicazioni sul valore della variabile

#Esempio fstring

Punti = 0
Altezza = 1.2
StaiVincendo = True

print(f"Il tuo punteggio è {Punti}, la tua altezza è {Altezza} e stai vincendo {StaiVincendo}")

# Esercizio per calcolare quanti giorni, settimane e mesi mancano ad arrivare a 90 anni

# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

i_age = int(age)

days_max = 90 * 365
weeks_max = 90 * 52
months_max = 90 * 12 

days = days_max - (i_age * 365)
weeks = weeks_max - (i_age * 52)
months = months_max - (i_age * 12)



print(f"You have {days} days, {weeks} weeks, and {months} months left.")

# Esercizio Tip Calculator

#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

result = 0
print("Welcome to the Tip Calculator!")
bill = float(input("What was the total bill? $"))
tip = int(input("How much tip would you like to give? 10, 12, or 15? " ))
people = int(input("How many people to split the bill? "))

tip_on_bill = bill * (tip / 100)
result = round((tip_on_bill + bill) / people, 2)
#Tiene sempre due decimali dopo la virgola, se il secondo non è presente mostra 0
result_figo = "{:.2f}".format(result)

print(f"The total is $ {result_figo}")

# Esercizio check numero pari o dispari

# 🚨 Don't change the code below 👇
number = int(input("Which number do you want to check? "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

risultato = number % 2

if risultato > 0:
    print("This is an odd number.")
else:
    print("This is an even number.")

# BMI 2.0

# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight / (height ** 2)
rounded_bmi = round(bmi)

if bmi < 18.5:
    print(f"Your BMI is {rounded_bmi}, you are underweight")
elif bmi < 25:
    print(f"Your BMI is {rounded_bmi}, you have a normal weight")
elif bmi < 30:
    print(f"Your BMI is {rounded_bmi}, you are slightly overweight")
elif bmi < 35:
    print(f"Your BMI is {rounded_bmi}, you are obese")
else:
    print(f"Your BMI is {rounded_bmi}, you are clinically obese")


#Esercizio Love Score


# 🚨 Don't change the code below 👇
from math import comb


print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇


combo_name = name1+ name2
lower_combo_name= combo_name.lower()


find_t = lower_combo_name.count('t')
find_r = lower_combo_name.count('r')
find_u = lower_combo_name.count('u')
find_e = lower_combo_name.count('e')

true = find_t + find_r + find_u + find_e

find_l = lower_combo_name.count('l')
find_o = lower_combo_name.count('o')
find_v = lower_combo_name.count('v')
find_e = lower_combo_name.count('e')

love = find_l + find_o + find_v + find_e

love_score = str(true) + str(love)

print(love_score)

if (love_score < 10) or (love_score > 90):
    print(f"Your score is {love_score}, you go together like coke and mentos.")
elif (love_score >= 40) and (love_score <= 50):
    print(f"Your score is {love_score}, you are alright together.")
else:
    print(f"Your score is {love_score}.")
