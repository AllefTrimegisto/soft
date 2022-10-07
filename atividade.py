nome = input("Digite seu nome \n")

nota1 = float(input("Digite a primeira nota \n"))

nota2 = float(input("Digite a segunda nota \n"))

faltas = int(input("Digite a quantidade de faltas do aluno \n"))

media = (nota1 + nota2)/2


    
if media >= 7: 
    print("Sua média foi " + str(media) + " Aprovado")
    
else:
        print("Sua média foi " + str(media) + " Reprovado")
        
if faltas > 3:
        print("O aluno foi Reprovado")
