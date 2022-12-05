# ## Questão 4
#
# Você receberá uma string em [CamelCase](https://en.wikipedia.org/wiki/CamelCase). Ela possuí as seguintes propriedades:
#
# * É a concatenação de uma ou mais palavras, onde a primeira letra de cada palavra é maiúscula, e as demais são
#   minúsculas.
# * Não contém espaços, números ou caracteres especiais.
#
# Você deverá retornar o número de palavras na string.
#
# ### Exemplo
#
# Para a entrada:
#
# ```
# hexaVemEsseAno
# ```
#
# A saída deve ser:
#
# ```
# 4
# ```
#
# Isso porque a string possui 4 palavras: ``hexa``, ``Vem``, ``Esse`` e ``Ano``.
#
# Para obter a nota máxima dessa questão, não deve-se utilizar nenhuma função pronta do Python.

def q4(s):
    x=str(input('palavra:'))
lis=[]
numero=1
pala=('Q','W','E','R','T','Y','U','I','O','P','A','S','D','F','G','H','J','K','L','Z','X','C','V','B','N','M')
for y in range(len(x)):
    lis.append(x[y])
    
for q in range(len(lis)):
    for w in range(len(pala)):
        if lis[q]==pala[w]:
            numero=numero+1
            
#print(f'há {numero} palavras')

    return numer


if __name__ == '__main__':
    print(q4('hexaVemEsseAno'))
