def build_json(row):
    return {
        'id': row[0],
        'camis': row[1],
        'name': row[2],
        'boro': row[3],
        'building': row[4],
        'street': row[5],
        'zipcode': row[6],
        'phone': row[7],
        'cuisine_description': row[8],
        'inspection_date': row[9],
        'action': row[10],
        'violation_code': row[11],
        'violation_description': row[12],
        'critical_flag': row[13],
        'score': row[14],
        'grade': row[15],
        'grade_date': row[16],
        'record_date': row[17],
        'inspection_type': row[18]
    }

def build_query(params):
    query = 'SELECT * FROM restaurant'
    grades = ("A", "B", "C","D", "E", "F")
    where_clauses = []
    if params.get('min_grade') == 'A':
        where_clauses.append('grade=="A"')
    elif params.get('min_grade'):
        where_clauses.append('grade in {}'.format(grades[0:grades.index(params['min_grade'])+1]))

    if params.get('cuisine_description'):
        where_clauses.append('cuisine_description="%s"' % params['cuisine_description'])


    if where_clauses:
        where_clauses_string = ' AND '.join(where_clauses)
        return '{} where {} limit {}'.format(query, where_clauses_string, params['limit'])
    else:
        return '{} limit {}'.format(query, params['limit'])
