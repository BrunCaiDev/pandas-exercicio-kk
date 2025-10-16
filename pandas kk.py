# 1)
import pandas as pd


funcionarios = {
    "nome": [
        "Ana Souza", "Bruno Lima", "Carla Ferreira", "Diego Santos", "Eduarda Nascimento",
        "Felipe Almeida", "Giovana Ramos", "Henrique Costa", "Isabela Araujo", "João Pereira",
        "Karina Oliveira", "Lucas Rodrigues", "Mariana Machado", "Nathan Silva", "Olívia Barbosa"
    ],
    "unidade": [
        2, 1, 3, 2, 1,
        3, 1, 2, 3, 1,
        2, 3, 1, 3, 2
    ],
    "escala_noturna": [
        False, True, False, True, False,
        True, False, True, False, True,
        False, True, False, True, False
    ],
    "vendas": [
        18754.32, 24321.89, 19876.45, 27543.22, 15789.66,
        29123.10, 22345.99, 26789.40, 19456.78, 28345.55,
        17654.12, 23876.99, 20543.70, 29654.88, 18321.44
    ]
}
# 2)
df = pd.DataFrame(funcionarios)


# 3)-----------------------------
# dados = df.info()

# 4)---------------------------------
# df['unidade'].value_counts()


# 5)-------------------------------------
# df['escala_noturna'].value_counts()



# 6) ---------------------------------------
# lista = df[df['nome'] == "Henrique Costa"]
# lista




# 7) -----------------------------------
# lista = df[df['vendas'] < 20000]
# lista



















