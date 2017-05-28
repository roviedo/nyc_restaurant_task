import petl as etl
import sqlite3


def main():
    print('Running main ETL program')

    table1 = (
        etl
        .fromcsv('DOHMH_New_York_City_Restaurant_Inspection_Results_sample.csv')
    )

    # Create restaurants table data
    table2 = etl.rename(
        table1,
        {
            'CAMIS': 'camis',
            'DBA': 'name',
            'BORO': 'boro',
            'BUILDING': 'building',
            'STREET': 'street',
            'ZIPCODE': 'zipcode',
            'PHONE': 'phone',
            'CUISINE DESCRIPTION': 'cuisine_description',
            'INSPECTION DATE': 'inspection_date',
            'ACTION': 'action',
            'VIOLATION CODE': 'violation_code',
            'VIOLATION DESCRIPTION': 'violation_description',
            'CRITICAL FLAG': 'critical_flag',
            'SCORE': 'score',
            'GRADE': 'grade',
            'GRADE DATE': 'grade_date',
            'RECORD DATE': 'record_date',
            'INSPECTION TYPE': 'inspection_type'
        }
    )

    connection = sqlite3.connect('main.db')
    etl.todb(table2, connection, 'restaurant')


if __name__ == '__main__':
    main()
