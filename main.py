import matplotlib
import matplotlib.pyplot as plt
import pandas as pd
import copy
import statistics

matplotlib.use('TkAgg')

comp_a = 'dados_grupo_7_comp_A'
comp_b = 'dados_grupo_7_comp_B'


def csv_loader(path):
    # Carrega dados do CSV
    full_path = 'data/' + path + '.csv'
    data = ''

    try:
        data = pd.read_csv(full_path, index_col=0)

    except FileNotFoundError:
        print(full_path, "nao encontrado!")

    return data


def create_table_gender_education(data):
    gender_education_table = {"prim": {"masc": 0, "fem": 0, "total": 0}, "sec": {"masc": 0, "fem": 0, "total": 0},
                              "terc": {"masc": 0, "fem": 0, "total": 0}, "total": {"masc": 0, "fem": 0, "total": 0}}
    gender_education_raw = data[['Sexo', 'Educ']].to_dict()

    for education_level in gender_education_raw["Educ"]:
        if gender_education_raw["Educ"][education_level] == "prim":
            if gender_education_raw["Sexo"][education_level] == "masc":
                gender_education_table["prim"]["masc"] += 1
                gender_education_table["total"]["masc"] += 1
            else:
                gender_education_table["prim"]["fem"] += 1
                gender_education_table["total"]["fem"] += 1

            gender_education_table["prim"]["total"] += 1

        elif gender_education_raw["Educ"][education_level] == "sec":
            if gender_education_raw["Sexo"][education_level] == "masc":
                gender_education_table["sec"]["masc"] += 1
                gender_education_table["total"]["masc"] += 1
            else:
                gender_education_table["sec"]["fem"] += 1
                gender_education_table["total"]["fem"] += 1

            gender_education_table["sec"]["total"] += 1

        else:
            if gender_education_raw["Sexo"][education_level] == "masc":
                gender_education_table["terc"]["masc"] += 1
                gender_education_table["total"]["masc"] += 1
            else:
                gender_education_table["terc"]["fem"] += 1
                gender_education_table["total"]["fem"] += 1

            gender_education_table["terc"]["total"] += 1

        gender_education_table["total"]["total"] += 1

    return gender_education_table


def create_table_gender_income(data):
    gender_income_table = {"(0, 4]": {"masc": 0, "fem": 0, "total": 0}, "(4, 8]": {"masc": 0, "fem": 0, "total": 0},
                           "(8, 12]": {"masc": 0, "fem": 0, "total": 0}, "(12, 16]": {"masc": 0, "fem": 0, "total": 0},
                           "(16, 20]": {"masc": 0, "fem": 0, "total": 0}, "(20, 24]": {"masc": 0, "fem": 0, "total": 0},
                           "total": {"masc": 0, "fem": 0, "total": 0}}
    gender_income_table_raw = {"masc": [], "fem": []}
    salary_range = [0, 4, 8, 12, 16, 20, 24]
    gender_income_raw = data[['Sexo', 'Sal']].to_dict()

    for income in range(1, len(salary_range)):
        current_range = "(" + str(salary_range[income - 1]) + ", " + str(salary_range[income]) + "]"
        for gender in gender_income_raw["Sexo"]:
            if salary_range[income - 1] <= gender_income_raw["Sal"][gender] < salary_range[income]:
                if gender_income_raw["Sexo"][gender] == "masc":
                    gender_income_table[current_range]["masc"] += 1
                    gender_income_table_raw["masc"].append(gender_income_raw["Sal"][gender])
                    gender_income_table["total"]["masc"] += 1

                else:
                    gender_income_table[current_range]["fem"] += 1
                    gender_income_table_raw["fem"].append(gender_income_raw["Sal"][gender])
                    gender_income_table["total"]["fem"] += 1

                gender_income_table[current_range]["total"] += 1
                gender_income_table["total"]["total"] += 1

    return gender_income_table, gender_income_table_raw


