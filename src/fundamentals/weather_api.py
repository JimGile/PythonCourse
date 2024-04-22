import requests

city = 'Denver'
url = 'http://api.weatherapi.com/v1/current.json?key=f6146603d02e4098b5a235946241404&q=' + city + '&aqi=no'
response = requests.get(url)
weather_json = response.json()

print(weather_json)

location = weather_json.get('location')
name = location.get('name')
region = location.get('region')
current = weather_json.get('current')
temp = current.get('temp_f')
descr = current.get('condition').get('text')

print(name, region, temp, descr)
