import unittest
import setup_db
import os
import sqlite3

class TestTransform(unittest.TestCase):
    def setUp(self):
        try:
            self.conn = setup_db.connect_to_db('test_main.db')
            setup_db.create_tables(self.conn)
        except sqlite3.OperationalError:
            None

    def tearDown(self):
        os.remove('test_main.db')

    def test_insert(self):
        c = self.conn.cursor()
        restaurants = [
            (23456, 'Chick F', 'Queens', 'cool building', '123 hoyt street', 12345, 3471234567, 'cool place'),
            (67891, 'Beef C', 'Brooklyn', 'cool building', '124 hoyt street', 12345, 3471234567, 'cool place'),
        ]

        c.executemany(
            '''INSERT INTO restaurant (camis, name, boro, building, street, zipcode, phone, cuisine_description)
            VALUES (?, ?,?,?,?,?,?,?)''',
            restaurants
        )

        c.execute('SELECT * from restaurant where id = 1')
        restaurant_row = (1, 23456, 'Chick F', 'Queens', 'cool building', '123 hoyt street', 12345, 3471234567, 'cool place')
        self.assertEqual(c.fetchone(), restaurant_row)

if __name__ == '__main__':
    unittest.main()
