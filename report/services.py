import numpy as np
import pandas as pd
from datetime import datetime
from .models import Brand


class MakeReport:

    def __init__(self, file_path, data):
        self.__file_path = file_path
        self.__data = data
        self.__save_path = datetime.now().strftime('%Y-%m-%d_%H-%M-%S.xlsx')
        self.__df = pd.read_excel(self.__file_path, sheet_name='Список товаров', header=(1,))
        self.__result_df = pd.DataFrame(columns=self.__df.columns)

    def change_df(self):
        for item in self.__data:
            brand_name = MakeReport.get_brand_from_id(int(item["brandId"]))
            rate = float(item["rate"])
            temp_df = self.__df[self.__df['Название товара'].str.contains(brand_name, case=False, na=False)].copy()
            if not temp_df.empty:
                temp_df.loc[temp_df['Базовая цена *'].notna(), 'Ваш порог для софинсирования'] = \
                    (temp_df['Базовая цена *'] * (1 - rate / 100)).round(1)
            self.__result_df = pd.concat([self.__result_df, temp_df])

    def set_difference(self):
        self.__result_df['Разница порогов'] = (
                100 * (self.__result_df['Подходящий порог'] - self.__result_df['Ваш порог для софинсирования'])
                / self.__result_df['Подходящий порог']
        ).round(1)

    def save_to_excel(self):
        self.__result_df.to_excel(self.__save_path, index=False)
        return self.__save_path

    @staticmethod
    def get_brand_from_id(brand_id):
        brand = Brand.objects.get(pk=brand_id)
        return brand.name
