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

if __name__ == '__main__':
    main()
