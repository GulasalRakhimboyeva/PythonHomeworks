def convert_celcius_to_farangeit(celcius):
    return round(celcius*9/5 + 32, 2)

def convert_farangeit_to_celcius(farangeit):
    return round((farangeit-32)*5/9, 2)

farangeit=float(input('Enter farangeit temperature: '))

print(farangeit, 'degrees F =', convert_farangeit_to_celcius, "degrees C")