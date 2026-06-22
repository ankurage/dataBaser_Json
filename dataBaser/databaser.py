import os
import json

class DataBase:
    def __init__(self, db_name):
        self.db_name = db_name

    def db_format_check(db):
        check = db[::-1]
        if check[:5] == "nosj.":
            return True
        else:
            return False
        
    # == | == #
    def create(self, obj: any, check_exists: bool=True, encode: str="utf-8", ensure_ascii: bool=False, indent: int=4):
        if check_exists:
            if not os.path.exists(self.db_name):
                with open(self.db_name, "w", encoding=encode) as file:
                    json.dump(obj, file, indent=indent, ensure_ascii=ensure_ascii)
        else:
            with open(self.db_name, "w", encoding=encode) as file:
                json.dump(obj, file, indent=indent, ensure_ascii=ensure_ascii)

    # == | == #
    def get(self, encode: str="utf-8"):
        try:
            with open(self.db_name, "r", encoding=encode) as file:
                data = json.load(file)
                return data
        except json.decoder.JSONDecodeError:
            raise ValueError("Decode Error")
            
    # == | == #
    def load(self, obj: any, encode: str="utf-8", ensure_ascii: bool=False, indent: int=4):
        with open(self.db_name, "w", encoding=encode) as file:
            json.dump(obj, file, indent=indent, ensure_ascii=ensure_ascii)
