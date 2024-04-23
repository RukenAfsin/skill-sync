import requests
import json

api_key = "YOUR-API-KEY" 
url = f"https://v6.exchangerate-api.com/v6/{api_key}/latest/"



exchange=input("bozulan döviz türü: ")
exchange_2=input("alınan döviz türü: ")
money=int(input("ne kadar bozduracaksınız? "))

response = requests.get(url+exchange)

result_json=json.loads(response.text)


print(result_json["conversation_rates"][exchange_2])

print("1 {0} = {1} {2}".format(exchange,result_json ["conversation_rates"] [exchange_2],exchange_2))

print("{0} {1} = {2}{3}".format(money,exchange, money*result_json["conversation_rates"][exchange_2],exchange_2))

