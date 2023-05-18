import sqlite3

from common.FileProvider import FileProvider


class JournalDatabase:

    DATABASE_NAME = "journal_database"

    def __init__(self):
        self.connection = sqlite3.connect(FileProvider.get_file_path(filename=self.DATABASE_NAME))
        self.cursor = self.connection.cursor()
