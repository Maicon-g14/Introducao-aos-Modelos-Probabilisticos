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

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
import copy

import numpy as np

comp_a = 'dados_grupo_7_comp_A'
comp_b = 'dados_grupo_7_comp_B'


# wage_increase_a = 'dados_grupo_7_Incremento_salario_comp_A'
# wage_increase_b = 'dados_grupo_7_Incremento_salario_comp_B'


def csv_loader(path):
    # Carrega dados do csv em dicionario
    data = ''
    try:
        data = pd.read_csv('data/' + path + '.csv', index_col=0)

    except FileNotFoundError:
        print(path, "nao encontrado!")

    return data


def write_on_disk(data):
    pass


def create_table_gender_education(data):
    gender_education_table = {"prim": {"masc": 0, "fem": 0, "total": 0}, "sec": {"masc": 0, "fem": 0, "total": 0},
                              "terc": {"masc": 0, "fem": 0, "total": 0}, "total": {"masc": 0, "fem": 0, "total": 0}}
    gender_education_raw = data[['Sexo', 'Educ']].to_dict()

    for i in gender_education_raw["Educ"]:
        if gender_education_raw["Educ"][i] == "prim":
            if gender_education_raw["Sexo"][i] == "masc":
                gender_education_table["prim"]["masc"] += 1
                gender_education_table["total"]["masc"] += 1
            else:
                gender_education_table["prim"]["fem"] += 1
                gender_education_table["total"]["fem"] += 1
            gender_education_table["prim"]["total"] += 1
        elif gender_education_raw["Educ"][i] == "sec":
            if gender_education_raw["Sexo"][i] == "masc":
                gender_education_table["sec"]["masc"] += 1
                gender_education_table["total"]["masc"] += 1
            else:
                gender_education_table["sec"]["fem"] += 1
                gender_education_table["total"]["fem"] += 1
            gender_education_table["sec"]["total"] += 1
        else:
            if gender_education_raw["Sexo"][i] == "masc":
                gender_education_table["terc"]["masc"] += 1
                gender_education_table["total"]["masc"] += 1
            else:
                gender_education_table["terc"]["fem"] += 1
                gender_education_table["total"]["fem"] += 1
            gender_education_table["terc"]["total"] += 1
        gender_education_table["total"]["total"] += 1

    return gender_education_table


def create_table_gender_wage(data):
    gender_wage_table = {}
    gender_wage_table_raw = {"masc": [], "fem": []}
    salary_range = [0, 4, 8, 12, 16, 20, 24]
    gender_wage_raw = data[['Sexo', 'Sal']].to_dict()

    for r in range(1, len(salary_range)):
        gender_sub_table = {"masc": 0, "fem": 0}
        for i in gender_wage_raw["Sexo"]:
            if salary_range[r - 1] <= gender_wage_raw["Sal"][i] < salary_range[r]:
                if gender_wage_raw["Sexo"][i] == "masc":
                    gender_sub_table["masc"] += 1
                    gender_wage_table_raw["masc"].append(gender_wage_raw["Sal"][i])
                else:
                    gender_sub_table["fem"] += 1
                    gender_wage_table_raw["fem"].append(gender_wage_raw["Sal"][i])

        gender_wage_table["(" + str(salary_range[r - 1]) + ", " + str(salary_range[r]) + "]"] = gender_sub_table

    return gender_wage_table, gender_wage_table_raw


def create_table_education_wage(data):
    education_wage_table = {}
    education_wage_table_raw = {"prim": [], "sec": [], "terc": []}
    salary_range = [0, 4, 8, 12, 16, 20, 24]
    education_wage_raw = data[['Educ', 'Sal']].to_dict()

    for r in range(1, len(salary_range)):
        education_sub_table = {"prim": 0, "sec": 0, "terc": 0}
        for i in education_wage_raw["Educ"]:
            if salary_range[r - 1] <= education_wage_raw["Sal"][i] < salary_range[r]:
                if education_wage_raw["Educ"][i] == "prim":
                    education_sub_table["prim"] += 1
                    education_wage_table_raw["prim"].append(education_wage_raw["Sal"][i])
                elif education_wage_raw["Educ"][i] == "sec":
                    education_sub_table["sec"] += 1
                    education_wage_table_raw["sec"].append(education_wage_raw["Sal"][i])
                else:
                    education_sub_table["terc"] += 1
                    education_wage_table_raw["terc"].append(education_wage_raw["Sal"][i])

        education_wage_table["(" + str(salary_range[r - 1]) + ", " + str(salary_range[r]) + "]"] = education_sub_table

    return education_wage_table, education_wage_table_raw


