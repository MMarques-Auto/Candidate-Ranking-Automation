import pandas as pd

#Iniciar com tratamento de dados, vamos limpar a planilha
df = pd.read_csv('Candidatos.csv')
df['Skill'] = df['Skill'].str.strip()
df['Skill'] = df['Skill'].str.upper()

df = df.dropna(subset=['Pretensao'])

df['Experiencia'] = df['Experiencia'].fillna(df['Experiencia'].median())
#tratamento de dados concluido

#criação da senioridade, separando juniors plenos e seniors
def calc_nivel(anos):
    if anos > 8:
        return "Senior"
    elif anos < 3:
        return "Junior"
    else:
        return "Pleno"

df['Nivel'] = df['Experiencia'].apply(calc_nivel)
#fim da criação e implementação da senioridade

#criando tabela agrupada por localização
aprovados = df[df['Status_Entrevista'] == 'Aprovado']

relatorio_final = aprovados.groupby('Localizacao').agg({
    'Pretensao': 'mean',
    'Experiencia': 'sum'
})

print(df)
print("\n\n\n")
print("--- Resultado do groupby ---")
print(relatorio_final)

relatorio_final.to_csv('Relatório_Candidatos_Europa;csv')
print("\nRelatório exportado com sucesso!")