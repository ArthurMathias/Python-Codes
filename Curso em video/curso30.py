from datetime import date

print("Ano Bissexto")
print("-" * 20)

ano = int(input("Qual ano quer analisar? Digite 0 para analisar o ano atual: "))
if ano == 0:
    ano = date.today().year

if (ano % 4 == 0 and ano % 100 != 0) or ano % 400 == 0:
    print(f"{ano} é bissexto!")
else:
    print(f"{ano} não é bissexto.")
