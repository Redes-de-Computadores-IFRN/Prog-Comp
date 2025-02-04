'''
   EXEMPLO 02:
   A partir do código do Exemplo 01, faça as seguintes alterações:

   a) Ao sair do laço, informe quantos nomes há na lista;
   b) Caso o nome digitado após sair do laço exista na lista, 
      informe em qual posição ele está.
'''
nomes = [ ]

while True:
    n = input('Digite os nomes: ').upper()

    if n == 'FIM': break

    nomes.append(n)

print(f'Há {len(nomes)} nomes na Lista')

solicite = input('Digite um nome para consulta: ').upper()

if solicite in nomes:
    print(f'{solicite}')
else:
    print('Não consta.')

