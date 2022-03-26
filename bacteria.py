complements = {"A": "T", "T": "A", "C": "G", "G": "C"}

def get_complement(original):
    return "".join(complements[x] for x in original)

def add_space(string, comp=False):
    if comp:
        return " ".join([string[:-1], string[-1:]])
    return " ".join([string[:1], string[1:]])

def extract(_strand, _site, _replacement):
    return _strand.replace(_site, _replacement, 1).split()[1]

def cut(_strand, _site, _cuts, right=False):
    if right:
        return extract(_strand[::-1], _site[::-1], _cuts[_site][::-1])[::-1]
    return extract(_strand, _site, _cuts[_site])

def identity(x):
    return x

def print_cuts(_strand, _l_site, _r_site, _comp=False, foo=lambda x: x):
    strand, l_site, r_site = (foo(x) for x in [_strand, _l_site, _r_site])
    cuts = {x: add_space(x, comp=_comp) for x in [l_site, r_site]}
    remain = cut(strand, l_site, cuts)
    print(cut(remain, r_site, cuts, right=True))


original = input()
l_site, r_site = input().split()

for f, comp in zip([identity, get_complement], [False, True]):
    print_cuts(original, l_site, r_site, _comp=comp, foo=f)
