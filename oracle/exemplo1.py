#pip install oracledb

import oracledb

conexao = oracledb.connect(user='pf0313', 
            password='professor#23',
            dsn='oracle.fiap.com.br/orcl')

print(conexao.version)
cursor = conexao.cursor()

cursor.execute('select sysdate from dual')
registro = cursor.fetchone()
print(registro[0])

cursor.execute('select id, nome, crm, especialidade from medico order by id')
registro = cursor.fetchall()
#print(registro)
for med in registro:
    print(med)

cursor.close()
conexao.close()