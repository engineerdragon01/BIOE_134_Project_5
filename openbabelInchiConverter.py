import csv

good_chems_file = "good_chems.txt"

# def inchiAndSmilesColumns(file):
#     with open("good_chems.txt") as file, open("inchisAndSmiles.txt", "w") as f:
#     tsv_file = csv.reader(file, delimiter = "\t")
#     inchisAndSmiles = csv.writer(f, delimiter = "\t")
#     for line in tsv_file:
#         new_line = [line[2], line[3]]
#         inchisAndSmiles.writerow(new_line)
#
# inchiAndSmilesColumns(good_chems_file)

def inchisFileMaker(file):
    first = True
    with open("good_chems.txt") as file, open("inchis.txt", "w") as f:
        tsv_file = csv.reader(file, delimiter = "\t")
        inchisAndSmiles = csv.writer(f, delimiter = "\t")
        for line in tsv_file:
            if first:
                first = False
                continue
            new_line = [line[2]]
            inchisAndSmiles.writerow(new_line)

inchisFileMaker(good_chems_file)
