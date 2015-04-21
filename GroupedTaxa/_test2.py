'''
Created on Feb 1, 2011

@author: Ivan Vogel
'''

from Models import JC
from cogent.parse.fasta import MinimalFastaParser
from Sequences import GenericSequence

if __name__ == '__main__':
    file = open("/home/puko/Desktop/franta/eleo_aln_upravene.fas")
    sequences  = dict()
    for name,seq in MinimalFastaParser(file):
        key =  name[:name.find('_')]
        if key not in sequences.keys():
            sequences[key]= [seq]
        else:
            sequences[key].append(seq)
    
    bububu = []
    for n in sequences:
        bububu.append(GenericSequence.GenericSequence(sequences[n],n))
    
    
    model = JC.JC()
    dists = dict()
    for i in range(len(bububu)-1):
        for j in range(i+1,len(bububu)):
            dists[(bububu[i].name,bububu[j].name)] = model.count(bububu[i],bububu[j])
    
    from cogent.phylo import nj
    njtree2 = nj.nj(dists)
    print njtree2.writeToFile('/home/puko/Desktop/franta.newick')
    #print njtree2
    
    
    
    #boootstraping
    import random
    

    file = open('/home/puko/Desktop/franta_bootstrap.newick','w')
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
    
    file.write(trees)
    file.close
    
    
