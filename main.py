import json
import pandas
from pathlib import Path # for specifying the path
 #Csv, parquet, Excel, xml, txt, html etc.

def read_file(file_path):
    #Csv, parquet, Excel, xml, txt, html, pickle, tsv, Feather etc
    file_path = Path(file_path)

    if not file_path.exists():
        raise FileNotFoundError(f"File not found{file_path}")

    extension = file_path.suffix.lower()

    try:
        if extension == ".csv":
            return pandas.read_csv(file_path)
        
        elif extension in [".xls", ".xlsx"]:
            return pandas.read_excel(file_path)

        elif extension in [".xml"]:
                    return pandas.read_xml(file_path)
        
        elif extension == ".json":
            return pandas.read_json(file_path)
        
        elif extension == ".parquet":
            return pandas.read_parquet(file_path)

        else:
            raise ValueError(
                f"Unsupported file format{extension}"
                )
    except Exception as error:
        raise RuntimeError(
            f"failed to read {file_path}: {error}"
            )
        
        