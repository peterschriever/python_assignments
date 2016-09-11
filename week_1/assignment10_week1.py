import re

strGenome = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"

def identifyGenesFromSeq(strGenomeSeq):
    strGeneStart = "ATG" # starts with this triplet
    lstGeneInside = ["ATG", "TAG", "TAA", "TGA"] # cannot have these triplets
    lstGeneEnd = ["TAG", "TAA", "TGA"] # ends with either of these triplets
    geneLengthMultiple = 3

    strRegex = "("+strGeneStart+"){1}((?!"+lstGeneInside[0]+")(?!"\
        +lstGeneInside[1]+")(?!"+lstGeneInside[2]+")(?!"+lstGeneInside[3]\
        +")[ACGT])+(("+lstGeneEnd[0]+")|("+lstGeneEnd[1]+")|("+lstGeneEnd[2]\
        +")){1}" # The regular expression in string form
    reGenePattern = re.compile(strRegex) # compile the regex pattern object
    geneMatches = reGenePattern.finditer(strGenomeSeq,
        re.IGNORECASE + re.MULTILINE) # scan the string for matches

    lstGeneMatches = [] # create empty list
    for geneMatch in geneMatches: # iterate over found matches
        geneMatch = geneMatch.group(0)
        if (len(geneMatch) % geneLengthMultiple) is 0:
            lstGeneMatches.append(geneMatch) # save the match as a string

    return lstGeneMatches if lstGeneMatches else "No genes where found."


print("Welcome to the gene identification program.")
print("The genome sequence we will be using is: ")
print(strGenome)
print("\n")

identifyResult = identifyGenesFromSeq(strGenome)
print("Identification completed! The following genes where found:")
print(identifyResult)