def create_table_education_income(data):
    education_income_table = {"(0, 4]": {"prim": 0, "sec": 0, "terc": 0, "total": 0},
                              "(4, 8]": {"prim": 0, "sec": 0, "terc": 0, "total": 0},
                              "(8, 12]": {"prim": 0, "sec": 0, "terc": 0, "total": 0},
                              "(12, 16]": {"prim": 0, "sec": 0, "terc": 0, "total": 0},
                              "(16, 20]": {"prim": 0, "sec": 0, "terc": 0, "total": 0},
                              "(20, 24]": {"prim": 0, "sec": 0, "terc": 0, "total": 0},
                              "total": {"prim": 0, "sec": 0, "terc": 0, "total": 0}}
    education_income_table_raw = {"prim": [], "sec": [], "terc": []}
    salary_range = [0, 4, 8, 12, 16, 20, 24]
    education_income_raw = data[['Educ', 'Sal']].to_dict()

    for income in range(1, len(salary_range)):
        current_range = "(" + str(salary_range[income - 1]) + ", " + str(salary_range[income]) + "]"
        for education_level in education_income_raw["Educ"]:
            if salary_range[income - 1] <= education_income_raw["Sal"][education_level] < salary_range[income]:
                if education_income_raw["Educ"][education_level] == "prim":
                    education_income_table[current_range]["prim"] += 1
                    education_income_table["total"]["prim"] += 1
                    education_income_table_raw["prim"].append(education_income_raw["Sal"][education_level])

                elif education_income_raw["Educ"][education_level] == "sec":
                    education_income_table[current_range]["sec"] += 1
                    education_income_table["total"]["sec"] += 1
                    education_income_table_raw["sec"].append(education_income_raw["Sal"][education_level])

                else:
                    education_income_table[current_range]["terc"] += 1
                    education_income_table["total"]["terc"] += 1
                    education_income_table_raw["terc"].append(education_income_raw["Sal"][education_level])

                education_income_table[current_range]["total"] += 1
                education_income_table["total"]["total"] += 1

    return education_income_table, education_income_table_raw


def create_table_gender_role(data):
    gender_role_table = {"gerencial": {"masc": 0, "fem": 0, "total": 0}, "outro": {"masc": 0, "fem": 0, "total": 0},
                         "total": {"masc": 0, "fem": 0, "total": 0}}
    gender_role_raw = data[['Sexo', 'cargo']].to_dict()

    for role in gender_role_raw["cargo"]:
        if gender_role_raw["cargo"][role] == "gerencial":
            if gender_role_raw["Sexo"][role] == "masc":
                gender_role_table["gerencial"]["masc"] += 1
                gender_role_table["total"]["masc"] += 1
            else:
                gender_role_table["gerencial"]["fem"] += 1
                gender_role_table["total"]["fem"] += 1

            gender_role_table["gerencial"]["total"] += 1

        else:
            if gender_role_raw["Sexo"][role] == "fem":
                gender_role_table["outro"]["fem"] += 1
                gender_role_table["total"]["fem"] += 1
            else:
                gender_role_table["outro"]["masc"] += 1
                gender_role_table["total"]["masc"] += 1

            gender_role_table["outro"]["total"] += 1

        gender_role_table["total"]["total"] += 1

    return gender_role_table


