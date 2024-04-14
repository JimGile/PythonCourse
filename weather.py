temperature = 75
forecast = "rainy"
raining = True
if temperature > 80:
    print("Too hot, Stay inside!")
elif temperature < 30:
    print("Too cold, Stay inside!")
else:
    print("Gtfo!")

if temperature < 80 and forecast != "rainy":
    print("Gtfo!")
else:
    print("Stay inside!")

if not raining:
    print("Gtfo!")