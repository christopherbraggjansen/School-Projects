######################################################################
# Author: Christopher Jansen
#Python Version: 2.7
# Purpose: Gain More practice breaking a larger problem down into smaller pieces using functions,
# Gain practice manipulating strings
######################################################################
# Acknowledgements:
#   Modified from code written by Dr. Jan Pearce
#  Idea from: http://www.cs.uni.edu/~schafer/1140/assignments/pa9/index.htm
######################################################################

import sys

def testit(did_pass):
    """ Print the result of a test. """
    # This function works correctly
    linenum = sys._getframe(1).f_lineno # Get the caller's line number.
    if did_pass:
        msg = "Test at line {0} ok.".format(linenum)
    else:
        msg = ("Test at line {0} FAILED.".format(linenum))
    print(msg)

def is_nucleotide(sequence):
    '''checks that the string sequence provided is a valid string
    consisting only of the 4 nucleotides A, C, G, and T
    Returns True if so, and False otherwise
    '''
    for n in str(sequence):
        if n == "A" or n == "C" or n == "G" or n == "T": # This loop checks that every character of the string is legal
            didpass = "True"  # I discovered that I could not simply return true right away or the function would not
            # Test any other character except for the first one so didpass stays True as long as n is a legal character
            # Then at the end of the function the function returns true as long as didpass is true
        else:
            return False
    if didpass == "True":
        return True
    else:
        return False
def num_times(sequence, nucleotide):
    '''Returns count of how many times nucleotide is found in sequence.'''
    count =0
    for n in sequence:
        if n == nucleotide:
            count = count + 1
    return count

def complement_strand(sequence):
    '''returns the string which will be the second strand of the DNA sequence
    given that Ts complement As, and Cs complement Gs.'''
    complementlist=[]  # I did the complementlist as a list because lists are mutable and therefore I can add as many
    # Gene letters as I need strings are immutable so I would have to make a new string every time it changed.
    for n in sequence:
        if n == "T":
            complementlist.append("A")
        elif n == "A":
            complementlist.append("T")
        elif n == "C":
            complementlist.append("G")
        elif n == "G":
            complementlist.append("C")
        else:
            return "Sequencing Error"
    complement = ''.join(complementlist)  # This line of code turns a list into a string
    return complement

def mRNA(sequence):
    '''using the return from complement_strand(sequence) with each occurrence
    of the nucleotide T replaced with the nucleotide U'''
    listmRNA =[]  # I used same logic as above with strings and lists
    for n in sequence:
        if n == "T":
            listmRNA.append("U")
        else:
            listmRNA.append(n)
    mrna = ''.join(listmRNA)
    return mrna

def chunk_amino_acid(sequence):
    '''uses mRNA(sequence) and divides it into substrings of length 3,
    ignoring any "extra dna" at the far end returning the relevant substrings in a list.'''
    list_of_chunks=[]
    times = int(len(sequence)) /3
    n=0
    m=3
    for x in range(times):
        list_of_chunks.append(sequence[n:m])  # I decided to use slicing as I find it easier. I learned that I can not
        # use both n in range(times) and n as a variable or they variable gets reset to count of n
        n= n+3
        m= m+3
    return list_of_chunks

