
controle = [{

        "cadastro": "Alex Silva",
        "idade": 30 ,
        "altura em cm." : 180, 
        "esta ativo?": True,
        "avaliacoes" : [9.3, 7.7, 4.3],
        "possui alguma doenca ou impossibilidade fisica?" : False},
        {
        "cadastro": "ana claudia",
        "idade": 28 ,
        "altura em cm." : 175, 
        "esta ativo?": False,
        "avaliacoes" : [5.3, 2.9, 9.9],
        "possui alguma doenca ou impossibilidade fisica?" : True,    
        },
        {
        "cadastro": "gabriel freitas",
        "idade": 17 ,
        "altura em cm." : 168, 
        "esta ativo?": True,
        "avaliacoes" : [9.7, 8.2, 10.0],
        "possui alguma doenca ou impossibilidade fisica?" : False,
        },
        {
        "cadastro": "guilherme oliveira",
        "idade": 21 ,
        "altura em cm." : 175, 
        "esta ativo?": True,
        "avaliacoes" : [10.0, 10.0, 10.0],
        "possui alguma doenca ou impossibilidade fisica?" : False
        }]

for aluno in controle:
    print("cadastro:", aluno["cadastro"])
    print("idade:", aluno["idade"])
    print("altura em cm:", aluno["altura em cm."])
    print("está ativo?:", aluno["esta ativo?"])
    print("avaliações:", aluno["avaliacoes"])
    print("doença ou impossibilidade fisica:", aluno["possui alguma doenca ou impossibilidade fisica?"])
    print("_" * 40)

    def controle(aluno):
        ativo = [aluno for aluno in controle if aluno['esta ativo?']]
        return ativo
    
    def calcular_media(avaliacoes):
        return sum(avaliacoes) / len(avaliacoes)
    print(calcular_media)