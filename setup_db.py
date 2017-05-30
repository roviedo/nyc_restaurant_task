import connect_to_db

"""
camis: CAMIS,
name: DBA,
boro: BORO,
building: BUILDING,
street: STREET,
zipcode: ZIPCODE,
phone: PHONE,
cuisine_description: CUISINE DESCRIPTION,
inspection_date: INSPECTION DATE,
action: ACTION,
violation_code: VIOLATION CODE,
violation_description: VIOLATION DESCRIPTION,
critical_flag: CRITICAL FLAG,
score: SCORE,
grade: GRADE,
grade_date: GRADE DATE,
record_date: RECORD DATE,
inspection_type: INSPECTION TYPE
"""


def create_tables(conn):
    c = conn.cursor()
    c.execute(
        '''
        CREATE TABLE restaurant(
          id    INTEGER PRIMARY KEY AUTOINCREMENT,
          camis INTEGER,
          name  TEXT,
          boro TEXT,
          building TEXT,
          street TEXT,
          zipcode INTEGER,
          phone INTEGER,
          cuisine_description TEXT,
          inspection_date   TEXT,
          action TEXT,
          violation_code TEXT,
          violation_description TEXT,
          critical_flag TEXT,
          score TEXT,
          grade TEXT,
          grade_date TEXT,
          record_date TEXT,
          inspection_type TEXT
        );
        '''
    )
    #TODO: Add indexes and unique clauses

    conn.commit()


def main():
    conn = connect_to_db.connect_to_sqlite3('main.db')
    create_tables(conn)

if __name__ == '__main__':
    main()
