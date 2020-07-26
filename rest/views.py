from django.shortcuts import render
import requests

def rest(request):
	print("rest entered")
	return render(request,'index.html')

def forecast(request):
	print("forecast enterd")
	API_Key = 'ccc705470451d28b0515203bd845e344'
	city = "Tokyo,jp"
	if request.POST['city']:
		city = request.POST['city']
	url = 'http://api.openweathermap.org/data/2.5/forecast'
	query = {
		'units':'metric',
		'q':city,
		'cnt':'30',
		'appid':API_Key
	}
	r = requests.get(url,params=query)
	print("response",r.json())
	print("Weather forecast in Tokyo at UTC(needs + 9h): ")
	result = []
	for x in range(r.json()['cnt']):
		print("x: ",x)
		result.append(r.json()['list'][x]['dt_txt'])
		result.append("temp: ")
		result.append(r.json()['list'][x]['main']['temp'])
		result.append("weather: ")
		result.append(r.json()['list'][x]['weather'][0]['main'])
		result.append("/")
		result.append(r.json()['list'][x]['weather'][0]['description'])
		result.append('\n')

		print(r.json()['list'][x]['dt_txt'],
			"temp: ",r.json()['list'][x]['main']['temp'],
			'weather: ',r.json()['list'][x]['weather'][0]['main'],"/",r.json()['list'][x]['weather'][0]['description'])

	mapped_num = map(str,result) # 格納される数値を文字列にする
	result_string = ' '.join(mapped_num)
	print("result_string",result_string)
	print("city",city)
	return render(request, 'forecast.html',{'city': city,'result':result_string})
