import ssl
import urllib.request
from abc import ABC, abstractmethod


class Extract(ABC):
    @abstractmethod
    def extract_data_from_source(self):
        pass


class ExtractCSV(Extract):

    def extract_data_from_source(self, url, filename):
        context = ssl._create_unverified_context()
        f = urllib.request.urlopen(url, context=context)
        data = f.read()
        with open(filename, "wb") as code:
            code.write(data)


def main():
    CSV_URL = 'https://nycopendata.socrata.com/api/views/xx67-kt59/rows.csv?accessType=DOWNLOAD'
    filename = 'DOHMH_New_York_City_Restaurant_Inspection_Results.csv'
    extract = ExtractCSV()
    extract.extract_data_from_source(CSV_URL, filename)


if __name__ == '__main__':
    main()
