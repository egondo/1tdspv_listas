import oracledb

con = oracledb.connect(user='pf0313', password='professor#23',
        dsn='oracle.fiap.com.br/orcl')
cur = con.cursor()

sql = '''update empregado set nome=:name, cargo=:jobtitle, 
        departamento=:department, salario=:salary,
        data_contratacao=to_date(:hiring_date, 'YYYY-MM-DD') 
        where numero=:id'''

info = {'id': 1000, 'name': 'Eduardo Kazuaki Gondo', 'salary': 8503,
        'jobtitle': 'Professor mestre', 'department': 'graduação',
        'hiring_date': '2007-12-14'}

cur.execute(sql, info)
con.commit()
cur.close()
con.close()