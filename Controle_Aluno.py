
controle = [{

        "cadastro": "Alex Silva",
        "idade": 30 ,
        "altura em cm." : 170, 
        "esta ativo?": True,
        "avaliacoes" : [9.3, 7,7, 4,3],
        "possui alguma doenca ou impossibilidade fisica?" : False} 
]
for "cadastro" in controle: str 
for "idade" in controle: int
for "altura em cm" in controle: int
for "esta ativo?" in controle: bool
for "avaliacoes" in controle: float
for "possui alguma doenca ou impossibilidade fisica?" in controle: bool


print(type(controle["cadastro"]))   # str
print(type(controle["altura_cm"]))  # int
print(type(controle["avaliacoes"])) # list
print(type(controle))               # dict
print(type(controle["ativo"]))      # bool

# controle_aluno()