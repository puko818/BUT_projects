'''
Created on Mar 20, 2011

@author: Ivan Vogel
'''
'''
class MyClass(object):



    def __init__(selfparams):

'''

from Models import Model
from Models import JC
from Sequences import GenericSequence,FrequenceAnalysis
from math import log1p
from cogent.parse.fasta import MinimalFastaParser


def findValue(collection, element1,element2):
     try:
         return collection[(element1,element2)]
     except KeyError:
         try:
             return collection[(element2,element1)]
         except KeyError:
             raise KeyError
         
'''
divide input matrix according to 2 centroids
'''
#def checkAndFillDistanceMatrix(collection,element,without_element):
def complementDistanceMatrix(collection,complement):
    new_dict = dict()
    for item in collection.keys():
        if not complement.has_key(item):
            new_dict[item] = collection[item]
    return new_dict
    
def lookUpDistances(distmat, cluster):
    newdistmat = dict()
    for i in range(len(cluster)-1):
        for j in range(i+1,len(cluster)):
            try:
                tmp_value = distmat[(cluster[i],cluster[j])]
                tmp_key = (cluster[i],cluster[j]) 
            except KeyError:
                try:
                    tmp_value = distmat[(cluster[j],cluster[i])]
                    tmp_key = (cluster[j],cluster[i])
                except KeyError:
                    tmp_key = None
            if tmp_key is not None:
                newdistmat[tmp_key] = tmp_value
    return newdistmat
                    #not found

                               
        
        
        
    
#def checkDistanceMatrix(collection,element1=None,element2=None):
        
def split(tree,dists):
    if len(dists) < 1:
        return
    else:
        cluster1 = []
        cluster2 = []
        name1 = ""
        name2 = ""
        otu= ""
        #hladame najvzdialenejsi par vramci zhluku
        maximum = max(dists)
        cluster1.append(maximum[0])
        cluster2.append(maximum[1])
        if len(dists) is 1:
            A_node=PhyloNodeExtra(Name=maximum[0])
            B_node=PhyloNodeExtra(Name=maximum[1])
            tree.insert(0,A_node)
            tree.insert(1,B_node)
            return
        else:
            for x in dists:
            #pre vsetky vzdialenosti ine ako vzdialenosti najvzdialenejsich zhlukov
                if maximum[0] in x and maximum[1] not in x:
                    tmp_x = x
                    if maximum[0] is x[0]:
                        otu = x[1]
                    else:
                        otu = x[0]
             
                    if findValue(dists,otu,maximum[1]) > dists[x]:
                        cluster1.append(otu)
                        name1 += otu + "_"
                        #dists_new1[x]= dists[x]
                    else:
                        cluster2.append(otu)
                        name2 += otu + "_"
                        #dists_new2[x] = dists[x]
                    
            
            node1name = ""
            node2name = ""
            if len(cluster1) is 1:
                node1name = cluster1[0]
            if len(cluster2) is 1:
                node2name = cluster2[0]
            A_node=PhyloNodeExtra(Name=node1name)
            B_node=PhyloNodeExtra(Name=node2name)
            tree.insert(0,A_node)
            tree.insert(1,B_node)
            if len(cluster1) is not 1:
                split(A_node,lookUpDistances(dists,cluster1))
            if len(cluster2) is not 1:
                split(B_node,lookUpDistances(dists,cluster2))
            
            
             

if __name__ == '__main__':

    f2=open('C:\\Users\\Ivan Vogel\\Desktop\\workspace\\science_aligned.fas' )
    sequences  = dict()
    for name,seq in MinimalFastaParser(f2):
        #print len(seq)
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
        
    dists = dict()
    model = JC.JC()
    
    for i in range(len(bububu)-1):
        for j in range(i+1,len(bububu)):
            dists[(bububu[i].name,bububu[j].name)] = model.count(bububu[i],bububu[j])
            
    tree_root_string = "ROOT;"
    tree = LoadTree(treestring = tree_root_string)
    split(tree,dists)
    
    print tree.getNewick()
    #print dists


                    
   
        
    #print dists[('$Europe','$American')]
    #print dists[('$Chimpanzee' ,'$East_Asia')]
    #print findValue(dists, '$East_Asia','$Chimpanzee')#print dists[('$East_Asia','$Chimpanzee')]
#print dists[('$Europe','$East_Asia')]

        
