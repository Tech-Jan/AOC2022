with open ("caloriecoutn") as f:
   caloriecount = f.read()

caloriecount_list = caloriecount.split("\n")

sum_calories_person = 0
sum_calories_max = 0
person_calories = []
for letter in caloriecount_list:
    if letter !="":
        sum_calories_person += int(letter)
    if sum_calories_person > sum_calories_max:
        sum_calories_max = sum_calories_person
    if letter == "":
        person_calories.append(sum_calories_person)
        sum_calories_person = 0


print(f"this is sum {sum_calories_max}")

person_calories.sort(reverse=True)

max3_persons = 0
for i in range(3):
    max3_persons += person_calories[i]

print(f"max3persons caloriessum = {max3_persons}")
