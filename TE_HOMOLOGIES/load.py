from Core import FamilyCollection
from Core import Family
import pickle
import sys
from itertools import *


sys.path.append('/storage/brno2/home/ivogel/software/python-2.7.6/intel/lib/python2.7/site-packages')
from pyfaidx import Fasta



organs={}

##Input parameter is a configuration file, fields delimited by ":"
##Example of serialized dictionaries loading
with open(sys.argv[1],'r') as fil:
  for line in fil:
     (organid,serialized,srna,treshold)=line.strip().split(":")
     f=open(serialized,'rb')
     #load serialized object, fasta index file and quantity treshold
     organs[organid]=(pickle.load(f),Fasta(srna),treshold)
  #loop in all TE-families in particular organ, i.e. Male Leaves
  for f in organs['Mleaves'][0]:
    #output sRNAs homologous to particular TE-family
    print f._homologySRNA
    #output all small RNAs homologous to TEs and also to non-repetitive part of transcriptome (potential miRNA->TE->siRNA->gene network)
    f.PotentialGeneTargets()





 
