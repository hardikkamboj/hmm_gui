import numpy as np
from config import *



def predict_weather(current_mood):
    if current_mood == 'H':
        den = p_rh*p_r + p_sh*p_s
        prob_day = (p_sh*p_s / den,p_rh*p_r/ den )
    else:
        den = p_rg*p_r + p_sg*p_s
        prob_day = (p_sg*p_s / den,p_rg*p_r/ den )
    weather_predicted = ['Sunny','Rainy'][np.argmax(prob_day)]
    return prob_day,weather_predicted




def predict_weather_sequence(moods):
    probabilities = []
    weather = []

    if moods[0] == 'H':
        probabilities.append((p_s*p_sh, p_r*p_rh))
    else:
        probabilities.append((p_s*p_sg, p_r*p_rg))

    for i in range(1,len(moods)):
        yesterday_sunny, yesterday_rainy = probabilities[-1]
        if moods[i] == 'H':
            today_sunny = max(yesterday_sunny*p_ss*p_sh, yesterday_rainy*p_rs*p_sh)
            today_rainy = max(yesterday_sunny*p_sr*p_rh, yesterday_rainy*p_rr*p_rh)
            probabilities.append((today_sunny, today_rainy))
        else:
            today_sunny = max(yesterday_sunny*p_ss*p_sg, yesterday_rainy*p_rs*p_sg)
            today_rainy = max(yesterday_sunny*p_sr*p_rg, yesterday_rainy*p_rr*p_rg)
            probabilities.append((today_sunny, today_rainy))

    for p in probabilities:
        if p[0] > p[1]:
            weather.append('S')
        else:
            weather.append('R')

    return weather

print(p_s)
print(predict_weather('G'))