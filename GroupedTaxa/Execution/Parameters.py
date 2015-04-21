'''
Created on 20.4.2011

@author: Ivan Vogel
'''
#from Generic import Object
import sys
from optparse import OptionParser


class Parameters(object):
    '''
    singleton for collecting analysis input parameters
    '''
    _instance = None
    def __new__(cls, *args, **kwargs):
        if not cls._instance:
            cls._instance = super(Parameters, cls).__new__(
                                cls, *args, **kwargs)
        return cls._instance
    
    def __init__(self):
        '''
        Constructor
        '''
        self.program_parameters = None
        self.__setParams()
    
    def __setParams(self):    
        parser = OptionParser()
        parser.add_option("-f", "--file", dest="filename",
                          help="select an input FASTA file", metavar="FILE")
        parser.add_option("-q", "--quiet",
                          action="store_false", dest="verbose", default=True,
                          help="don't print status messages to stdout")
        
        parser.add_option("-a","--algorithm",
                          default="nj",
                          help="methods: nj, tdcg, or upgma [default: %default]"
                          )
        
        parser.add_option("-t","--type",
                          default="auto",
                          help="types: protein, nucleotide or auto [default:%default]"
                          )
        
        parser.add_option("-m","--model",
                          default="jc69",
                          help="models: jc69, tamura, kimura, pc, or dayhoff [default:%default]"
                          )
        
        parser.add_option("-d","--deletion",
                          default="pairwise",
                          help="pairwise or complete deletion [default:%default]"
                          )
        
        (option,args) = parser.parse_args(sys.argv[1:])
        self.program_parameters = option






        
