import requests
import json

url = "https://currency-converter18.p.rapidapi.com/api/v1/convert"

Currency_1 = "INR"
Currency_2 = "USD"
Amount = "1000"

querystring = {"from": Currency_1,"to":Currency_2,"amount":Amount}

headers = {
	"X-RapidAPI-Key": "332df1d7ffmshdc495be2d06b4f9p1f6a33jsnb9541a237b5b",
	"X-RapidAPI-Host": "currency-converter18.p.rapidapi.com"
}

response = requests.request("GET", url, headers=headers, params=querystring)

data = json.loads(response.text)
converted_amount = data["result"]["convertedAmount"]
formatted = "{:,.2f}".format(converted_amount)

print(converted_amount, formatted)