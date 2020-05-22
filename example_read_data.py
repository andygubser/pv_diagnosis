from preprocessor.paths import (PATH_TO_PLANT_A,
                                PATH_TO_PLANT_B,
                                PATH_TO_PLANT_C,
                                PATH_TO_WEATHER)
from preprocessor.preprocessor import PlantPreprocessor
from preprocessor.weather_preprocessor import WeatherPreprocessor

data_power_plant_a = PlantPreprocessor(PATH_TO_PLANT_A).df_indexed_utc
data_weather = WeatherPreprocessor(PATH_TO_WEATHER).df_indexed_utc