def amino_acid_chunks(threecharseq):
    '''expects a three character string as a parameter and returns
    the corresponding single character AminoAcid'''

    # This function is already completed correctly

    translator = { "GCA":"A", "GCC":"A", "GCG":"A", "GCU":"A",
                        "AGA":"R", "AGG":"R", "CGA":"R", "CGC":"R", "CGG":"R", "CGU":"R",
                        "GAC":"D", "GAU":"D",
                        "AAC":"N", "AAU":"N",
                        "UGC":"C", "UGU":"C",
                        "GAA":"E", "GAG":"E",
                        "CAA":"Q", "CAG":"Q",
                        "GGA":"G", "GGC":"G", "GGU":"G", "GGG":"G",
                        "CAC":"H", "CAU":"H",
                        "AUA":"I", "AUC":"I", "AUU":"I",
                        "UUA":"L", "UUG":"L", "CUA":"L", "CUC":"L", "CUG":"L", "CUU":"L",
                        "AAA":"K", "AAG":"K",
                        "AUG":"M",
                        "UUC":"F", "UUU":"F",
                        "CCA":"P", "CCC":"P", "CCG":"P", "CCU":"P",
                        "AGC":"S", "AGU":"S", "UCA":"S", "UCC":"S", "UCG":"S", "UCU":"S",
                        "ACA":"T", "ACC":"T", "ACG":"T", "ACU":"T",
                        "UGG":"W",
                        "UAC":"Y", "UAU":"Y",
                        "GUA":"V", "GUC":"V", "GUG":"V", "GUU":"V",
                        "UAA":"*", "UAG":"*", "UGA":"*" }
    if threecharseq in translator.keys():
        return translator[threecharseq]
    else:
        return "?"

def genomics_test_suite():
    ''' genomics_test_suite() is designed to test the following:
    is_nucleotide(sequence)
    num_times(sequence, nucleotide()
    complement_strand()
    amino_acid_chunks()
    sequence_gene()
    '''

    # The following tests test the is_nucleotide() function
    testit(is_nucleotide("CGTAGGCAT")==True)
    testit(is_nucleotide("CGTAFLCAT")==False)
    testit(is_nucleotide(int(123456))==False)  # Added a test if the user inputs a totally incorrect string such as
    # an integer
    # Testing the num_times() function
    testit(num_times("CGTAGGCAT",'T')==2)
    testit(num_times("CGTAGGCAT",'G')==3)
    testit(num_times("CGTCGTTCT",'A')==0)
    testit(num_times("GGCA",'T')==0)


    # Testing the complement_strand() function
    testit( complement_strand("CC") == "GG")
    testit( complement_strand("CA") == "GT")
    testit(complement_strand("CGTAGGCAT")=="GCATCCGTA")
    testit(complement_strand("CGTAFLCAT")=="Sequencing Error")

    # Testing the mRNA() function
    testit(mRNA("GCATCCGTA")=="GCAUCCGUA")

    # Testing amino_acid_chunks()
    testit(amino_acid_chunks('AGA')=='R')
    testit(amino_acid_chunks('AFA')=='?')

    # Testing amino_acid_chunks()
    testit(chunk_amino_acid("CGTAGGCAT")==["CGT","AGG","CAT"])

    # Testing sequence_gene()
    testit(sequence_gene("T")=='') # because input is not in a group of 3 nucleotides
    testit(sequence_gene("JAN")=='') # because input is not a valid string of nucleotides
    testit(sequence_gene("CACGT")=='V') # because mRNA sequence is "GUGCA"
                                        # and ignoring the last two "extra" nucleotides,
                                        # this returns amino acid "V".

    testit(sequence_gene("CGTAGGCAT")=="ASV") # because mRNA sequence is "GCAUCCGUA"
                                              # taking the complement and then replacing the T nucleotide with U.
                                              # Grouping into triples, we  get the "ASV" amino acid sequence.
def sequence_gene(sequence):
    '''sequence_gene() takes a a sequence of nucleotides: A, C, G, and T and returns
    the corresponding amino acid sequence.'''
    
    # This function is fully tested

    aaseq=""
    if is_nucleotide(sequence):
        comp_strand=complement_strand(sequence)
        mrna=mRNA(comp_strand)
        amino_acid_list=chunk_amino_acid(mrna)

        for amino_acid in amino_acid_list:
            aaseq=aaseq+amino_acid_chunks(amino_acid)
    return aaseq # Returns an empty string for any iiegal input

def main():
    '''main calls genomics_test_suite() which will test each of the supportive functions'''
    # print(sequence_gene("CACGT")) # To use directly
    genomics_test_suite()

main() # call to main() function

