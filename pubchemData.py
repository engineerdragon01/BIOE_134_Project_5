import csv
from pubchempy import get_compounds, Compound

file = "ecoli_chemicals.txt"

# 120/1160
def getCleanSmilesData(file_name):
    with open(file_name) as file, open("ecoli_new.txt", "w") as out:
        tsv_file = csv.reader(file, delimiter = "\t")
        updated = csv.writer(out, delimiter = "\t")
        first = True
        for line in tsv_file:
            if first:
                first = False
                continue
            if len(line) < 3:
                name = line[1]
                comps = get_compounds(name, 'name')
                if comps:
                    line.append(comps[0].canonical_smiles)

            updated.writerow(line)

getCleanSmilesData(file)
