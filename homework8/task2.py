import sqlite3


class TableData:
    dct = {}

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
        n_rows = self.__len__()
        self.cursor.execute(f"SELECT * from {self.table_name}")
        for i in range(n_rows):
            data = self.cursor.fetchone()
            self.dct[data[0]] = data
        return self.dct[item]

    def __contains__(self, item):
        """
        Check if row with key name=item exists in table
        :param item: key name
        :return: bool
        """
        return item in self.dct.keys()

    def __iter__(self):
        """
        Give ability to be iterable
        :return: iterator
        """
        n_rows = self.__len__()
        self.cursor.execute(f"SELECT * from {self.table_name}")
        iterator = (self.cursor.fetchone() for el in range(n_rows))
        return iterator
