import pandas as pd


class Preprocessor:
    """ input: raw dataframe of weather data,
    output: preprocessed dataframe with hourly datetimeindex """

    def __init__(self, path_to_weather, local_time_column):
        self.df_raw = pd.read_csv(path_to_weather)
        df_formatted_columns = self._format_columns(self.df_raw)
        df_formatted_datetime = self._format_datetime(df_formatted_columns,
                                                      local_time_column)
        self.df_indexed_ch = self._set_datetime_index(df_formatted_datetime)
        self.df_indexed_utc = self._set_datetime_index(df_formatted_datetime)

    @classmethod
    def _format_columns(cls, df):
        columns_lower = df.columns.str.lower()
        columns_clean = columns_lower.str.replace("-", "")
        df.columns = columns_clean
        return df

    @classmethod
    def _format_datetime(cls, df, local_time_column):
        df["timestamp_ch"] = \
            pd.to_datetime(df[local_time_column]).\
            dt.tz_localize(tz="Europe/Zurich",
                           ambiguous=True,
                           nonexistent="NaT")
        df["timestamp_utc"] = \
            df["timestamp_ch"]. \
            dt.tz_convert("UTC")
        df.ffill(inplace=True)
        return df

    @classmethod
    def _set_datetime_index(cls, df, utc_time=True):
        """ create datetime index based on local_time or utc,
        and resample mean per hour"""
        if utc_time:
            df.set_index(df["timestamp_utc"], inplace=True)
        elif not utc_time:
            df.set_index(df["timestamp_ch"], inplace=True)
        else:
            print("local_time error")
        return df.resample("h").mean()