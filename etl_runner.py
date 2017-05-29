import extract
import transform
import load


#TODO: This needs to be a periodic task hourly, daily etc. or if it's a manual task then need an UI
def runner():
    CSV_URL = 'https://nycopendata.socrata.com/api/views/xx67-kt59/rows.csv?accessType=DOWNLOAD'
    filename = 'DOHMH_New_York_City_Restaurant_Inspection_Results.csv'

    extract_csv = extract.ExtractCSV()
    extract_csv.extract_data_from_source(CSV_URL, filename)
    table = transform.transform(filename)
    load.load(table)


def main():
    runner()


if __name__ == '__main__':
    main()
