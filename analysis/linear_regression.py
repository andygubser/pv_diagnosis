import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from preprocessors.paths import (PATH_TO_PLANT_A,
                                 PATH_TO_PLANT_B,
                                 PATH_TO_PLANT_C,
                                 PATH_TO_WEATHER)
from preprocessors.plant_preprocessor import PlantPreprocessor
from preprocessors.weather_preprocessor import WeatherPreprocessor

data_plant_a = PlantPreprocessor(PATH_TO_PLANT_A).df_indexed_utc
data_plant_b = PlantPreprocessor(PATH_TO_PLANT_B).df_indexed_utc
data_plant_c = PlantPreprocessor(PATH_TO_PLANT_C).df_indexed_utc
data_weather = WeatherPreprocessor(PATH_TO_WEATHER).df_indexed_utc

# model_1: estimate \beta1, hypothesis: \beta1 is constant
# multiple linear regression
# actual_production_{time, plant} = \beta0 + \beta1_{plant}*weather_potential_{time} + ...
#       (A/B/C)                                 (estimate)        (weather)

data = pd.merge(left=data_plant_a, right=data_weather,
                left_index=True, right_index=True)
sns.set("poster")
fig, ax = plt.subplots()
data_plant_a.plot(legend=False, ax=ax)
plt.show()
