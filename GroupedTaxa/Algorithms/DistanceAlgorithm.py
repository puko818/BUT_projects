'''
Created on 20.4.2011

@author: Ivan Vogel
'''
from Generic import Object
from cogent.parse.fasta import MinimalFastaParser
from Execution import Parameters,formatters
from Sequences import GenericSequence
from Bio.Align.Applications import ClustalwCommandline
import os

class DistanceAlgorithm(Object.Object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        self.sequences = dict()
    
    def LoadSeq(self):
        params = Parameters.Parameters()
        '''
        cline = ClustalwCommandline("clustalw2", infile=params.program_parameters.filename)
        print cline
        cline()
        clustalw_exe = r"C:\Users\Ivan Vogel\Documents\clustalw2.exe"
        clustalw_cline = ClustalwCommandline(clustalw_exe, infile="sequence_340.fasta")
        #assert os.path.isfile(clustalw_exe), "Clustal W executable missing"
        stdout, stderr = clustalw_cline()
        '''
        from Bio.Align.Applications import MuscleCommandline
        cline = MuscleCommandline(input=params.program_parameters.filename, out=params.program_parameters.filename+"_aligned")
        print cline
        cline()
            
    def Align(self):
        pass
    
    def MakeGroups(self):
        params = Parameters.Parameters()
        file = open(params.program_parameters.filename+"_aligned")
        for name,seq in MinimalFastaParser(file):
            key =  formatters.extractGroup_gypExyr(name)
            if key not in self.sequences.keys():
                self.sequences[key]= GenericSequence.GenericSequence([seq],key)
            else:
                self.sequences[key].addSequence(seq)
        print 0
        
        
    
    def CountMatrix(self):
        pass
    
    def MakeTree(self):
        pass
   
    def CompleteRun(self):
        sequence = "A"
        self.LoadSeq(sequence)
        self.Align(sequence)
        self.CountMatrix(sequence)
        self.MakeTree(sequence) 
'''    
class A():
    def __init__(self,hodnota):
        self.bubu = hodnota
    
    def __tajna(self):
        print "ja som tajna"
        
    def Acko(self):
        print self.bubu
        
        
class B(A):
    def Bcko(self):
        print "juchuchu"
        
    def Zverejnena(self):
        self.__tajna()
    
instancia = B(1)
instancia.Zverejnena()
'''