def create_table_role_income(data):
    role_income_table = {
        "gerencial": {"(0, 4]": 0, "(4, 8]": 0, "(8, 12]": 0, "(12, 16]": 0, "(16, 20]": 0, "(20, 24]": 0, "total": 0},
        "outro": {"(0, 4]": 0, "(4, 8]": 0, "(8, 12]": 0, "(12, 16]": 0, "(16, 20]": 0, "(20, 24]": 0, "total": 0},
        "total": {"(0, 4]": 0, "(4, 8]": 0, "(8, 12]": 0, "(12, 16]": 0, "(16, 20]": 0, "(20, 24]": 0, "total": 0}}
    role_income_table_raw = {"gerencial": [], "outro": []}
    roles = ["gerencial", "outro"]
    role_income_raw = data[['cargo', 'Sal']].to_dict()

    for role in roles:
        for income in role_income_raw["cargo"]:
            if role_income_raw["cargo"][income] == role:
                if 0 <= role_income_raw["Sal"][income] < 4:
                    role_income_table[role]["(0, 4]"] += 1
                    role_income_table["total"]["(0, 4]"] += 1

                elif 4 <= role_income_raw["Sal"][income] < 8:
                    role_income_table[role]["(4, 8]"] += 1
                    role_income_table["total"]["(4, 8]"] += 1

                elif 8 <= role_income_raw["Sal"][income] < 12:
                    role_income_table[role]["(8, 12]"] += 1
                    role_income_table["total"]["(8, 12]"] += 1

                elif 12 <= role_income_raw["Sal"][income] < 16:
                    role_income_table[role]["(12, 16]"] += 1
                    role_income_table["total"]["(12, 16]"] += 1

                elif 16 <= role_income_raw["Sal"][income] < 20:
                    role_income_table[role]["(16, 20]"] += 1
                    role_income_table["total"]["(16, 20]"] += 1

                else:
                    role_income_table[role]["(20, 24]"] += 1
                    role_income_table["total"]["(20, 24]"] += 1

                role_income_table[role]["total"] += 1
                role_income_table["total"]["total"] += 1

                role_income_table_raw[role].append(role_income_raw["Sal"][income])

    return role_income_table, role_income_table_raw


def mean_of_variances(data):
    variance = {}
    all_elements = []

    for row in data:
        mean = statistics.mean(data[row])
        print("Media " + str(row) + ": %.2f" % mean)

        variance_upper = 0
        for value in data[row]:
            variance_upper += (value - mean) ** 2

        n = len(data[row])
        variance[row] = variance_upper / (n - 1)

        print("Variancia %s: %.2f" % (row, variance[row]))

        all_elements += data[row]

    total_mean = statistics.mean(all_elements)

    variance_total_upper = 0
    for value in all_elements:
        variance_total_upper += (value - total_mean) ** 2

    total_variance = variance_total_upper / (len(all_elements) - 1)

    variance_mean_upper = 0
    for i in variance:
        variance_mean_upper += variance[i] * len(data[i])

    variance_mean = variance_mean_upper / len(all_elements)

    print("Media das variancias: %.2f" % variance_mean)
    association_degree = 1 - (variance_mean / total_variance)
    print("Grau de Associacao: %.2f -> %i%%" % (association_degree, round(association_degree * 100)))


def percentage_by_columns(table):
    # Calcula as porcentagens da tabela
    percentage_table = copy.deepcopy(table)

    for total_column in percentage_table["total"]:
        for row in percentage_table:
            for column in percentage_table[row]:
                if column == total_column:
                    percentage_table[row][column] = round(
                        (percentage_table[row][column] / percentage_table["total"][total_column]) * 100)

    return percentage_table


def pearson_chi_squared(table):
    # Calcula Qui-quadrado de Pearson
    chi_sum = 0

    for row in table:
        for column in table[row]:
            if row != "total" and column != "total":
                chi_sum += ((table[row][column] - table[row]["total"]) ** 2) / table[row]["total"]

    return chi_sum


def show_table(company, item_key, item_name):
    table = company[item_key]
    print(5 * " " + item_name + "\n" + (len(item_name) + 11) * "-", end="\n            ")

    header = list(list(table.items())[0][1].keys())  # Obtem nome das columas

    for column in header:
        print(column, end=" ")
    print()

    for row in table:
        header_row = row
        while len(header_row) < 11:
            header_row += " "

        print(header_row, end=" ")

        for column in table[row]:
            formatted_value = str(table[row][column])
            while len(formatted_value) < len(column):
                formatted_value = " " + formatted_value

            print(formatted_value, end=" ")

        print()
    print()

    qui_quad = item_key + "_qui_quad"
    if qui_quad in company:
        print("Qui-quadrado: %.2f" % (company[qui_quad]), end="\n---\n")


