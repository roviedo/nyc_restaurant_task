import unittest
import setup_db
import os
import connect_to_db
import transform


class TestTransform(unittest.TestCase):
    def setUp(self):
        try:
            self.conn = connect_to_db.connect_to_sqlite3('test_main.db')
            setup_db.create_tables(self.conn)
        except sqlite3.OperationalError:
            None


    def tearDown(self):
        os.remove('test_main.db')


    def test_insert(self):
        c = self.conn.cursor()
        restaurants = [
            (
                40397962,'BEN ASH DELICATESSEN','MANHATTAN',855,'7 AVENUE',10019,2122651818,'Delicatessen','08/05/2016','Violations were cited','10F','Non-food contact surface improperly constructed.','Not Critical',10,'A','08/05/2016','05/25/2017','Re-inspection'
            )
        ]

        c.executemany(
            '''
            INSERT INTO restaurant (
                camis, name, boro, building, street, zipcode, phone, cuisine_description,
                inspection_date, action, violation_code, violation_description,
                critical_flag, score, grade, grade_date, record_date, inspection_type
            ) VALUES (?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?,?)
            ''',
            restaurants
        )

        c.execute('SELECT * from restaurant where id = 1')
        restaurant_row = (1, 40397962,'BEN ASH DELICATESSEN','MANHATTAN',855,'7 AVENUE',10019,2122651818,'Delicatessen','08/05/2016','Violations were cited','10F','Non-food contact surface improperly constructed.','Not Critical',10,'A','08/05/2016','05/25/2017','Re-inspection')
        self.assertEqual(c.fetchone(), restaurant_row)

    def test_transform(self):
        table = transform.transform('DOHMH_New_York_City_Restaurant_Inspection_Results_sample.csv')
        self.assertEqual(len(table), 10)

if __name__ == '__main__':
    unittest.main()
