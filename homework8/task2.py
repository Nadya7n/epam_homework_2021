import sqlite3
from collections import abc


class TableData(abc.Collection):
    def __init__(self, database_name, table_name):
        self.database_name = database_name
        self.table_name = table_name
        with sqlite3.connect(self.database_name) as conn:
            self.cursor = conn.cursor()

    def __len__(self):
        """
        Give current amount of rows in table in database
        :return: amount of rows
        """
        self.cursor.execute(f"SELECT count(*) from {self.table_name}")
        n_rows = self.cursor.fetchone()
        return n_rows[0]

    def __getitem__(self, item):
        """
        Return single data row for element in table with name=item
        :param item: key name of row
        :return: single data row
        """
        self.cursor.execute(
            f"SELECT * from {self.table_name} where name=:name", {"name": item}
        )
        return self.cursor.fetchone()

    def __contains__(self, item):
        """
        Check if row with key name=item exists in table
        :param item: key name
        :return: bool
        """
        self.cursor.execute(
            f"SELECT count(*) from {self.table_name} where name=:name", {"name": item}
        )
        return self.cursor.fetchone()[0] >= 1

    def __iter__(self):
        """
        Give ability to be iterable
        :return: iterator
        """
        self.cursor.execute(f"SELECT * from {self.table_name}")
        while row := self.cursor.fetchone():
            yield row
