import json
from typing import List
from logger import setup_logger

logger = setup_logger()

class Settings:
    def __init__(self, settings_file: str = "settings.json") -> None:
        self.settings_file = settings_file
        self.default_columns = ["ID", "Name", "Status"]
        self.selected_columns = self.load_settings()

    def load_settings(self) -> List[str]:
        try:
            with open(self.settings_file, 'r') as file:
                settings = json.load(file)
                return settings.get("selected_columns", self.default_columns)
        except (FileNotFoundError, json.JSONDecodeError) as e:
            logger.error(f"Error loading settings: {e}")
            return self.default_columns

    def save_settings(self) -> None:
        try:
            with open(self.settings_file, 'w') as file:
                json.dump({"selected_columns": self.selected_columns}, file)
        except Exception as e:
            logger.error(f"Error saving settings: {e}")

    def update_selected_columns(self, columns: List[str]) -> None:
        self.selected_columns = columns
        self.save_settings()
