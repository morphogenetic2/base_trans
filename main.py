import sys

# This is a very simple DNA to protein translator using the universal genetic code.

# Definition of the codons in a dictionary
geneticCodeLong = {
    'gct': 'Ala',
    'gcc': 'Ala',
    'gca': 'Ala',
    'gcg': 'Ala',

    'cgt': 'Arg',
    'cgc': 'Arg',
    'cga': 'Arg',
    'cgg': 'Arg',
    'aga': 'Arg',
    'agg': 'Arg',

    'aat': 'Asn',
    'aac': 'Asn',

    'gat': 'Asp',
    'gac': 'Asp',

    'tgt': 'Cys',
    'tgc': 'Cys',

    'caa': 'Gln',
    'cag': 'Gln',

    'gaa': 'Glu',
    'gag': 'Glu',

    'ggt': 'Gly',
    'ggc': 'Gly',
    'gga': 'Gly',
    'ggg': 'Gly',

    'cat': 'His',
    'cac': 'His',

    'att': 'Ile',
    'atc': 'Ile',
    'ata': 'Ile',

    'atg': 'Met',

    'tta': 'Leu',
    'ttg': 'Leu',
    'ctt': 'Leu',
    'ctc': 'Leu',
    'cta': 'Leu',
    'ctg': 'Leu',

    'aaa': 'Lys',
    'aag': 'Lys',

    'ttt': 'Phe',
    'ttc': 'Phe',

    'cct': 'Pro',
    'ccc': 'Pro',
    'cca': 'Pro',
    'ccg': 'Pro',

    'tct': 'Ser',
    'tcc': 'Ser',
    'tca': 'Ser',
    'tcg': 'Ser',
    'agt': 'Ser',
    'agc': 'Ser',

    'act': 'Thr',
    'acc': 'Thr',
    'aca': 'Thr',
    'acg': 'Thr',

    'tgg': 'Trp',

    'tat': 'Tyr',
    'tac': 'Tyr',

    'gtt': 'Val',
    'gtc': 'Val',
    'gta': 'Val',
    'gtg': 'Val',

    'taa': '***',
    'tga': '***',
    'tag': '***',
}

# Input of the DNA sequence and cleanup
dna = input('What\'s your DNA? ')
dna = dna.lower()  # convert to lowercase

# DNA sequence cleanup

dnaClean = ''
for base in dna:
    if base == 'a' or base == 'c' or base == 't' or base == 'g':
        dnaClean += base
    else:
        pass

dna = dnaClean  # Renaming dna to dnaClean
print('Your clean sequence is %s' % dna)

if len(dna) % 3 != 0:
    print('This is not a correct ORF, you have %d mismatched bases' % (len(dna) % 3))
    sys.exit(0)

#triplets = [dna[i:i + 3] for i in
 #           range(0, len(dna), 3)]  # Iterate through dna to make a list with all of the triplets, isolated

triplets=[]
for i in range(0,len(dna),3):
    triplets+=dna[i:i+3]
 
# print(triplets)
proteinLong = ''  # Long string for the translated protein
dnaLong = ''  # Formatted final DNA sequence

for codon in triplets:  # Iterate through the dna sequence looking up in the geneticCode dictionary
    aminoacidLong = geneticCodeLong[codon]
    dnaLong += codon + '.'
    proteinLong += aminoacidLong + '.'

print(dnaLong + '\n' + proteinLong)
