import pandas as pd

#base de dados bruta
dados_candidatos = {
    'Nome': ['Lucas', 'Ana', 'Roberto', 'Maria', 'Enzo', 'Clara'],
    'Experiencia_Anos': [5, 2, 8, 4, 1, 6],
    'Linguagem': ['Python', 'Java', 'Python', 'Python', 'JS', 'Python'],
    'Pretensao_Salarial': [55000, 48000, 75000, 52000, 40000, 62000],
    'Cidadania_EU': [True, False, False, True, False, True]
}

df = pd.DataFrame(dados_candidatos)

filtro = (df['Experiencia_Anos'] >= 3) & (df['Linguagem'] == 'Python')
bons_candidatos = df[filtro]

print("--- Candidatos Bons ---")
print(bons_candidatos)

media = bons_candidatos['Pretensao_Salarial'].mean()
print(f"\nA média de pretenção salarial dos candidatos bons é: £{media:.2f}")

print(f"\nUtilizando como prioridade a cidadania EU os melhores\nentre os melhores são:\n")
Candidatos_eu = bons_candidatos[bons_candidatos['Cidadania_EU'] == True]
print(Candidatos_eu)