#parser2=Parsers.ParseGenomicFasta("/storage/brno2/home/ivogel/SL_transposon_families_macas/male/Male.labeled.fa")
#parser=Parsers.ParseBam("/storage/ostrava1/home/ivogel/SL_RNA_seq_To_Genomic/results/1erne_M_sorted.bam"
#microrazersParser=Parsers.ParseMicroRazers("/storage/ostrava1/home/ivogel/SL_sRNA_to_Genomic/1M_mr")
#nonteparser=Parsers.ParseBam("/storage/ostrava1/home/ivogel/SL_sRNA_to_mRNA/1M_NONTE_1_erne")

import sys, getopt
import os



class Params(object):
 def __init__(self,argv):
   self.params={}
   self.output=""
   self.setParams(argv)
   self.checkParams()
   self.params["outputfile"]=self.output 
  
 def getParams(self):
   return self.params 

 def  setParams(self,argv):
   try:
      opts, args = getopt.getopt(argv,"hg:m:s:n:f:o:",["gfile=","mfile=","sfile=","nfile=","ffile=","ofile="])
   except getopt.GetoptError:
      print 'test.py -g <genomicreads> -m <mrnaalignment> -s <srnaalignment> -n <nontealignment> -f <clustersfasta> -o <outputfile>'
      sys.exit(2)
   for opt, arg in opts:
      if opt == '-h':
         print 'test.py -g <genomicreads> -m <mrnaalignment> -s <srnaalignment> -n <nontealignment> -f <clustersfasta> -o <outputfile>'
         sys.exit()
      elif opt in ("-g", "--gfile"):        
         self.params["genomic"] = arg
      elif opt in ("-m", "--mfile"):
         self.params["mrna"] = arg
      elif opt in ("-s","--sfile"):
         self.params["srna"] = arg
      elif opt in ("-n","--nfile"):
         self.params["nontemrna"] = arg
      elif opt in ("-f","--ffile"):
         self.params["clustersfasta"] = arg
      elif opt in ("-o","--ofile"):
         self.output = arg
  
 def dumpParams(self):
     print self.params
 
 def checkParams(self):
     i=False
     for k in self.params.values():
       if not os.path.isfile(k):
         i=True
         print 'File {} does not exist'.format(k)
     if i: sys.exit()



#param=Params(sys.argv[1:])
#params=param.getParams()
#print params


#python Params.py -g /storage/brno2/home/ivogel/SL_transposon_families_macas/male/Male.labeled.fa -m /storage/ostrava1/home/ivogel/SL_RNA_seq_To_Genomic/results/1erne_M_sorted.bam -s /storage/ostrava1/home/ivogel/SL_sRNA_to_Genomic/1M_mr -n /storage/ostrava1/home/ivogel/SL_sRNA_to_mRNA/1M_NONTE_1_erne -o Mleaves


#

