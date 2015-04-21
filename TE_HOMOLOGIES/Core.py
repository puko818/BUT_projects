###################################
#Core classes for TE alignment data and the related processing operations, filtering and edge identification
##################################
import collections
from sets import Set
import sys
####include locally installed libraries
sys.path.append('/storage/brno2/home/ivogel/.local/lib/python2.7/site-packages')
sys.path.append('/storage/brno2/home/ivogel/software/python-2.7.6/intel/lib/python2.7/site-packages')
####################################
import Parsers
import Params
import pickle
from timeit import Timer
import pysam
from itertools import *
from pyfaidx import Fasta


class FamilyCollection(object):
  def __init__(self,organ="default"):
    self._organ=organ
    self._families=dict()
    self._srnaspecific=dict()
    self._mrnanonte=Set([])
    self._srnaref=None
    self._srnaall=None
  
  def __iter__(self):
    for elem in self._families.values():
       yield elem
  
  def __len__(self):
    # If the generator is exhausted, we know its length, so
     # we can use that information; if not, we raise TypeError,
     # just like any other object with no length
     result = len(self._families)
     if result is None:
        raise TypeError, "object of type %s has no len()" % \
            self.__class__.__name__
     return result
    
  def __getitem__(self, index):
     # Return the item at index, advancing the generator if
     # necessary; if the generator is exhausted before index,
     # raise IndexError, just like any other sequence when an
     # index out of range is requested
     if index not in self._families.keys():
         raise IndexError, "sequence index out of range"
     return self._families[index]
 
  def GetsRNAAllFamilies(self,treshold,d):
    if not hasattr(self,'_srnaall'):
      self._srnaall=Set([])
      for f in self._families.values():
        self._srnaall=(f.GetAllRNAClusters(treshold)).union(self._srnaall)
    if len(self._srnaall)>0:
      #return set([(str(d[i]),i) for i in self._srnaall])
      for i in self._srnaall:
         print str(d[i])
    else:
      return set([])


  def GetsRNAID(self,seq):
    return self._srnasequences[seq]
 
 
  def GetsRNARefFamilies(self,treshold,d):
    if not hasattr(self,'_srnaref'):
      self._srnasequences={}
      self._srnaref=Set([])
      for f in self._families.values():
        self._srnaref=(f.GetRefsRNAClusters(treshold)).union(self._srnaref)
    if len(self._srnaref)>0:
      for i in self._srnaref:
         self._srnasequences[str(d[i])]=i 
      #return set([str(d[i]) for i in self._srnaref])
         print str(d[i])
         # return set(self._srnasequences.keys())
    else:
      return set([])
    

  def CheckAndAddNonTERelationship(self,mrna,srna):
     for fam in self._families.values():
         if fam.AddMRNASRNAnonte(mrna,srna):
            self._mrnanonte.add(mrna)


  def InterSectionAllSRNA(self,treshold,d):
    for i in range(1,len(self._families.keys())+1):
      for j in combinations(self._families.keys(),i):
          t=set.intersection(*[self._families[k].GetAllRNAClusters(treshold) for k in list(j)])
          if len(t)>0:
            for s in t:
              tref_rec=str(s).split("|")
              for f in j:
                 print f,
              for t in tref_rec:
                 print t,
              print d[s],
              print
            #tref=[s for s in t if len(str(s).split("|"))==5]
            #if len(tref)>0:
 
  def InterSectionRefSRNA(self,treshold):
    for i in range(1,len(self._families.keys())):
      for j in combinations(self._families.keys(),i):
          t=set.intersection(*[set(self._families[k]._srnaclusters) for k in list(j)])
          if len(t)>0:
            for s in t:
              tref_rec=str(s).split("|")
              if len(tref_rec)==5:
                #tref=[s for s in t if len(str(s).split("|"))==5]
                #if len(tref)>0:
                #for g in tref:
                (seqid,seqlen,clustersize,ref)=tref_rec[0],tref_rec[2],tref_rec[3],tref_rec[4]
                if str(seqid).startswith("HWI") and int(clustersize)>=treshold:
                  for f in j:
                     print f, 
                  print seqid,seqlen,clustersize,ref

  def CheckAndUpdateNonTERelationship(self,mrna,sequence):
     if mrna in self._mrnanonte:
      for fam in self._families.values():
         fam.UpdateMRNASRNANONTE(mrna,sequence)


  def InsertGenomicRead(self,family,readID,sequence,additional=""):
     if self._families.has_key(family):
        self._families[family].AddRead(readID[1:],sequence,additional)
     else:
        fam=Family(str(family))
        fam.AddRead(readID[1:],sequence,additional)
        self._families[family]=fam
 
  def GetFamily(self,name):
    if name not in self._families.keys():
       f=Family(name)
       self._families[name]=f
    else: f=self._families[name]
    return f
  
  def FamiliesSizes(self):
    for fam in self._families:
      print fam,
      print self._families[fam].Size()

  def DumpFamilies(self):
     print self._families 


  #check check families containing the cluster, if true return the list families, otherwise return None deprecated??
  def IsSRNA(self,srnaid):
    families=[]
    for i in self._families.keys():
      if self._families[i].HasClusterSRNA(srnaid):
          #print "it has!"
          families.append(self._families[i])
    return families

  #check if any of the families contains sRNA that is also homologous to non repetitive part of transcriptome
  #if true return family, otherwise return None
  def IsMRNASRNAnonte(self,mrnaid): 
    families=[]
    for i in self._families.keys():
       if self._families[i].HasMRNASRNANONTE(mrnaid):
         families.append(self._families[i])
         #print "coucou"
    return families

