import math
import random
import copy

tree = {
    'ANTLR':
    {
        'M':
        {
            'MAX':
            {
                'SVG': 0,
                'TEXT': 1
            },
            'PERL': 2,
            'REXX':
            {
                'JULIA': 3,
                'ATS': 4
            }
        },
        'LIMBO':
        {
            'JULIA': 5,
            'ATS': 6
        },
        'AWK': 7
    },
    'STAN': 8,
    'DART':
    {
        'MAX':
        {
            'M': 9,
            'LIMBO': 10,
            'AWK': 11
        },
        'PERL': 12,
        'REXX': 13
    }
}

def run(tree, key, current):

    if tree.get(key[current], None) is not None:
        if type(tree[key[current]]) == int:
            return tree[key[current]]
        return run(tree[key[current]], key, current + 1)


def main(path):
    z = math.factorial(len(path))
    truepath = []
    while len(truepath) != z:
        tr = copy.copy(path)
        random.shuffle(tr)
        if tr not in truepath:
            truepath.append(tr)
    for i in range(z): #Проход по всем путям
        a = run(tree, truepath[i], 0)
        if a is not None:
            break
    return a

            

      


    

print(main(['TEXT', 'M', 'ANTLR', 'JULIA', 'MAX']))

print(main(['TEXT', 'LIMBO', 'DART', 'JULIA', 'REXX']))
