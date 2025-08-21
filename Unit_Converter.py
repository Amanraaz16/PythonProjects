def km_to_miles(km):
    return km * 0.621371

def miles_to_km(miles):
    return miles / 0.621371

def c_to_f(celsius):
    return (celsius * 9/5) + 32

def f_to_c(fahrenheit):
    return (fahrenheit - 32) * 5/9

def m_to_ft(meters):
    return meters * 3.28084

def ft_to_m(feet):
    return feet / 3.28084

def kg_to_lb(kg):
    return kg * 2.20462

def lb_to_kg(lb):
    return lb / 2.20462

def l_to_gal(liters):
    return liters * 0.264172

def gal_to_l(gallons):
    return gallons / 0.264172


while True:
    print("\n🌍 Unit Converter")
    print("1. Kilometers to Miles")
    print("2. Miles to Kilometers")
    print("3. Celsius to Fahrenheit")
    print("4. Fahrenheit to Celsius")
    print("5. Meters to Feet")
    print("6. Feet to Meters")
    print("7. Kilograms to Pounds")
    print("8. Pounds to Kilograms")
    print("9. Liters to Gallons")
    print("10. Gallons to Liters")
    print("11. Exit")

    choice = input("Choose conversion (1-11): ")

    try:
        if choice == '1':
            km = float(input("Enter kilometers: "))
            print(f"{km} km = {km_to_miles(km):.2f} miles")
        elif choice == '2':
            miles = float(input("Enter miles: "))
            print(f"{miles} miles = {miles_to_km(miles):.2f} km")
        elif choice == '3':
            c = float(input("Enter Celsius: "))
            print(f"{c}°C = {c_to_f(c):.2f}°F")
        elif choice == '4':
            f = float(input("Enter Fahrenheit: "))
            print(f"{f}°F = {f_to_c(f):.2f}°C")
        elif choice == '5':
            m = float(input("Enter meters: "))
            print(f"{m} m = {m_to_ft(m):.2f} ft")
        elif choice == '6':
            ft = float(input("Enter feet: "))
            print(f"{ft} ft = {ft_to_m(ft):.2f} m")
        elif choice == '7':
            kg = float(input("Enter kilograms: "))
            print(f"{kg} kg = {kg_to_lb(kg):.2f} lbs")
        elif choice == '8':
            lb = float(input("Enter pounds: "))
            print(f"{lb} lbs = {lb_to_kg(lb):.2f} kg")
        elif choice == '9':
            l = float(input("Enter liters: "))
            print(f"{l} L = {l_to_gal(l):.2f} gallons")
        elif choice == '10':
            gal = float(input("Enter gallons: "))
            print(f"{gal} gallons = {gal_to_l(gal):.2f} L")
        elif choice == '11':
            print("👋 Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please choose between 1 and 11.")
    except ValueError:
        print("❌ Please enter a valid number.")
