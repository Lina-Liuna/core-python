import collections

class LinaCalorie(dict):
    def __init__(self, calorie):
        super().__init__(calorie)

    def calorie(self):
        sum = 0
        # print(f'self={self}')
        for (key, value) in self.items():
            sum += value
        return sum

import logging
def calc_calorie(foodc, workoutc):
    lina_food_calorie = LinaCalorie(foodc)
    lina_workout_calorie = LinaCalorie(workoutc)
    lina_total_calorie = lina_food_calorie.calorie() - lina_workout_calorie.calorie()
    print(f'lina food calorie:{lina_food_calorie.calorie()}')
    print(f'lina workout calorie: {lina_workout_calorie.calorie()}')
    logger = logging.getLogger()
    if lina_total_calorie > 100:
        logger.warning(f'watch out!, you input food calorie is far beyond than you output workout caloire!')
        logger.warning(f'lina input calorie in mar 16 is:{lina_total_calorie}')
        logging.warning(f'!!!!!!DO MORE WORKOUT!!!!!!!!, PLEASE EAT LESS TOMORROW!!!!!!!!')

import pandas as pd
import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
import matplotlib

def claorie_diagram(calorie_dict, calor_type_str):
    calorie_df = pd.DataFrame(
        list(calorie_dict.values()),
        index= list(calorie_dict.keys()),
        columns=[calor_type_str]
    )

    matplotlib.rc('figure', figsize=(10, 5))
    for key in calorie_dict.keys():
        calorie_df.style.set_properties(subset=[key], **{'width': '1000000px'})

    calorie_df.plot()
    plt.show()
def mar_16_2023():
    food_calorie = {'two bananas': 105 * 2,
                'one apple': 95,
                'sweet potato': 100,
                'pistachios': 170 * 1.5,
                'salmon': 350,
                'two pepper':24 * 2,
                'cucumber':45,
                'green bean':50}

    workout_calorie = {
        'plank jump-ins': 15,
        'jumping jacks': 100,
        'high knees': 7 * 10 + 7 * 10,
        'squats': 25,
        'hard crunch': 24 * 8,
        'Bubble butt': 130,
        'Five-min-quick-fit': 50,
        'other': 15,
    }
    calc_calorie(food_calorie, workout_calorie)
    claorie_diagram(food_calorie, 'Lina Liu Food Calories')
    claorie_diagram(workout_calorie, 'Lina Liu Workout Calories')

mar_16_2023()