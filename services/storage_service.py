import json
import os


class StorageService:

    @staticmethod
    def load_data(file_path):
        if not os.path.exists(file_path):
            return []

        try:
            with open(file_path, "r") as file:
                return json.load(file)

        except json.JSONDecodeError:
            return []

    @staticmethod
    def save_data(file_path, data):
        with open(file_path, "w") as file:
            json.dump(data, file, indent=4)