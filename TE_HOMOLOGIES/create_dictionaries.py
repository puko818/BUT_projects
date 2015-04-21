##################
#Script for indexing sequence IDs for fast random access
################
import Parsers
import sys
import os 
import pickle

parsemrnaseq=Parsers.ParseFasta(sys.argv[1])
name=os.path.basename(sys.argv[1])

seqs={}

#print name.split(".")[0]

for p in parsemrnaseq:
  seqs[p[0]]=p[1] 
  with open('dictionaries/' + name.split(".")[0] +'.obj','wb') as f:
    pickle.dump(seqs,f)

