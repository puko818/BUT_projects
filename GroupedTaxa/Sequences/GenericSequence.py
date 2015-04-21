'''
Created on 18.1.2011

@author: Ivan Vogel
'''


'''
konstruktor prijima list sekvencii
'''
class GenericSequence():
    
    def __init__(self, sequences,names=None):
        self.sequences = sequences
        self.name = names
        self.bootstrap = False 
        if not self.sequences:
            self.sequences = list()
            
    def __iter__(self):
        self.position = 0
        self.maxpos = len(max(self.sequences, key = len))
        return self
    
    def next(self):
        if self.position > (self.maxpos-1):
            raise StopIteration
        element = []
        for sequence in self.sequences:
            try:
                actual = sequence[self.position]
            except IndexError:
                actual = '*' 
            element.append(actual)      
        self.position += 1
        return element
    
    def getSequences(self):
        return self.sequences
    
    def addSequence(self,seq, name=None):
        self.sequences.append(seq)
        #self.names.append(name)
        
    def activateBootstrap(self,values): 
        self.bootstrap_values = values
        self.tmp_next = self.next
        self.next = self.bootstrapNext
        
    def deactivateBootstrap(self):
        self.next = self.tmp_next
            
    def bootstrapNext(self):
        if self.position > (self.maxpos-1):
            raise StopIteration
        element = []
        for sequence in self.sequences:
            try:
                actual = sequence[self.bootstrap_values[self.position]]
            except IndexError:
                actual = '*' 
            element.append(actual)      
        self.position += 1
        return element
    
    def __len__(self):
        return len(max(self.sequences, key = len))
'''        
import random
a = GenericSequence(["ABCDEFGH",
                     "12345678"])
b = GenericSequence(["IJKLMNOP",
                    "9ABCDEFG"])



bootstrap =  [random.randint(0,len(a)-1) for x in range(0,len(a)) ]

print bootstrap

a.activateBootstrap(bootstrap)
b.activateBootstrap(bootstrap)


for a1,b1 in zip(a,b):
    print (a1,b1)

'''

        
        