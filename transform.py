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
            'score': int,
            'grade': int,
            'phone': lambda v: v.replace(' ', '').replace('-', '').replace('(', '').replace(')', '')
        }
    )

    return table3


def main():
    table = transform('sample.csv')


if __name__ == '__main__':
    main()
