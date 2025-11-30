# step 1. ask for user input for temperature in fahrenheit
temperature = int(input("What is the temperature in Farenheit? "))

# step 2. convert the temperature from fahrenheit to celsius

new_temp = (temperature-32)*(5/9)

# step 3. print out the new temperature in celsius

print("The temperature in Celsius is:")
print(new_temp)

# C = (F - 32) * (5/9)