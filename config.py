import pandas as pd
import numpy as np

init_transition_matrix = [0.8,0.2,0.4,0.6]
init_prob_weather = [0.8,0.2]
init_emission_matrix = [0.8,0.2,0.4,0.6]

class Hmm_parameters:

    def __init__(self,transition_matrix = init_transition_matrix, prob_weather = init_prob_weather,emission_matrix = init_emission_matrix):
        self.transition_matrix = transition_matrix
        self.prob_weather = prob_weather
        self.emission_matrix = emission_matrix

    def update_values(self,transition_matrix, prob_weather,emission_matrix):
        self.transition_matrix = transition_matrix
        self.prob_weather = prob_weather
        self.emission_matrix = emission_matrix

    def get_parameters(self):
        p_ss,p_sr,p_rs,p_rr = self.transition_matrix
        p_s, p_r = self.prob_weather
        p_sh,p_sg,p_rh,p_rg = self.emission_matrix

        return p_ss,p_sr,p_rs,p_rr,p_s, p_r,p_sh,p_sg,p_rh,p_rg

    def display_parameters(self):
        print('Transition matrix -')
        d = pd.DataFrame(np.array(self.transition_matrix).reshape(2,2))
        d.columns = ['Sunny','Rainy']
        d.index = ['Sunny','Rainy']
        print(d)
        print()

        print('Probablity of whether')
        print('Probablity of sunny - ',self.prob_weather[0])
        print('Probablity of rainy - ',self.prob_weather[1])

        print(' ')
        d1 = pd.DataFrame(np.array(self.emission_matrix).reshape(2,2))
        d1.columns = ['Happy','Sad']
        d1.index = ['Sunny','Rainy']
        print(d1)
