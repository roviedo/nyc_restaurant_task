import re
import sys

import petl as etl

import connect_to_db


def transform(filename):

    table1 = (
        etl
        .fromcsv(filename)
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

    table3 = etl.convert(
        table2, {
            'score': lambda v: convert_score(v),
            'phone': lambda v: int(re.sub(r'-|_|\(|\)|\s', '', v))
        }
    )

    return table3


def convert_score(score):
    try:
        return int(score)
    except:
        print('Invalid score {}'.format(score), file=sys.stderr)
        return 0


def main():
    table = transform('DOHMH_New_York_City_Restaurant_Inspection_Results_sample.csv')


if __name__ == '__main__':
    main()
