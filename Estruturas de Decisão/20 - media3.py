nota_1 = float(input('Digite a primeira nota: '))
nota_2 = float(input('Digite a segunda nota: '))
nota_3 = float(input('Digite a terceira nota: '))

media = (nota_1 + nota_2 + nota_3) / 3

if media < 7:
    print(f'O aluno terminou com a média {media:.1f}, portanto sua situação é de REPROVADO!')
elif 7 <= media < 10:
    print(f'O aluno terminou com a média {media:.1f}, portanto sua situação é de APROVADO!')
elif media == 10:
    print(f'O aluno terminou com a média {media:.1f}, portanto sua situação é de APROVADO COM NOTA MÁXIMA!')
