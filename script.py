import random

#magic 8-ball
name = "Mihai"
question = "Ploua maine?"
answer = ""
magic_answer = ""
random_number = random.randint(1, 9)
#print(random_number)

if random_number == 1:
  answer = "Yes - definitely"
elif random_number == 2:
  answer = "It is decidedly so"
elif random_number == 3:
  answer = "Without a doubt"
elif random_number == 4:
  answer = "Reply hazy, try again"
elif random_number == 5:
  answer = "Ask again later"
elif random_number == 6:
  answer = "Better not tell you now"
elif random_number == 7:
  answer = "My sources say no"
elif random_number == 8:
  answer = "Outlook not so good"
elif random_number == 9:
  answer = "Very doubtful"
else:
  answer = "Error"

magic_answer = "Magic 8-Ball's answer: " + answer
if name == "":
  print("Question "+ question)
elif question == "":
  print("Please ask a question")
else:
  print(name + " asks: " + question )
  print("Magic 8-Ball's answer: " + answer)

  #cost transport ground sau drona
  weight = 41.5
  grnd_cost = 0
  drone_cost = 0
  grnd_cost_shipping = 0
  drone_cost_shipping = 0
  flat_charge = 20
  premium_grnd_shipping = 125.00

  # Ground Shipping
  if weight <= 2:
    grnd_cost = 1.50
  elif weight > 2 and weight <= 6:
    grnd_cost = 3.0
  elif weight > 6 and weight <= 10:
    grnd_cost = 4.0
  else:
    grnd_cost = 4.75
  print("Cost per Lbs grnd: " + str(grnd_cost))
  grnd_cost_shipping = weight * grnd_cost + flat_charge
  print("Cost transport: " + str(grnd_cost_shipping))
  # print(premium_grnd_shipping)

  # Drone shipping
  if weight <= 2:
    drone_cost = 4.50
  elif weight > 2 and weight <= 6:
    drone_cost = 9.0
  elif weight > 6 and weight <= 10:
    drone_cost = 12.0
  else:
    drone_cost = 14.25
  print("Cost per Lbs drone: " + str(drone_cost))
  drone_cost_shipping = weight * drone_cost
  print("Cost transport: " + str(drone_cost_shipping))

#tipul anului leap sau non leap
  def is_leap(year):
    leap = False

    # Write your logic here
    if (year % 4 == 0 and not year % 100 == 0) or year % 400 == 0:
      leap = True

    return leap

year = int(input())


last_semester_gradebook = [["politics", 80], ["latin", 96], ["dance", 97], ["architecture", 65]]

# Your code below:

subjects = ["physics", "calculus", "poetry", "history"]
grades = [98, 97,85,88]
gradebook = [["physics" ,98], ["calculus" ,	97], ["poetry" ,	85], ["history" ,88]]
print(gradebook)

gradebook.append(["computer science", 100])
gradebook.append(["visual arts", 93])
print(gradebook)

grade_viz = gradebook[-1][-1] + 5
gradebook[-1][-1] = grade_viz
print(gradebook)

grade_poetry = gradebook[2][1]
print(grade_poetry)
gradebook[2].remove(grade_poetry)
print(gradebook)

gradebook[2].append("Pass")
print(gradebook)
full_gradebook = last_semester_gradebook + gradebook
print(full_gradebook)


# Pizzerie
toppings = [
    "pepperoni",
    "pineapple",
    "cheese",
    "sausage",
    "olives",
    "anchovies",
    "mushrooms"
]
prices =[
    2,
    6,
    1,
    3,
    2,
    7,
    2
]
num_two_dollar_slices = prices.count(2)
#print(num_two_dollar_slices)
num_pizzas = len(toppings)
#print(num_pizzas)

#print("We sell " + str(num_pizzas) +" different kinds of pizza!")

pizza_and_prices = [[2,	"pepperoni"], [6,	"pineapple"], [1, "cheese"],[3,	"sausage"], [2,	"olives"], [7,	"anchovies"], [2,	"mushrooms"]]
#print(pizza_and_prices)
pizza_and_prices.sort()

cheapest_pizza = pizza_and_prices[0]
priciest_pizza = pizza_and_prices[-1]
pizza_and_prices.pop()
pizza_and_prices.insert(0, [2.5, "peppers"])
pizza_and_prices.sort()
print(pizza_and_prices)
three_cheapest = pizza_and_prices[:3]
print(three_cheapest)
