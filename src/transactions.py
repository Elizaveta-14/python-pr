import pandas as pd
import csv


def read_csv(file_path: str) -> list[dict]:
    """Функция принимает пусть к файлу .csv и возвращает список словарей."""
    try:
        with open(file_path, encoding="utf-8") as file_name:
            reader = csv.DictReader(file_name, delimiter=";")

            return list(reader)
    except FileNotFoundError:

        return []


def read_excel(file_path) -> list[dict]:
    """Функция принимает пусть к файлу формата excel и возвращает список словарей."""
    try:
        excel_data = pd.read_excel(file_path).to_dict(orient="records")

        return excel_data
    except FileNotFoundError:

        return []


# if __name__ == "__main__":
#    print(read_excel)
