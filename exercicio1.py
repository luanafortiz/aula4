import datetime
def diasdevida (hoje, nascimento):
    dias = hoje - nascimento
    return dias

hoje = datetime.date(year = 2020,month= 2,day=20)
dia = int(input('em que dia você nasceu '))
mes = int(input('que mes '))
ano = int(input('que ano ')) 
nascimento = datetime.date(ano, mes, dia)
resposta = diasdevida(hoje,nascimento)
print(resposta)
