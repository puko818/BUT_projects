'''
Created on 28.3.2011

@author: Ivan Vogel
'''

import sys
sys.path.append('C:\\Users\\Ivan Vogel\\Desktop\\workspace\\IntraGroupClustering\\src')
from Exceptions import ParameterException
from Execution import Parameters
from Algorithms import NeighborJoining

if __name__ == '__main__':
    params = Parameters.Parameters()
    
    if params.program_parameters.algorithm is 'nj':
        algorithm_instance = NeighborJoining.NeighborJoining()
        
    elif params.program_parameters.algorithm is 'upgma':
        pass
    
    elif params.program_parameters.algorithm is 'tdcg':
        pass
    
    else:
        raise ParameterException
    
    algorithm_instance.LoadSeq()
    algorithm_instance.MakeGroups()
    