def show_box_plot(table, item_name, x_labels, x_label, y_label="Salário"):
    # Gera e exibe Box Plots
    income = list(table.values())
    ticks = [4, 8, 12, 16, 20, 24]

    fig, ax = plt.subplots()
    ax.set_yticks(ticks)
    ax.set_xticklabels(x_labels)

    plt.xlabel(x_label, fontsize=12)
    plt.ylabel(y_label, fontsize=12)
    ax.set_title(item_name)
    ax.boxplot(income)
    plt.show()


def dependency_analysis_2_1(company, data):
    print(8 * " " + company["name"])
    company["gender_education"] = create_table_gender_education(data)
    company["gender_education_percent"] = percentage_by_columns(company["gender_education"])
    company["gender_education_qui_quad"] = pearson_chi_squared(company["gender_education_percent"])
    show_table(company, "gender_education", "Grau de Escolaridade por Genero")
    show_table(company, "gender_education_percent", "Genero por Grau de Escolaridade %")


def dependency_analysis_2_2(company, data):
    print(8 * " " + company["name"])
    company["gender_income"], company["gender_income_raw"] = create_table_gender_income(data)
    show_table(company, "gender_income", "Renda por Genero")
    mean_of_variances(company["gender_income_raw"])
    show_box_plot(company["gender_income_raw"], company["name"], ["Masculino", "Feminino"], "Gênero")


def dependency_analysis_2_3(company, data):
    print(8 * " " + company["name"])
    company["education_income"], company["education_income_raw"] = create_table_education_income(data)
    show_table(company, "education_income", "Renda por Grau de Escolaridade")
    mean_of_variances(company["education_income_raw"])
    show_box_plot(company["education_income_raw"], company["name"], ["Primaria", "Secundária", "Terceária"],
                  "Nível de Escolaridade")


def dependency_analysis_2_4(company, data):
    print(8 * " " + company["name"])
    company["gender_role"] = create_table_gender_role(data)
    company["gender_role_percent"] = percentage_by_columns(company["gender_role"])
    company["gender_role_qui_quad"] = pearson_chi_squared(company["gender_role_percent"])
    show_table(company, "gender_role", "Genero por Cargo Ocupado")
    show_table(company, "gender_role_percent", "Genero por Cargo Ocupado %")


def dependency_analysis_2_5(company, data):
    print(8 * " " + company["name"])
    company["role_income"], company["role_income_raw"] = create_table_role_income(data)
    show_table(company, "role_income", "Renda por Cargo Ocupado")
    mean_of_variances(company["role_income_raw"])
    show_box_plot(company["role_income_raw"], company["name"], ["Gerencial", "Outro"], "Cargo")


def main():
    company_a = {"name": "Companhia A"}
    company_b = {"name": "Companhia B"}

    data_a = csv_loader(comp_a)
    data_b = csv_loader(comp_b)

    # ------------------1-------------------
    dependency_analysis_2_1(company_a, data_a)
    dependency_analysis_2_1(company_b, data_b)

    # ------------------2-------------------
    dependency_analysis_2_2(company_a, data_a)
    dependency_analysis_2_2(company_b, data_b)

    # ------------------3-------------------
    dependency_analysis_2_3(company_a, data_a)
    dependency_analysis_2_3(company_b, data_b)

    # ------------------4-------------------
    dependency_analysis_2_4(company_a, data_a)
    dependency_analysis_2_4(company_b, data_b)

    # ------------------5-------------------
    dependency_analysis_2_5(company_a, data_a)
    dependency_analysis_2_5(company_b, data_b)


main()
