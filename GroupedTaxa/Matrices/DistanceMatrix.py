'''
Created on 21.1.2011

@author: Ivanko
'''


#from cogent import LoadSeqs, DNA
#from cogent.phylo import distance
#from cogent.evolve.models import F81

#aln = LoadSeqs('data/primate_brca1.fasta')
#d = distance.EstimateDistances(aln, submodel=F81())
#d.run()


class DistanceMatrix(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    '''
    key je tuple obsahujuca  
    '''
    def __iter__(self,key):
        return self
    
    def __getitem__(self,key,value):
        pass
    
    def __setitem__(self):
        pass
    
    def next(self):
        return self
    
    #def FillMatrix(self):
    #    pass
    '''
    Textovy vystup matice
    format MEGA
    '''
    def ToString(self):
        pass
    
    
    