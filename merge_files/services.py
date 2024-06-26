import os
import pandas as pd
from datetime import datetime
from pathlib import Path
from django.conf import settings


class MergeFiles:
    """
    Класс для соединения двух отчетов в один
    """

    def __init__(self, sanbest_file: str, market_file: str):
        """
        Инициализатор класса соединения файлов
        Читает файлы в датафреймы pandas
        :param sanbest_file: путь к файлу, полученного с Sanbest.ru
        :param market_file: путь к файлу, полученного с Я.Маркета
        """

        self.__sanbest_df = pd.read_csv(sanbest_file, delimiter=';', on_bad_lines='skip')
        self.__market_df = pd.read_excel(market_file, header=4)

    def merge_files(self) -> str:
        """
        Соединяет файл с Sanbest.ru и Я.Маркета
        :return: Возвращает путь к соединенному файлу
        """

        merge_df = pd.merge(self.__sanbest_df, self.__market_df, left_on='SKU на нашем сайте', right_on='SKU',
                            how='inner')
        save_dir = Path(__file__).parent.parent / 'media/merge_files'
        if not os.path.exists(save_dir):
            os.makedirs(save_dir)
        merge_filename = f'{save_dir}/merge_{datetime.now()}.xlsx'
        merge_df.to_excel(merge_filename, index=False)
        return merge_filename

    def delete_useless_columns(self) -> None:
        """
        Удаляет лишние столбцы в датафрейме self.market_file
        Столбцы для удаления необходимо указать в настройках проекта config/settings
        :return: None
        """

        columns = []
        for column in columns:
            if column in self.__market_df.columns:
                self.__market_df = self.__market_df.drop(columns=column)
