import pandas as pd


class PlantPreprocessor:
    """ input: raw dataframe of weather data,
    output: preprocessed dataframe with hourly datetimeindex """
    def __init__(self, path_to_plant):
        self.df_raw = pd.read_csv(path_to_plant)
        df_formatted_columns = self._format_columns(self.df_raw)
        df_datetime_indexed = self._set_datetime_index(df_formatted_columns)
        self.df_preprocessed = df_datetime_indexed

    @classmethod
    def _format_columns(cls, df):
        columns_lower = df.columns.str.lower()
        columns_clean = columns_lower.str.replace("-", "")
        df.columns = columns_clean
        return df

    @classmethod
    def _set_datetime_index(cls, df):
        """ create datetime index based on local_time,
        and resampled mean per hour"""
        df["timestamp"] = pd.to_datetime(df["timestamp"])
        df.set_index(df["timestamp"], inplace=True)
        df = df.resample("h").mean()
        return df
