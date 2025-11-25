def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")


def get_user_input():
    user_input = input()
    list_str = user_input.split(",")
    list_float = [float(x) for x in list_str]
    return list_float


def calc_average_temperature(list_of_temps):
    average = sum(list_of_temps) / len(list_of_temps)
    return average


def calc_min_max_temperature(list_of_temps):
    min_temp = min(list_of_temps)
    max_temp = max(list_of_temps)
    return [min_temp, max_temp]
