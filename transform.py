import petl as etl

def main():
    print('main etl program')
    # table = (
    #     etl
    #     .fromcsv('DOHMH_New_York_City_Restaurant_Inspection_Results_sample.csv')
    #     .convert('foo', 'upper')
    #     .convert('bar', int)
    #     .convert('baz', float)
    #     .addfield('quux', lambda row: row.bar * row.baz)
    # )
    #
    # table.look()
    '''
    +-------+-------+
    | 'foo' | 'bar' |
    +=======+=======+
    | 'a'   | 1     |
    +-------+-------+
    | 'b'   | 2     |
    +-------+-------+
    | 'c'   | 2     |
    +-------+-------+
    '''


    table = (
        etl
        .fromcsv('DOHMH_New_York_City_Restaurant_Inspection_Results_sample.csv')
    )
    # Create restaurants table data
    #
    #etl.rename(table1, 'sex', 'gender')
    # tosqlite3(table, 'test.db', 'foobar')
    for row in table:
        print(type(row))


if __name__ == '__main__':
    main()
