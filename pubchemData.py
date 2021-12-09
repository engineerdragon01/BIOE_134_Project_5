import csv
from pubchempy import get_compounds, Compound

file = "good_chems.txt"

def getCleanSmilesData(file_name):
    with open(file_name) as file, open("out.txt", "w") as out:
        tsv_file = csv.reader(file, delimiter = "\t")
        updated = csv.writer(out, delimiter = "\t")
        for line in tsv_file:
            if line[3] == "null":
                name = line[1]
                comps = get_compounds(name, 'name')
                if comps:
                    line[3] = comps[0].canonical_smiles
            updated.writerow(line)

function(file)
