'''
Created on 19.1.2011

@author: Ivan Vogel
'''

class model(object):
    '''
    classdocs
    '''


    def __init__(self):
        '''
        Constructor
        '''
        pass
    
    def count(self,sequence1,sequence2):
        pass
    

'''
helper functions
'''

def dotProduct(a,b):
    sum = 0
    for x,y in zip(a,b):
        sum += x*y
    return sum
        
        
if __name__ == "__main__":  
    a = (2,4,6)
    b = (1,2,3)
    print dotProduct(a,b)
        
    