# ra221329

'''
2a Parte: Para cada companhia, analise a dependência entre as variáveis.
i) Analise a dependência entre as variáveis sexo e educação.
ii) Analise a dependência entre as variáveis sexo e salário.
iii) Analise a dependência entre as variáveis educação e salário.
iv) Analise a dependência entre as variáveis sexo e cargo.
v) Analise a dependência entre as variáveis cargo e salário.
vi) Escreva as conclusões da análise de dependência.
'''

import pandas as pd
from IPython.display import display, HTML

comp_a = 'dados_grupo_7_comp_A'
comp_b = 'dados_grupo_7_comp_B'
wage_increase_a = 'dados_grupo_7_Incremento_salario_comp_A'
wage_increase_b = 'dados_grupo_7_Incremento_salario_comp_B'


def csv_loader(path):
    # Carrega dados do csv em dicionario
    data = ''
    try:
        data = pd.read_csv('data/' + path + '.csv', index_col=0)

    except FileNotFoundError:
        print(path, "nao encontrado!")

    return data


def create_table_gender_education(data):

    company = data[['Sexo', 'Educ']].value_counts()

    b = data['Sexo'].value_counts()
    for i in b.keys():
        company.loc[(i, "total")] = b[i]

    c = data['Educ'].value_counts()
    for i in c.keys():
        company.loc[("total", i)] = c[i]

    company.loc[("total", "total")] = sum(company["total"].values)

    return company


def percentage_by_columns(table):
    percentage_table = table.copy()

    for i in table.keys():
        percentage_table.loc[(i[0], i[1])] = round((table[i[0]][i[1]]/table[i[0]]["total"])*100)

    return percentage_table


def show_table(table, company_name):
    columns = set([])
    rows = set([])

    for i in table.keys():
        columns.add(i[0])
        rows.add(i[1])

    columns = sorted(columns)
    rows = sorted(rows)

    print(5*" " + company_name + "\n" + 20*"-", end="\n      ")
    for i in columns:
        print(i, end=" ")
    print()

    for i in rows:
        aux = i
        while len(aux) < 5:
            aux += " "
        print(aux, end=" ")

        for j in columns:
            digit = str(table[j][i])
            while len(digit) < 3:
                digit = " " + digit
            print(digit, end="  ")

        print()
    print(20*"-", end="\n\n")


def main():
    company_a = {}
    company_b = {}

    data_a = csv_loader(comp_a)
    data_b = csv_loader(comp_b)
    #data_wage_a = csv_loader(wage_increase_a)
    #data_wage_b = csv_loader(wage_increase_b)

    #print(data_a.head())
    #print(data_a.loc[1])    #comeca do 1
    #print(data_a.iloc[0])   #comeca do 0
    #print(data_a.iloc[0].Sexo)  # comeca do 0
    #print(data_a[['Sexo', 'cargo']])
    #print(data_a.Sexo)  #so a coluna data

    #data["Indexes"] = data["Sexo"].str.find("masc")

    company_a["gender_education"] = create_table_gender_education(data_a)
    company_b["gender_education"] = create_table_gender_education(data_b)

    gender_education_percentage_a = percentage_by_columns(company_a["gender_education"])
    gender_education_percentage_b = percentage_by_columns(company_b["gender_education"])
    show_table(gender_education_percentage_a, "Companhia A")
    show_table(gender_education_percentage_b, "Companhia B")
    #print(company_a)

    #print(data_a)
    #print(data_a.Sal.truncate(axis="Sal"))

    #print(data_a['Sal'].value_counts())

    #print(data_a.Sexo)



    '''

    #dividir faixas salariais

    a_total_cargo_gerencial = 
    a_total_cargo_outro = '''


main()