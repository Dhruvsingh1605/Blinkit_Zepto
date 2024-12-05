import requests
url = "https://openweathermap.org/city/1273294"

def data_scrpae_and_save(url, path):
    r = requests.get(url)
    with open(path,'w') as f:
        f.write(r.text)
data_scrpae_and_save(url, "data_time.html")