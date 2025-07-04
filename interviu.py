#
# numbers = [0, 2, 4, 7, 8, 9, 10, 15, 13]
#
# def even_numbers(numbers_list):
#     """
#
#     """
#     even_numbers = []
#     # for number in numbers_list:
#     #     if number % 2 == 0:
#     #         even_numbers.append(number)
#
#     # for index in range(len(numbers_list)):
#     #     print(index)
#     #     if index % 2 == 0:
#     #         even_numbers.append(numbers_list[index])
#
#     # return [even_numbers for even_numbers in numbers_list if even_numbers % 2 == 0]
#     return [numbers_list[index]  for index in range(len(numbers_list)) if index % 2 == 0]
#



# import random
#
# def simulate_api_call():
#     return random.choice([True, False])
#
# def response_verification(max_fail_tries):
#     """
#
#     """
#     conter_fail = 0
#     while conter_fail < max_fail_tries:
#         print(conter_fail)
#         api_response = simulate_api_call()
#         print(api_response)
#         if api_response == False:
#             conter_fail += 1
#             continue
#         return "Success"
#     return "Failure"
#
#
# if __name__ == "__main__":
#     print(response_verification(1))


# def input_nubers_sum(numbers_list):
#     return sum(numbers_list)
#
#
# def input_number():
#     user_input = 1
#     numbers_list = []
#     while user_input != 0:
#         try:
#             user_input = float(input("Input a number "))
#             numbers_list.append(user_input)
#         except ValueError1 as ex:
#             print("Warning: User input was not integer, the number will not be added to list")
#             print(ex)
#
#     return input_nubers_sum(numbers_list)
#
#
# if __name__ == "__main__":
#     print(input_number())




# if __name__ == "__main__":
#     text = "Ana are Mere, si L,,.,.,aura, are Pere"
#     print(text)
#     # result = ['Ana', 'Mere', 'Laura', 'Pere']
#     lista_cuvinte_mari = []
#     for caracter in text:
#         if not caracter.isalpha() and not caracter.isspace():
#             text = text.replace(caracter,"")
#     print(text)
#     text_split = text.split(" ")
#     print(text_split)
#     for cuvant in text_split:
#         if cuvant.istitle():
#             lista_cuvinte_mari.append(cuvant)
#     x = [cuvant for cuvant in text_split if cuvant.istitle()]
#
#     print(x)


    hairstyles = ["bouffant", "pixie", "dreadlocks", "crew", "bowl", "bob", "mohawk", "flattop"]

    prices = [30, 25, 40, 20, 20, 35, 50, 35]

    last_week = [2, 3, 5, 8, 4, 4, 6, 2]

    total_price = sum(prices)
    print(total_price)
    average_price = total_price / len(prices)
    print("Average Haircut Price: " + str(average_price))

    new_prices = [new_prices - 5 for new_prices in prices]
    print(new_prices)

    total_revenue = 0
    for i in range(0, len(hairstyles)):
      total_revenue += prices[i] * last_week[i]
    print("Total Revenue: " + str(total_revenue))

    average_daily_revenue = total_revenue / 7
    # cuts_under_30 = [cuts_under_30 for index in range(len(hairstyles)) if prices[i] < 30 ]
    cuts_under_30 =[]
    for index in range(len(new_prices)):
      if new_prices[index] < 30:
        cuts_under_30.append(hairstyles[index])
    print(cuts_under_30)




    # Uncomment this when you reach the "Use the Force" section
    train_mass = 22680
    train_acceleration = 10
    train_distance = 100
    bomb_mass = 1


    # Write your code below:
    def f_to_c(f_temp):
      return (f_temp - 32) * 5/9


    def c_to_f(c_temp):
      return (c_temp * 5/9) + 32

    c0_in_fahrenheit = c_to_f(0)

    def get_force(mass, acceleration):
      return mass * acceleration


    train_force = get_force(train_mass, train_acceleration)
    print(train_force)

    print("The GE train supplies", train_force, " Newtons of force.")

    def get_energy(mass, c = 3*10**8):
      return mass * c
    bomb_energy = get_energy(bomb_mass)
    print("A 1kg bomb supplies", bomb_energy, " Joules.")

    def get_work(mass, acceleration, distance):
      return get_force(mass, acceleration) * distance
    train_work = get_work(train_mass, train_acceleration, train_distance)
    print("The GE train does", train_work, "Joules of work over", train_distance,  " meters.")

if __name__ == "__main__":

