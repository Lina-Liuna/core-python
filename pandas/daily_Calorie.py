import collections

class LinaCalorie(dict):
    def __init__(self, calorie):
        super().__init__(calorie)

    def calorie(self):
        sum = 0
        print(f'self={self}')
        for (key, value) in self.items():
            sum += value
        return sum

import pandas as pd
import numpy as np
import matplotlib as mp
import matplotlib.pyplot as plt
import matplotlib


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
        'high knees': 7 * 10,
        'squats': 25,
        'hard crunch': 24 * 8,
        'Bubble butt': 130,
        'Five-min-quick-fit': 50,
        'other': 15,
    }

    lina_food_calorie = LinaCalorie(food_calorie)
    lina_workout_calorie = LinaCalorie(workout_calorie)
    lina_total_calorie = lina_food_calorie.calorie() - lina_workout_calorie.calorie()
    print(f'lina food calorie:{lina_food_calorie.calorie()}')
    print(f'lina workout calorie: {lina_workout_calorie.calorie()}')
    print(f'lina input calorie in mar 16 is:{lina_total_calorie}')

    calorie_df = pd.DataFrame(
        list(food_calorie.values()),
        index= list(food_calorie.keys()),
        columns=['food calorie']
    )

    matplotlib.rc('figure', figsize=(10, 5))
    for key in food_calorie.keys():
        calorie_df.style.set_properties(subset=[key], **{'width': '1000000px'})

    calorie_df.plot()
    plt.show()
mar_16_2023()


