dias_uteis = int(input("Dias úteis: "))
horas_trabalhadas = float(input("Horas trabalhadas: "))

salario_hora = float(input("Salário hora:"))

jornada_mensal = dias_uteis * 8

valor_hora_extra = 0
if horas_trabalhadas > jornada_mensal:
    hora_extra = horas_trabalhadas - jornada_mensal
    valor_hora_extra = hora_extra * salario_hora * 1.5
    print(f"O valor de hora extra é {valor_hora_extra}")
    horas_trabalhadas = jornada_mensal

salario_total = horas_trabalhadas * salario_hora + valor_hora_extra
print(f"O total a receber será R$ {salario_total}")