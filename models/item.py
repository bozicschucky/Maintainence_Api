import sqlite3


class ItemModel:
    def __init__(self, name, id):
        self.name = name
        self.price = id

    def json(self):
        return {'name': self.name, 'id': self.id}

    @classmethod
    def find_by_name(cls, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM items WHERE name=?"
        result = cursor.execute(query, (name,))
        row = result.fetchone()
        connection.close()

        if row:
            return row(*row)

    def insert(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "INSERT INTO item VALUES(?, ?)"
        cursor.execute(query, (self.name, self.id))

        connection.commit()
        connection.close()

    @classmethod
    def update(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "UPDATE item SET id=? WHERE name=?"
        cursor.execute(query, (self.id, self.name))

        connection.commit()
        connection.close()
