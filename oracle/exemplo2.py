import oracledb

con = oracledb.connect(user='pf0313', password='professor#23',
        dsn='oracle.fiap.com.br/orcl')
cur = con.cursor()

sql = '''insert into empregado(numero, nome, cargo, departamento, salario,
        data_contratacao) values(:numero, :nome, :cargo, :departamento,
        :salario, to_date(:data_contratacao, 'MM-DD-YYYY'))'''

info = {'numero': 2756, 'nome': 'Manoel Ferreira', 'salario': 5403.90,
        'cargo': 'Diretor acadêmico', 'departamento': 'reitoria',
        'data_contratacao': '10-23-2008'}

cur.execute(sql, info)
con.commit()
cur.close()
con.close()