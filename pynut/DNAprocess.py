def translation(seq, start=1, end=100000000):
    ''''the translation function helps to translate the DNA sequence to the amino acid sequence.
     It requires to input the string format DNA sequence, e.g. "ATC" and returns the corresponding AA sequence.
     You can also specify the starting and ending postion of the coding sequence region.'''
    __author__ = 'Ziliang Luo'

    import string

    table = {
        'ATA':'I', 'ATC':'I', 'ATT':'I', 'ATG':'M',
        'ACA':'T', 'ACC':'T', 'ACG':'T', 'ACT':'T',
        'AAC':'N', 'AAT':'N', 'AAA':'K', 'AAG':'K',
        'AGC':'S', 'AGT':'S', 'AGA':'R', 'AGG':'R',
        'CTA':'L', 'CTC':'L', 'CTG':'L', 'CTT':'L',
        'CCA':'P', 'CCC':'P', 'CCG':'P', 'CCT':'P',
        'CAC':'H', 'CAT':'H', 'CAA':'Q', 'CAG':'Q',
        'CGA':'R', 'CGC':'R', 'CGG':'R', 'CGT':'R',
        'GTA':'V', 'GTC':'V', 'GTG':'V', 'GTT':'V',
        'GCA':'A', 'GCC':'A', 'GCG':'A', 'GCT':'A',
        'GAC':'D', 'GAT':'D', 'GAA':'E', 'GAG':'E',
        'GGA':'G', 'GGC':'G', 'GGG':'G', 'GGT':'G',
        'TCA':'S', 'TCC':'S', 'TCG':'S', 'TCT':'S',
        'TTC':'F', 'TTT':'F', 'TTA':'L', 'TTG':'L',
        'TAC':'Y', 'TAT':'Y', 'TAA':'_', 'TAG':'_',
        'TGC':'C', 'TGT':'C', 'TGA':'_', 'TGG':'W',
    }
    protein = ''
    NTs = {'A', 'T', 'C', 'G'}
    if type(seq) is not str:
        print("Sequence is not string, please input a string format sequence!")
    else:
        seq = seq.upper().rstrip().replace('\n', '')
        if len(set(seq) - NTs) != 0:
            print('DNA sequence contains letter other than ATCG, please check your sequence.')
        elif len(seq) % 3 == 0:
            if end < len(seq):
                for i in range(start-1, end//3*3, 3):
                    codon = seq[i:i+3]
                    protein += table[codon]
            else:
                for i in range(start-1, len(seq), 3):
                    codon = seq[i:i+3]
                    protein += table[codon]
        else:
            print("Warnning: the sequence length is not divisible by 3! Extra tail sequence will be ignored")
            if end < len(seq):
                for i in range(start-1, end//3*3, 3):
                    codon = seq[i:i+3]
                    protein += table[codon]
            else:
                for i in range(start-1, len(seq)//3*3, 3):
                    codon = seq[i:i+3]
                    protein += table[codon]
    return  protein

import string
def complement_seq(text):
    dic = {'A':'T', 'T':'A', 'C':'G', 'G':'C', 'N': 'N'}
    text = text.upper().rstrip()
    new_seq = ''
    for l in text:
        new_seq += dic[l]
    return new_seq
def reverse_seq(text):
    new = ''
    text = text.upper().rstrip()
    for i in text:
        new = i + new
    return new
def reverse_complementary_seq(text):
    new = complement_seq(reverse_seq(text))
    return new

#if __name__ == '__main__':
#    translation(seq)
