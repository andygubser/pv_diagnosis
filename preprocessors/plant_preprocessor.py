import pandas as pd


class PlantPreprocessor:
    """ input: raw dataframe of weather data,
    output: preprocessed dataframe with hourly datetimeindex """

    def __init__(self, path_to_plant):
        self.df_raw = pd.read_csv(path_to_plant)
        df_formatted_columns = self._format_columns(self.df_raw)
        df_formatted_datetime = self._format_datetime(df_formatted_columns)
        self.df_indexed_ch = self._set_datetime_index(df_formatted_datetime.copy(), local_time=True)
        self.df_indexed_utc = self._set_datetime_index(df_formatted_datetime, local_time=False)

    @classmethod
    def _format_columns(cls, df):
        columns_lower = df.columns.str.lower()
        columns_clean = columns_lower.str.replace("-", "")
        df.columns = columns_clean
        return df

    @classmethod
    def _format_datetime(cls, df):
        df["timestamp_ch"] = pd.to_datetime(df["timestamp"]). \
            dt.tz_localize("Europe/Zurich",
                           ambiguous="NaT",
                           nonexistent="NaT")
        df["timestamp_utc"] = df["timestamp_ch"]. \
            dt.tz_convert("UTC")
        return df

    @classmethod
    def _set_datetime_index(cls, df, local_time):
        """ create datetime index based on local_time or utc,
        and resample mean per hour"""
        if local_time:
            df = (df.set_index(df["timestamp_ch"])
                    .drop(columns=["timestamp_utc"]))
        else:
            df = (df.set_index(df["timestamp_utc"])
                    .drop(columns=["timestamp_ch"]))
        return df.resample("h").mean().ffill()
