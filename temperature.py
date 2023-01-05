import requests
import json

# Monoxyde de carbone (CO) !!!!!!!!!!!
# Dioxyde d’azote (NO2) !!!!!!!!!!!
# Ozone (O3)
# Anhydride sulfureux (SO2)
# Particules PM2,5
# Particules PM10

def temps(city):
    api_url = 'https://api.api-ninjas.com/v1/airquality?city={}'.format(city)
    response = requests.get(api_url, headers={'X-Api-Key': 'qBtvs6QhscjFF1vmScOB5A==NgBV8wGDx4gDRb7C'})
    if response.status_code == requests.codes.ok:
        data = response.json();
        json_data = json.dumps(data);

        data1 = json.loads(json_data)

        Monoxyde_de_carbone = data1['CO']
        Dioxyde_d_azote = data1['NO2']

        #print(Monoxyde_de_carbone)
        #print(Dioxyde_d_azote)

        Monoxyde_de_carbones = Monoxyde_de_carbone['concentration']
        Dioxyde_d_azotes = Dioxyde_d_azote['concentration']
        # print(Monoxyde_de_carbones)
        # print(Dioxyde_d_azotes)

    else:
        print("Error:", response.status_code, response.text)




    #   "wind_speed": 5.66,     !!!!!!!!!!!
    #   "wind_degrees": 210,    !!!!!!!!!!!
    #   "temp": 7,              !!!!!!!!!!!
    #   "humidity": 87,         !!!!!!!!!!!
    #   "sunset": 1615658463,
    #   "min_temp": 7,          !!!!!!!!!!!
    #   "cloud_pct": 75,
    #   "feels_like": 2,
    #   "sunrise": 1615616341,  !!!!!!!!!!!
    #   "max_temp": 8           !!!!!!!!!!!




    #   « vitesse du vent »: 5,66,  !!!!!!!!!!!
    #   « degrés de vent »: 210,    !!!!!!!!!!!
    #   « temp »: 7,                !!!!!!!!!!!
    #   « humidité »: 87,           !!!!!!!!!!!
    #   « coucher de soleil »: 1615658463,
    #   « température minimale »: 7,    !!!!!!!!!!!
    #   « Cloud PCT »: 75,
    #   « se sent comme »: 2,
    #   « lever du soleil »: 1615616341,    !!!!!!!!!!!
    #   « température maximale »: 8         !!!!!!!!!!!




    api_url = 'https://api.api-ninjas.com/v1/weather?city={}'.format(city)
    response = requests.get(api_url, headers={'X-Api-Key': 'qBtvs6QhscjFF1vmScOB5A==NgBV8wGDx4gDRb7C'})
    if response.status_code == requests.codes.ok:
        datas = response.json();
        json_datas = json.dumps(datas);

        data2 = json.loads(json_datas)

        vitesse_du_vent = data2['wind_speed']
        temperature = data2['temp']
        temperature_max = data2['max_temp']
        temperature_min = data2['min_temp']
        humidite = data2['humidity']
        
        print(vitesse_du_vent)
        print(temperature)
        print(temperature_max)
        print(temperature_min)
        print(humidite)

    else:
        print("Error:", response.status_code, response.text)
    
    return(Monoxyde_de_carbones,Dioxyde_d_azotes,vitesse_du_vent,temperature,temperature_max,temperature_min,humidite)
