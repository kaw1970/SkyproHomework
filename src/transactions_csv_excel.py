from typing import Any, Dict

import pandas as pd


def transactions_csv(file_path: str) -> list[Dict[str, Any]]:
    """������� ��� ���������� ���������� �������� �� CSV."""
    df = pd.read_csv(file_path, sep=';')
    dict_data = df.to_dict(orient='records')
    return dict_data


def transactions_excel(file_path: str) -> list[Dict[str, Any]]:
    """������� ��� ���������� ���������� �������� �� Excel."""
    df = pd.read_excel(file_path)
    dict_dada = df.to_dict(orient='records')
    return dict_dada

