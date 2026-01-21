import pandas as pd
import requests

df = pd.read_csv('Candidatos.csv')
df['Linguagem'] = df['Linguagem'].str.strip()
df['Linguagem'] = df['Linguagem'].str.capitalize()

#desafio de orçamento

filtro1 = (df['Pretensao_Salarial'] <= 50000) & (df['Cidadania_EU'] == True)
budget = df[filtro1]

print('\n---Budget Challenge---')
print(budget[['Nome', 'Pretensao_Salarial']])

#desafio de Senior

exp = df.sort_values(by='Experiencia_Anos', ascending=False)

print("\n\n---Senior Challenge---")
print(exp[['Nome', 'Experiencia_Anos']])

#desafio de conversão

url = "https://economia.awesomeapi.com.br/last/EUR-BRL"
resposta =  requests.get(url)
moeda = resposta.json()
cot_euro = float(moeda['EURBRL']['bid'])
print("\n\n---BRL Challenge---")
print(f"\nCotação do Euro: R$ {cot_euro:.2f}")
df['PretensaoBRL'] = df['Pretensao_Salarial'] * cot_euro
df['PretensaoBRLM'] = df['PretensaoBRL'] / 12
print(df[['Nome', 'Pretensao_Salarial', 'PretensaoBRL', 'PretensaoBRLM']])

#desafio blacklist

filtro2 = df['Linguagem'] != "Java"
print("\n\n---NoJava Challenge---")
print(df[filtro2])

#Balance and tendency

cont = df['Linguagem'].value_counts()
print(cont)