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
            'phone': lambda v: convert_phone(v),
            'zipcode': lambda v: convert_zipcode(v)
        }
    )

    return table3


def convert_score(score):
    try:
        return int(score)
    except:
        print('Invalid score {}'.format(score), file=sys.stderr)
        return 0


def convert_phone(phone):
    try:
        return int(re.sub(r'-|_|\(|\)|\s', '', v))
    except:
        print('Invalid phone {}'.format(phone), file=sys.stderr)
        return 0

def convert_zipcode(zip_code):
    try:
        return int(zip_code)
    except:
        print('Invalid zip code {}'.format(zip_code), file=sys.stderr)
        return 0


def main():
    table = transform('DOHMH_New_York_City_Restaurant_Inspection_Results_sample.csv')


if __name__ == '__main__':
    main()
