import pandas as pd

#base de dados para vagas EU
vagas = {
    'Cargo': ['Data Analyst', 'python Dev', 'Data Engineer', 'Junior Dev', 'Senior Python'],
    'Salario_Anual': [45000, 52000, 60000, 38000, 85000],
    'Pais': ['Alemanha', 'holanda', 'Alemanha', 'Portugal', 'Irlanda'],
    'Remoto': [True, True, False, False, True]
}

#Transformando em DataFrame
df = pd.DataFrame(vagas)

#filtro
filtro = (df['Salario_Anual'] >= 45000) & (df['Remoto'] == True)
vagas_top = df[filtro]

#resultados
print("--- Buscador de vagas Euro 2026 ---")
print(vagas_top)

#calculo de salário médio da vagas top
media = vagas_top['Salario_Anual'].mean()
print(f"\nA média salarial das melhores vagas é: £{media:.2f}")