import requests

APP_ID = "9106730b5f69eaa97b32270fb7410727ea8c1322"
API_URL  = "https://api.e-stat.go.jp/rest/2.1/app/json/getStatsData"

params = {
    "appId": APP_ID,
    "statsDataId": "0003412313",# 消費者物価指数（CPI）の統計表ID
    "cdArea": "00000",
    "cdTime": "202110",
    "lang": "J"
}




#response = requests.get(API_URL, params=params)
response = requests.get(API_URL, params=params)
# Process the response
data = response.json()
print(data)