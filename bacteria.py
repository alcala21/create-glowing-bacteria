restrictases = ("CTGCAG", "GACGTC")
cuts = {"CTGCAG": "C TGCAG", "GACGTC": "GACGT C"}
dna_cuts = {x: y.replace(x, cuts[x]) for x, y in zip(restrictases, input().split())}
for rest in restrictases:
    print(dna_cuts[rest])
