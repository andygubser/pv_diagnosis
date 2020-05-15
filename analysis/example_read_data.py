from preprocessors.paths import (PATH_TO_PLANT_A,
                                 PATH_TO_PLANT_B,
                                 PATH_TO_PLANT_C,
                                 PATH_TO_WEATHER)
from preprocessors.plant_preprocessor import PlantPreprocessor
from preprocessors.weather_preprocessor import WeatherPreprocessor

data_power_plant_a = PlantPreprocessor(PATH_TO_PLANT_A).df_preprocessed
data_weather = WeatherPreprocessor(PATH_TO_WEATHER).df_preprocessed


