import requests, json

#base url
url = "https://api.openweathermap.org/data/2.5/weather?"

#enter your Api Key
api_id = "your_api_key"

#give name of the city to forecast
city = input("Enter a City Name: ")

#complete the url
complete_url = url+"q="+city+"&appid="+api_id
# print(complete_url)

#get response from the api
response = requests.get(complete_url)
# print(response)

#convert json format to python format
data = response.json()
# print(data)

if data["cod"] != 404:
	print("\n")
	print("==== Today's Weather Forecast ====")
	#get weather description
	weather = data["weather"]
	weather_info = weather[0]["description"]
	print("\n")
	print(f"Description: {weather_info.capitalize()}")	#capitalize first letter

	#get temprature, pressure, humidity
	main = data["main"]

	#get the temperature rating
	temp = main["temp"]
	print(f"Temperature: {int(temp-273.15)}°C")	#converting temperature from kelvin to celcius

	#get the pressure rating
	pressure = main["pressure"]
	print(f"Pressure: {pressure} hPa")

	#get the humidity rating
	humidity = main["humidity"]
	print(f"Humidity: {humidity}%")

	#get wind info
	wind = data["wind"]
	speed = wind["speed"]
	print(f"Wind Speed: {speed} m/s")
	print("\n")

else:
	print("Sorry, can't find your city!")