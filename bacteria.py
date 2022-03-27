complements = {"A": "T", "T": "A", "C": "G", "G": "C"}

def get_complement(original):
    return "".join(complements[x] for x in original)

def add_space(string, comp=False):
    if comp:
        return " ".join([string[:-1], string[-1:]])
    return " ".join([string[:1], string[1:]])

def extract(_strand, _site, _replacement):
    return _strand.replace(_site, _replacement, 1).split()

def cut(_strand, _site, _cuts, right=False):
    if right:
        return [x[::-1] for x in extract(_strand[::-1], _site[::-1], _cuts[_site][::-1])]
    return extract(_strand, _site, _cuts[_site])

def identity(x):
    return x

def cut_gfp(_strand, _l_site, _r_site, _cuts):
    remain = cut(_strand, _l_site, _cuts)[1]
    return cut(remain, _r_site, _cuts, right=True)[1]

def print_cuts(_strand, _p_site, _gfp, _l_site, _r_site, _comp=False, foo=lambda x: x):
    strand, p_site, gfp, l_site, r_site = (foo(x) for x in [_strand, _p_site, _gfp, _l_site, _r_site])
    p_cuts = {p_site: add_space(p_site, comp=_comp)}
    strands = cut(strand, p_site, p_cuts)
    g_cuts = {x: add_space(x, comp=_comp) for x in [l_site, r_site]}
    short_gfp = cut_gfp(gfp, l_site, r_site, g_cuts)
    print(strands[0] + short_gfp + strands[1])


with open(input().strip(), 'r') as f:
    original = f.readline().strip()
    p_site = f.readline().strip()
    gfp = f.readline().strip()
    l_site, r_site = f.readline().strip().split()

for f, comp in zip([identity, get_complement], [False, True]):
    print_cuts(original, p_site, gfp, l_site, r_site, _comp=comp, foo=f)
