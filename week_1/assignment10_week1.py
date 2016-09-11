import re

strGenome = "ACAAGATGCCATTGTCCCCCGGCCTCCTGCTGCTGCTGCTCTCCGGGGCCACGGCCACCGCTGCCCTGCCCCTGGAGGGTGGCCCCACCGGCCGAGACAGCGAGCATATGCAGGAAGCGGCAGGAATAAGGAAAAGCAGCCTCCTGACTTTCCTCGCTTGGTGGTTTGAGTGGACCTCCCAGGCCAGTGCCGGGCCCCTCATAGGAGAGGAAGCTCGGGAGGTGGCCAGGCGGCAGGAAGGCGCACCCCCCCAGCAATCCGCGCGCCGGGACAGAATGCCCTGCAGGAACTTCTTCTGGAAGACCTTCTCCTCCTGCAAATAAAACCTCACCCATGAATGCTCACGCAAGTTTAATTACAGACCTGAA"

def identifyGenesFromSeq(strGenomeSeq):
    # Note: to make the code more dynamic the forming
    # of strRegex should be edited.

    strGeneStart = "ATG" # can only start with this string
    lstNotInsideGene = ["ATG", "TAG", "TAA", "TGA"] # 4 items required
    lstGeneEnd = ["TAG", "TAA", "TGA"] # 3 items required
    geneLengthMultiple = 3

    strRegex = "("+strGeneStart+"){1}((?!"+lstNotInsideGene[0]+")(?!"\
        +lstNotInsideGene[1]+")(?!"+lstNotInsideGene[2]+")(?!"\
        +lstNotInsideGene[3]+")[ACGT])+(("+lstGeneEnd[0]+")|("+lstGeneEnd[1]+\
        ")|("+lstGeneEnd[2]+")){1}"
    reGenePattern = re.compile(strRegex)
    geneMatches = reGenePattern.finditer(strGenomeSeq,
        re.IGNORECASE + re.MULTILINE)

    lstGeneMatches = []
    for geneMatch in geneMatches:
        geneMatch = geneMatch.group(0)[len(strGeneStart):-len(max(lstGeneEnd))]
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
