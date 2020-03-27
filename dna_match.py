dna = 'GTAT'
def DNA_strand(dna):
    dna = dna.replace("A","%temp%").replace("T", "A").replace("%temp%","T")
    dna = dna.replace("C","#temp#").replace("G", "C").replace("#temp#","G")

    return dna

print(DNA_strand(dna))
