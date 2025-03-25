temp=float(input("Enter temperature in celcius:"))
if temp < 10:
    print("It's cold wear a warm cloth!")
elif temp >= 10 and temp <=  25:
    print("It's mild wear a light jacket!")
elif temp > 25:
    print("It's hot wear a t-shirt")
else :
    print("Enter proper temperature !")
