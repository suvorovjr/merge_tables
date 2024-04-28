import openpyxl
import os
import csv


class ToCSVClient:

    def __init__(self, market_file):
        self.market_file = market_file

    def clear_excel_files(self):
        workbook = openpyxl.load_workbook(self.market_file)
        sheet = workbook.active
        ToCSVClient.delete_unwanted_row(sheet)
        ToCSVClient.share_cells(sheet)
        new_path = ToCSVClient.get_to_csv(sheet, self.market_file)
        return new_path

    @staticmethod
    def share_cells(sheet):
        merged_cells = [str(merged_cell) for merged_cell in sheet.merged_cells.ranges]
        for merged_cell in merged_cells:
            sheet.unmerge_cells(str(merged_cell))
        sheet.delete_rows(6)

    @staticmethod
    def is_colored(cell):
        if cell.fill.fgColor.rgb is not None and cell.fill.fgColor.rgb != "00000000" and cell.fill.fgColor.rgb != "FFFFFFFF":
            return True
        return False

    @staticmethod
    def get_to_csv(sheet, excel_path):
        csv_path = os.path.splitext(excel_path)[0] + '.csv'
        with open(csv_path, 'w', newline='', encoding='utf-8-sig') as file:
            c = csv.writer(file, delimiter=';')
            for row in sheet.iter_rows(min_row=5, values_only=True):
                c.writerow(row)
        return csv_path

    @staticmethod
    def delete_unwanted_row(sheet):
        for row in sheet.iter_rows(min_row=5, max_row=5):
            for cell in row:
                if not ToCSVClient.is_colored(cell):
                    sheet.delete_cols(cell.column, 1)
