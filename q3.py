# ## Questão 3
#
# Dado uma sequência de números inteiros, uma trinca a[i], a[j], a[k] é perfeita se:
#
# * a[i] < a[j] < a[k]
# * a[j] - a[i] = a[k] - a[j] = d
#
# Dado um valor de ``d``, você deve encontrar a quantidade de trincas perfeitas.
#
# ### Exemplo
#
# Para a entrada:
#
# ```
# arr = [1, 2, 4, 5, 7, 8, 10]
# d = 3
# ```
#
# A saída deve ser:
#
# ```
# 3
# ```
#
# Isso porque existem apenas três trincas perfeitas:
#
# * (1, 4, 7)
# * (2, 5, 8)
# * (4, 7, 10)
#
# Para obter a nota máxima dessa questão, não deve-se utilizar nenhuma função pronta do Python.

def q3(arr, d):
    tri=[]
    for k in arr:
        a=[]
        if((k+d) in arr):
            if (k+(2*d)) in arr:
                a.append(k)
                a.append(k+d)
                a.append(k+(2*d))
                tri.append(a)
    return len(tri)


if __name__ == '__main__':
    print(q3([1, 2, 4, 5, 7, 8, 10], 3))
