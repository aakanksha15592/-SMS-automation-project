import requests
from twilio.rest import Client

OWM_ENDPOINT = "https://api.openweathermap.org/data/2.5/weather"
api_key = "a1173e1c34196544c25aa4b242a9b40e"
account_sid = "AC1c38d2466a5ccd8720361f70beafc400"
auth_token = "759f0eded686dbcf67ae558e126f27ba"
weather_parameter = {
    "lat": 19.134510,
    "lon": 72.911797,
    "appid": api_key,
    "exclude": "current,minute,daily",
    "include": "hourly"
}
response = requests.get(OWM_ENDPOINT, params=weather_parameter)
response.raise_for_status()
weather_data = response.json()
weather_slice = weather_data["weather"]

will_rain = False

for data in weather_slice:
    conition_code = weather_data["hourly"][0]["id"]
    if int(conition_code) < 700:
        will_rain = True

if will_rain:
    client = Client(account_sid, auth_token)
    message = client.messages.create(
        body= "It's going to rain today. Remember to bring an ☔",
        from_="+14787072932",
        to="+917505978427"
    )

    print(message.status)

