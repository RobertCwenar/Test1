# Napisz dwie funkcje:
# calculate_bmi(weight_kg, height_cm)
# Wzór: waga / (wzrost_m ** 2)
# height_cm to centymetry - zamień na metry
# Zwróć float
# bmi_category(bmi)
# Zwróć: niedowaga, norma, nadwaga, otyłość
# Progi: <18.5, 18.5-24.9, 25.0-29.9, >=30.0
# run_cli() jest już gotowe - nie zmieniaj go.


def calculate_bmi(weight_kg, height_cm):
    height_m = height_cm / 100
    bmi = weight_kg / (height_m ** 2)
    return bmi

def bmi_category(bmi):
    if bmi < 18.5:
        return "niedowagę"
    elif 18.5 <= bmi <= 24.9:
        return "normę"
    elif 25.0 <= bmi <= 29.9:
        return "nadwagę"
    elif bmi >= 30.0:
        return "otyłość"
    
def run_cli():
    weight = float(input("Podaj swoją wagę w kg: "))
    height = float(input("Podaj swój wzrost w cm: "))
    
    bmi = calculate_bmi(weight, height)
    category = bmi_category(bmi)
    
    category = bmi_category(bmi)
    print(f"Twoje BMI wynosi: {bmi:.2f}, co oznacza: {category}")

if __name__ == "__main__":
    run_cli()


    