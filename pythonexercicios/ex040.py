print('MEDIA DO ALUNO')
nota1 = float(input('Qual a primeira nota?'))
nota2 = float(input('Qual a segunda nota?'))
media = (nota1 + nota2) / 2
if media < 5.0:
    print('Sua média foi {}, você está reprovado'.format(media))
elif media >= 5.0 and media <= 6.9:
    print('Sua média foi {}, você está de recuperação'.format(media))
elif media >= 7:
    print('Sua média foi {}, você está aprovado'.format(media))

