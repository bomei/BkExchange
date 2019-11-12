from db.db_interface import TickDBInterface
import pandas as pd
import pathlib
import sys
from log import log
import arrow
from data_structure import Tick


class CsvDB(TickDBInterface):
    def __init__(self, options):
        self.csv_path = options['csv.path']
        if pathlib.Path(self.csv_path).exists():
            try:
                self.df = pd.read_csv(self.csv_path)
            except:
                log.warning(f"Read csv {self.csv_path} error")
        else:
            log.warning("csv.path not exists")
            sys.exit(1)

    def sort_df_by_time(self):
        if 'time' in self.df.columns:
            time_column = 'time'
        elif 'timestamp' in self.df.columns:
            time_column = 'timestamp'
        else:
            log.warning(f'"time" or "timestamp" in df.columns is required but not found in csv {self.csv_path}')
            return
        self.df.sort_values(time_column, inplace=True)

    def generate_tick(self):
        self.sort_df_by_time()
        for _, row in self.df.iterrows():
            d = {}
            for i in range(len(row)):
                d[self.df.columns[i]] = row[i]
            tick = Tick().from_dict(d)
            yield tick


def main():
    options = {
        "csv.path": r"C:\Users\zannb\jupyter-notebook\candle_btc.usdt-xtc.okex_1m_1546300800_1547078400.csv"
    }
    csv_db = CsvDB(options)
    for tick in csv_db.generate_tick():
        print(tick)


if __name__ == '__main__':
    main()
