import csv
import itertools

pairs = {}

partidos = set()

with open('coliga.csv') as csvfile:
    r = csv.reader(csvfile, delimiter=';')
    for row in r:
        coligacao = row[1].split(' / ')
        if len(coligacao) is 1:
            coligacao = [tuple(coligacao*2)]
        else:
            coligacao = itertools.combinations(coligacao, 2)
        candidatos = int(row[2].replace('.', ''))
        for pair in coligacao:
            partidos.add(pair[0])
            partidos.add(pair[1])
            key = tuple(sorted(pair))
            tot_candidatos = pairs.setdefault(key, 0)
            pairs[key] = tot_candidatos + candidatos

partidos = sorted(partidos)
print "".center(7),
for p in partidos:
    print (p or "--").center(7),
print
for p1 in partidos:
    print p1.center(7),
    for p2 in partidos:
        print str(pairs.get((p2, p1)) or pairs.get((p1, p2)) or "--").center(7),
    print