def create_table_gender_role(data):
    gender_role_table = {"gerencial": {"masc": 0, "fem": 0, "total": 0}, "outro": {"masc": 0, "fem": 0, "total": 0},
                         "total": {"masc": 0, "fem": 0, "total": 0}}
    gender_role_raw = data[['Sexo', 'cargo']].to_dict()

    for i in gender_role_raw["cargo"]:
        if gender_role_raw["cargo"][i] == "gerencial":
            if gender_role_raw["Sexo"][i] == "masc":
                gender_role_table["gerencial"]["masc"] += 1
                gender_role_table["total"]["masc"] += 1
            else:
                gender_role_table["gerencial"]["fem"] += 1
                gender_role_table["total"]["fem"] += 1
            gender_role_table["gerencial"]["total"] += 1
        else:
            if gender_role_raw["Sexo"][i] == "fem":
                gender_role_table["outro"]["fem"] += 1
                gender_role_table["total"]["fem"] += 1
            else:
                gender_role_table["outro"]["masc"] += 1
                gender_role_table["total"]["masc"] += 1
            gender_role_table["outro"]["total"] += 1
        gender_role_table["total"]["total"] += 1

    return gender_role_table


def create_table_role_wage(data):
    role_wage_table = {
        "gerencial": {"(0, 4]": 0, "(4, 8]": 0, "(8, 12]": 0, "(12, 16]": 0, "(16, 20]": 0, "(20, 24]": 0},
        "outro": {"(0, 4]": 0, "(4, 8]": 0, "(8, 12]": 0, "(12, 16]": 0, "(16, 20]": 0, "(20, 24]": 0}}
    role_wage_table_raw = {"gerencial": [], "outro": []}
    cargos = ["gerencial", "outro"]
    role_wage_raw = data[['cargo', 'Sal']].to_dict()

    for cargo in cargos:
        for i in role_wage_raw["cargo"]:
            if role_wage_raw["cargo"][i] == cargo:
                if 0 <= role_wage_raw["Sal"][i] < 4:
                    role_wage_table[cargo]["(0, 4]"] += 1
                elif 4 <= role_wage_raw["Sal"][i] < 8:
                    role_wage_table[cargo]["(4, 8]"] += 1
                elif 8 <= role_wage_raw["Sal"][i] < 12:
                    role_wage_table[cargo]["(8, 12]"] += 1
                elif 12 <= role_wage_raw["Sal"][i] < 16:
                    role_wage_table[cargo]["(12, 16]"] += 1
                elif 16 <= role_wage_raw["Sal"][i] < 20:
                    role_wage_table[cargo]["(16, 20]"] += 1
                else:
                    role_wage_table[cargo]["(20, 24]"] += 1
                role_wage_table_raw[cargo].append(role_wage_raw["Sal"][i])

    return role_wage_table, role_wage_table_raw


def percentage_by_columns(table):
    percentage_table = copy.deepcopy(table)

    for i in percentage_table["total"]:
        for j in percentage_table:
            for k in percentage_table[j]:
                if k == i:
                    # print(table[j][k], end=" -> ")
                    percentage_table[j][k] = round((percentage_table[j][k] / percentage_table["total"][i]) * 100)
                    # print(table[j][k])

    return percentage_table


