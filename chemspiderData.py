import csv
from chemspipy import ChemSpider
cs = ChemSpider('GtAtpgHtsFeIQuaplrGj8LW0FxSuaJU1')

file = "good_chems.txt"

def convertToSmilesData(file_name):
    i = 0
    with open(file_name) as file, open("out1.txt", "w") as out:
        tsv_file = csv.reader(file, delimiter = "\t")
        updated = csv.writer(out, delimiter = "\t")
        for line in tsv_file:
            if line[3] == "null":
                name = line[1]
                # results = cs.search(name)
                
                line[3] = results[0].smiles
                i += 1
                print(i)
            updated.writerow(line)

convertToSmilesData(file)

# def getMoreCleanSmilesData(file_name):
#     i = 0
#     with open(file_name) as file, open("out1.txt", "w") as out:
#         tsv_file = csv.reader(file, delimiter = "\t")
#         updated = csv.writer(out, delimiter = "\t")
#         for line in tsv_file:
#             if line[3] == "null":
#                 name = line[1]
#                 results = cs.search(name)
#                 if results:
#                     line[3] = results[0].smiles
#                     i += 1
#                     print(i)
#             updated.writerow(line)
#
# getMoreCleanSmilesData(file)
