'''
Created on 19.1.2011

@author: Ivan Vogel
'''
from Models import Model
from Sequences import GenericSequence,FrequenceAnalysis
from math import log1p
from cogent.parse.fasta import MinimalFastaParser



class JC(Model.model):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def count(self,sequence1,sequence2):
        dec1 = FrequenceAnalysis.FrequenceAnalysis(sequence1)
        dec2 = FrequenceAnalysis.FrequenceAnalysis(sequence2)
        '''
        probability no substitution occurs
        '''
        #sites_count = len(min([dec1,dec2], key = len))
        sites_count = len(dec1)
        different_sites = 0
        for e1,e2 in zip(dec1,dec2):
            different_sites += (1- Model.dotProduct(e1,e2))
        #return (-float(3)/4)* log1p(-(float(4)/3)*different_sites/sites_count)      
        return different_sites/sites_count
        
    def Name(self):
        print "Juke-Cantor model"

            

        
if __name__ == "__main__": 
    a_1 = "GAACCTGCGGAAGGATCATTGTTGTTGCCTTTTGAAAACACGACCGTTGCACAAGTAAAGAAACGATGCCGAGGAGGG---CAGCCCCCTCGGCTCCACCGGCCCCGAACA-GCCCTTGCCTTCCGGGG--CGTGCTGGTCGCGGTGTCGGAACACGGCGCGGGTTGGCGCCAAGGAATACATGCTTGCTGAGGCAGACGGCGGTGCTTCGGCATCGTGCCATCTGTCGAGGCCAAAGAAATGAAATGAGATGACTCCCGGCAACGGATATCTCGGCTCTCGCATCGATGAAGAACGTAGCGAAATGCGATACATGGTGTGAATTGCAGAATCCCGTGAACCATCGAGTCTTTGAACGCAAGTTGCGCCCGAGGGACCATCCCGAGGGCACGCCTGCCTCATGGGCGTTAGAAGCCCATCCACGCTCGGCGCA-CGT-CCTTGTAGGCCTGCCCGATGCGGACAAAATGGCCCTCCGAGCCGTGAGGCGCGACGGGCACAAGTGTATGGCCGTCGGTTGAGGCCGGGAGCGGCGAGTGGTGGGCTAACTGCGCACGCTGCCTCCGAACCTCATGCCGACGTTAGGCCTATTT-GGACCTCGAAACGAGGAGTACGTCGCCT-AGCGCGGCAG--CCTCGGACCGATACCCCAGGTCAGGCGTGGCCACCCGCTGAGTTTAAGCATATCAATAAGCGG"
    a_2 = "GAACCTGCGGAAGGATCATTGTTGTTGCCTTTTGAAAACACGACCGTTGCACAAGTAAAGAAACGATGCCGAGGAGGG---CAGCCCCCTCGGCTCCACCGGCCCCGAACA-GCCCTTGCCTTCCGGGG--CGTGCTGGTCGCGGTGTCGGAACACGGCGCGGGTTGGCGCCAAGGAATACATGCTTGCTGAGGCAGACGGCGGTGCTTCGGCATCGTGCCATCTGTCGAGGCCAAAGAAATGAAATGAGATGACTCCCGGCAACGGATATCTCGGCTCTCGCATCGATGAAGAACGTAGCGAAATGCGATACATGGTGTGAATTGCAGAATCCCGTGAACCATCGAGTCTTTGAACGCAAGTTGCGCCCGAGGGACCATCCCGAGGGCACGCCTGCCTCATGGGCGTTAGAAGCCCATCCACGCTCGGCGCA-CGT-CCTCGTAGGCCTGCCCGATGCGGACAAAATGGCCCTCCGAGCCGTGAGGCGCGACGGGCACAAGTGTATGGCCGTCGGTTGAGGCCGGGAGCGGCGAGTGGTGGGCTAACTGCGCACGCTGCCTCCGAACCTCATGCCGACGTTAGGCCTATTT-GGACCTCGAAACGAGGAGTACGTCGCCT-AGCGCGGCAG--CCTCGGACCGATACCCCAGGTCAGGCGTGGCCACCCGCTGAGTTTAAGCATATCAATAAGCGG"
    b_1 = "GAACCTGCGGAAGGATCATTGTTGTTGCCTTTTGAAAACACGACCGGTGCACGAGTAAAGAAACGCTGTCGGGGAGGG---CAACCTCCTCGGCTCCACCGGCCCCGAACA-GCTCTCGTCCTTCGGGG--CGTGCTGGTCGTGGTGTCGGAATACGGCGCGGGTTGACGCCAAGGAATACATGTTTGCTGAGGCAGACGGCGATGCTTCGGCGTCGCCCGATCTGTCAAGGCCAAAGTAATAAAATGAGATGACTCCCGGCAACGGATATCTCGGCTCTCGCATCGATGAAGAACGTAGCGAAATGCGATACATGGTGTGGATTGCAGAATCCCGTGAACCATCGAGTCTTTGAACGCAAGTTGCGCCCGAGGGACCATCCCGAGGGCACGCCTGCCTCATGGGCGTTAGAAGCCCATCCACGCTCGGTGCA-CCTGCCTCGCAGGCCTGCCCGATGCGGACAA--TGGCCCTCCGAGCCGCGAGGCGCGACGGGCACAAGTGCATGGCCGTCGGTTGAGGCCGGGAGCGGCGAGTGGTGGGCTAACTGCGCACGCTGCCTCCGAACCTCACGTCGACGTAAGGCCTAGTT-GGACCTCGAAACGAGGAGTTTGTCGCCT-AGCGCGGCAGAGCCTCGGACCGATACCCCAGGTCAGGCGTGGCCACCCGCTGAGTTTAAGCATATCAATAAGCGG"
    b_2 = "GAACCTGCGGAAGGATCATTGTTGTTGCCTTTTGAAAACACGACCGGTGCACGAGTAAAGAAACGCTGTCGGGGAGGG---CAACCTCCTCGGCTCCACCGGCCCCGAACA-GCTCTCGTCCTTCGGGG--CGTGCTGGTCGTGGTGTCGGAATACGGCGCGGGTTGACGCCAAGGAATACATGTTTGCTGAGGCAGACGGCGATGCTTCGGCGTCGCCCGATCTGTCAAGGCCAAAGTAATAAAATGAGATGACTCCCGGCAACGGATATCTCGGCTCTCGCATCGATGAAGAACGTAGCGAAATGCGATACATGGTGTGAATTGCAGAATCCCGTGAACCATCGAGTCTTTGAACGCAAGTTGCGCCCGAGGGACCATCCCGAGGGCACGCCTGCC---TGGGCGTTAGAAGCCCATCCACGCTCGGCGCA-C---------------GCCCGATGCGGACAA--TGGCCCTCCGAGCCGCGAGGCGCGACGGGCACAAGTGCATGGCCGTCGGTTGAGGCCGGGAGCGGCGAGTGGTGGGCTAACTGCGCACGCTGCCTCCGAACCTCACGTCGACTGAAGGCCTAGTT-AGACCTCGAAACGAGGAGTTTGTCGCCT-AGCGCGGCAGAGCCTCGGACCGATACCCCAGGTCAGGCGTGGCCACCCGCTGAGTTTAAGCATATCAATAAGCGG"
    a = GenericSequence.GenericSequence([a_1,a_2],'a')
    b = GenericSequence.GenericSequence([b_1,b_2],'b')
    model = JC()
    #print model.count(a,b)
    
    f2=open('/home/puko/Desktop/science_aligned.fas' )
    sequences  = dict()
    for name,seq in MinimalFastaParser(f2):
        print len(seq)
        if name[:name.find('|')] in sequences:
            list = sequences[name[:name.find('|')]]
            list.append(seq)
            sequences[name[:name.find('|')]] = list
        else:
            sequences[name[:name.find('|')]] = [seq]
            
    #nacitanie sekvencii
    bububu = []
    for n in sequences:
        bububu.append(GenericSequence.GenericSequence(sequences[n],n))
    

    
    model = JC()
    #for seq in bububu:
    dists = dict()
    for i in range(len(bububu)-1):
        for j in range(i+1,len(bububu)):
            dists[(bububu[i].name,bububu[j].name)] = model.count(bububu[i],bububu[j])
             
        #model.count()
    #for i in range(len(bububu)):
    #   model.count()
    #from cogent.phylo import nj
    from cogent.phylo import nj
    #dists = {('a', 'b'): 2.7, ('c', 'b'): 2.33, ('c', 'a'): 0.73}
    njtree2 = nj.nj(dists)
    print njtree2.writeToFile('/home/puko/Desktop/science2.newick')
    #njtree2.writeToFile('/home/puko/Desktop/tree.newick')
    #print njtree2.asciiArt()
        
    #bootstrap    
    import random
    

    file = open('/home/puko/Desktop/science_bootstrap2.newick','w')
    trees = str()
    trees_list = []
    
    
    
    for x in range(0,499):
        bootstraplist =  [random.randint(0,len(bububu[0])-1) for x in range(0,len(bububu[0])) ]
        for n in bububu: n.activateBootstrap(bootstraplist)
        dists = dict()
        for i in range(len(bububu)-1):
            for j in range(i+1,len(bububu)):
                dists[(bububu[i].name,bububu[j].name)] = model.count(bububu[i],bububu[j])
        njtree3 = nj.nj(dists)
        trees_list.append(njtree3)
        trees += str(njtree3) + '\n'
    
    #njtree2.writeToFile('home/puko/Desktop/consensus.newick')
    import re
    p = re.compile(':\d.\d+(e-\d+)?')
    new_trees = p.sub('',trees)
    file.write(new_trees)
    file.close



    
 

