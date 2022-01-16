import requests , json
#from bs4 import BeautifulSoup


url = requests.get("https://open.er-api.com/v6/latest/USD")

txt = url.text
data = json.loads(txt)

time_last_updated = data['time_last_update_utc']

time_next_update = data['time_next_update_utc']

rates = data['rates']
inr = rates['INR']
#print(inr)




