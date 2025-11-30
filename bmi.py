def calculate_bmi():
    weight = 50
    height = 1.85
    bmi = weight/(height*height)

    if bmi < 18.5:
        print("Under Weight")
        return -1

    elif 18.5 <= bmi <= 25.0:
        print("Normal Weight")
        return 0

    elif bmi>25.0:
        print("Over weight")
        return 1
    
print(calculate_bmi())