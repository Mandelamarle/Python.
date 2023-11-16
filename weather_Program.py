ask_weather = input("Guess the weather degree today: ")
if int(ask_weather) >= 30:
    print("The weather today is too hot, please wear a light cloth, possibly a white cloth...")
elif int(ask_weather) >= 25:
    print("The weather is kinda hot today")
elif int(ask_weather) >= 15:
    print("The weather is cold, abeg wear jacket")
else:
    print("Bro, call her (_-_)")