import unittest
import setup_db
import os

class TestTransform(unittest.TestCase):
    def setUp(self):
        c = setup_db.connect_to_db('test_main.db')
        setup_db.create_tables(c)

    def tearDown(self):
        os.remove('test_main.db')

    def test_split(self):
        s = 'hello world'
        self.assertEqual(s.split(), ['hello', 'world'])
        # check that s.split fails when the separator is not a string
        with self.assertRaises(TypeError):
            s.split(2)

if __name__ == '__main__':
    unittest.main()
