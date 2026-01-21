import pandas as pd

df = pd.read_csv('candidatos.csv')

filtro = (df['Experiencia_Anos'] >= 3) & (df['Linguagem'] == 'Python') & (df['Pretensao_Salarial'] <= 60000)
bons_candidatos = df[filtro]

print("--- Candidatos No Orçamento ---")
print(bons_candidatos[['Nome', 'Pretensao_Salarial']])

media = bons_candidatos['Pretensao_Salarial'].mean()
print(f"\nA média de pretenção salarial dos candidatos bons é: £{media:.2f}")