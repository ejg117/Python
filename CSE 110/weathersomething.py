def calculate_wind_chill(temperature, wind_speed):
    wind_chill = 35.74 + 0.6215 * temperature - 35.75 * (wind_speed ** 0.16) + 0.4275 * temperature * (wind_speed ** 0.16)
    return wind_chill

def main():
    while True:
        temperature_input = float(input("What is the temperature? "))
        temp_unit = input("Fahrenheit or Celsius (F/C)? ").upper()

        if temp_unit == "C":
            temperature = (temperature_input * 9/5) + 32
        elif temp_unit == "F":
            temperature = temperature_input
        else:
            print("Invalid input. Please enter 'F' or 'C'.")
            continue
        
        for wind_speed in range(5, 61, 5):
            wind_chill = calculate_wind_chill(temperature, wind_speed)
            print(f"At temperature {temperature:.1f}F, and wind speed {wind_speed} mph, the windchill is: {wind_chill:.2f}F")

        choice = input("Do you want to continue (Y/N)? ").upper()
        if choice != "Y":
            break

if __name__ == "__main__":
    main()