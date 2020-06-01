import pandas as pd


class Preprocessor:
    """ input: the raw dataframe of weather or power plant data,
    output: preprocessed dataframe with hourly datetimeindex """

    def __init__(self, path_to_data, local_time_column, resampling_method):
        self.df_raw = pd.read_csv(path_to_data)
        df_formatted_columns = self._format_columns(self.df_raw)
        df_formatted_datetime = self._format_datetime(df_formatted_columns,
                                                      local_time_column)
        self.df_indexed_ch = self._set_datetime_index(df_formatted_datetime, resampling_method)
        self.df_indexed_utc = self._set_datetime_index(df_formatted_datetime, resampling_method)

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
    def _set_datetime_index(cls, df, resampling_method, utc_time=True):
        """ create datetime index based on local_time or utc,
        and resample mean per hour"""
        if utc_time:
            df = (df.set_index(df["timestamp_utc"])
                    .drop(columns=["timestamp_ch"]))
        else:
            df = (df.set_index(df["timestamp_ch"])
                    .drop(columns=["timestamp_utc"]))
        return cls._resampling(df, resampling_method)

    @classmethod
    def _resampling(cls, df, resampling_method):
        if resampling_method == "sum":
            df_resampled = df.resample("h").sum().ffill()
        elif resampling_method == "mean":
            df_resampled = df.resample("h").mean().ffill()
        df["hour"] = df.index.hour
        df["week"] = df.index.week
        df["month"] = df.index.month
        return df_resampled

