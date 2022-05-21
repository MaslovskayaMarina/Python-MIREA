import math
import random
import copy

tree = {
    2014:
    {
        1993:
        {
            1977: 3,
            1997:
            {
                'RAGEL': 0,
                'RUBY': 1,
                'GO': 2
            }

        },
        1977: 4
    },
    1970: 10,
    1984:
    {
        1977: 9,
        1993:
        {
            'RAGEL':
            {
                1997: 5,
                1977: 6
            },
            'RUBY': 7,
            'GO': 8
        }
    }
}


def run(tree, key, current):

    if tree.get(key[current], None) is not None:
        if type(tree[key[current]]) == int:
            return tree[key[current]]
        return run(tree[key[current]], key, current + 1)


def main(path):
    z = math.factorial(len(set(path)))
    truepath = []
    while len(truepath) != z:
        tr = copy.copy(path)
        random.shuffle(tr)
        if tr not in truepath:
            truepath.append(tr)
    for i in range(z):
        a = run(tree, truepath[i], 0)
        if a is not None:
            break
    return a

            

      


    

print(main([1997, 1984, 1977, 'RAGEL', 2014]))

print(main([1997, 1984, 1993, 'GO', 1959]))