def show_table(company, item_name):
    table = company[item_name]
    print(table)
    print(5 * " " + company["name"] + " " + item_name + "\n" + (len(company["name"]) + len(item_name) + 11) * "-",
          end="\n            ")

    header = list(list(table.items())[0][1].keys())

    for i in header:
        print(i, end=" ")
    print()
    for j in table:
        aux = j
        while len(aux) < 11:
            aux += " "
        print(aux, end=" ")
        for k in table[j]:
            aux = str(table[j][k])
            while len(aux) < len(k):
                aux = " " + aux
            print(aux, end=" ")
        print()
    print()


def show_box_plot(table, item_name, x_labels, x_label, y_label="Salário"):
    wage = []
    ticks = [4, 8, 12, 16, 20, 24]
    for i in table:
        wage.append(table[i])

    fig, ax = plt.subplots()
    ax.set_yticks(ticks)
    #ax.set_xticks([1, 2])
    ax.set_xticklabels(x_labels)

    plt.xlabel(x_label, fontsize=12)
    plt.ylabel(y_label, fontsize=12)
    ax.set_title(item_name)
    ax.boxplot(wage)
    plt.show()


def main():
    company_a = {"name": "Companhia A"}
    company_b = {"name": "Companhie B"}

    data_a = csv_loader(comp_a)
    data_b = csv_loader(comp_b)
    # data_wage_a = csv_loader(wage_increase_a)
    # data_wage_b = csv_loader(wage_increase_b)

    company_a["gender_education"] = create_table_gender_education(data_a)
    company_a["gender_education_percent"] = percentage_by_columns(company_a["gender_education"])
    company_b["gender_education"] = create_table_gender_education(data_b)
    company_b["gender_education_percent"] = percentage_by_columns(company_b["gender_education"])
    # show_table(company_a, "gender_education")
    # show_table(company_b, "gender_education")
    #show_table(company_a, "gender_education_percent")
    #show_table(company_b, "gender_education_percent")

    company_a["gender_wage"], company_a["gender_wage_raw"] = create_table_gender_wage(data_a)
    company_b["gender_wage"], company_b["gender_wage_raw"] = create_table_gender_wage(data_b)
    # show_table(company_a, "gender_wage")
    # show_table(company_b, "gender_wage")
    # show_box_plot(company_a["gender_wage_raw"], "Companhia A", ["Masculino", "Feminino"], "Gênero")
    # show_box_plot(company_b["gender_wage_raw"], "Companhia B", ["Masculino", "Feminino"], "Gênero")

    company_a["education_wage"], company_a["education_wage_raw"] = create_table_education_wage(data_a)
    company_b["education_wage"], company_b["education_wage_raw"] = create_table_education_wage(data_b)
    # show_table(company_a, "education_wage")
    # show_table(company_b, "education_wage")
    # show_box_plot(company_a["education_wage_raw"], "Companhia A", ["Primaria", "Secundária", "Terceária"], "Nível de Escolaridade")
    # show_box_plot(company_b["education_wage_raw"], "Companhia B", ["Primaria", "Secundária", "Terceária"], "Nível de Escolaridade")

    company_a["gender_role"] = create_table_gender_role(data_a)
    company_a["gender_role_percent"] = percentage_by_columns(company_a["gender_role"])
    company_b["gender_role"] = create_table_gender_role(data_b)
    company_b["gender_role_percent"] = percentage_by_columns(company_b["gender_role"])
    # show_table(company_a, "gender_role")
    # show_table(company_b, "gender_role")
    #show_table(company_a, "gender_role_percent")
    #show_table(company_b, "gender_role_percent")

    company_a["role_wage"], company_a["role_wage_raw"] = create_table_role_wage(data_a)
    company_b["role_wage"], company_b["role_wage_raw"] = create_table_role_wage(data_b)
    # show_table(company_a, "role_wage")
    # show_table(company_b, "role_wage")
    # show_box_plot(company_a["role_wage_raw"], "Companhia A", ["Gerencial", "Outro"], "Cargo")
    # show_box_plot(company_b["role_wage_raw"], "Companhia B", ["Gerencial", "Outro"], "Cargo")


main()