#('HWI-ST1210:79:D0YE5ACXX:7:2308:19095:43756|491419|19|4|cpa-miR8155', ('AAAAAAAACAGAAATTTTTTTTTTTAAAATAATACTGTTCATCCGTGAACAGTACGGAAACGAAAAATAAAATTCACAGCTCAAAAAAAATTCCAGCCGATTATATTTTTTCGCAAACCCTAATTATTGTTTACAAACAATTTTATGAGAATCATCAAAATTAAAATTCGTAACCTGGCTCTGATACCACTTGTGGGATTTATCTGTATGCATCCCTTTATTTTTAAGGATTATAACGAATTATAAAGTGATGATT', ''))


class Family(object):
  def __init__(self,name):
    self._name=name
    self._genomicreads={}
    self._homologyMRNA=[]
    self._homologySRNA=[]
    self._srnaclusters=Set([])
    self._MRNASRNAnonte={}
    self._filteredsrna=None
  
   
  def GetRefsRNAClusters(self,treshold):
    output=set([])
    for i in self._srnaclusters:
      tmp=i.split("|")
      if len(tmp)>4 and tmp[0].startswith("HWI") and int(tmp[3])>=int(treshold):
        output.add(i)
    return output
  
  def GetAllRNAClusters(self,treshold):
    if not hasattr(self,'_filteredsrna'):
      self._filteredsrna=set([])
      for i in self._srnaclusters:
        tmp=i.split("|")
        if tmp[0].startswith("HWI") and int(tmp[3])>=int(treshold):
          self._filteredsrna.add(i)
    return self._filteredsrna


  
  def PotentialGeneTargets(self):
    for k in self._MRNASRNAnonte.keys():
      print ">"+ k
      print self._MRNASRNAnonte[k][1]
  
  def DumpSRNAClusters(self):
    print "I am ",self._name
    print self._homologySRNA
  
  def DumpSRNAHybridClusters(self):
    print "I am ",self._name
    print self._MRNASRNAnonte
 
  def DumpSRNAHybridAllClusters(self,mirnaseqs,blast):
    for k,v in self._MRNASRNAnonte.items():
       mrnaid=k
       (srnacluster,seq)=v
       tmp=srnacluster.split("|")
       if len(tmp)==5:
         (srnaid,i,seqlen,clustersize,ref)=tuple(tmp)
         if mrnaid in blast.keys() and srnaid in mirnaseqs.keys(): print '{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}'.format(mirnaseqs[srnaid],clustersize,seqlen,ref,seq,mrnaid,self._name,blast[mrnaid])
       elif len(tmp)==4:
         (srnaid,i,seqlen,clustersize)=tuple(tmp)
         if mrnaid in blast.keys() and srnaid in mirnaseqs.keys(): print '{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}'.format(mirnaseqs[srnaid],clustersize,seqlen,seq,mrnaid,self._name,blast[mrnaid])
       else:
         print "Error!"
         sys.exit(2)
       #if mrnaid in blast.keys(): print '{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}'.format(mirnaseqs[srnaid],clustersize,seqlen,seq,mrnaid,self._name,blast[mrnaid])

  def DumpSRNAHybridIdentifiedClusters(self,mirnaseqs,blast):
      for k,v in self._MRNASRNAnonte.items():
       mrnaid=k
       (srnacluster,seq)=v
       tmp=srnacluster.split("|")
       if len(tmp)==5:
         (srnaid,i,seqlen,clustersize,ref)=tuple(tmp)
         if mrnaid in blast.keys() and srnaid in mirnaseqs.keys(): print '{0}\t{1}\t{2}\t{3}\t{4}\t{5}\t{6}\t{7}'.format(mirnaseqs[srnaid],clustersize,seqlen,ref,seq,mrnaid,self._name,blast[mrnaid])     
   
  #add sRNA cluster homologous to self, store specific sRNA-DNA pair as well as sRNA ID (unique - srnaclusters)
  def AddSRNAHomology(self,sequence,sRNAID,genomicReadID):
    self._srnaclusters.add(sRNAID)
    self._homologySRNA.append((sRNAID,self._genomicreads[genomicReadID]))


  def GetIdentifiedSRNA(self,seqs):
    for i in self._homologySRNA:
      b=str(i[0]).split("|")
      if len(b)==5:
        if b[0] in seqs.keys(): print (seqs[b[0]],b[2],b[3],b[4],self._name)
       
  def GetSRNA(self,seqs):
    for i in self._homologySRNA:
      b=str(i[0]).split("|")
      if len(b)==5:
        if b[0] in seqs.keys(): print (seqs[b[0]],b[2],b[3],b[4],self._name)
      else:
        if b[0] in seqs.keys(): print (seqs[b[0]],b[2],b[3],self._name)

 
  def AddMRNAHomology(self,sequence,mRNAID,genomicReadID):
    self._homologyMRNA.append((mRNAID,self._genomicreads[genomicReadID]))

  def AddRead(self,readID,sequence,additional):
     self._genomicreads[readID]=(sequence,additional)

  def Size(self):
     return len(self._genomicreads)
  
  def HasClusterSRNA(self,srnaid):
    val=srnaid in self._srnaclusters
    #print val,self._name,srnaid
    return val

  #homology of sRNA-TE specific cluster to some nonTE content in mRNA
  def AddMRNASRNAnonte(self,mrnaid,srnaid):
     #if mrnaid in self._MRNASRNAnonte.keys():
     if srnaid in self._srnaclusters:
       #print "macuch"
       self._MRNASRNAnonte[mrnaid]=srnaid
       return True
     return False
  
  
  def UpdateMRNASRNANONTE(self,mrnaid,sequence):
     if mrnaid in self._MRNASRNAnonte.keys():
       t=(self._MRNASRNAnonte[mrnaid],sequence)
       #print self._MRNASRNAnonte[mrnaid]#=tuple(list(self._MRNASRNAnonte[mrnaid]).append(sequence))
       self._MRNASRNAnonte[mrnaid]=t
       return True
     return False
