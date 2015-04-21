#####################################
## Script for merging two hitfiles (sequence coverage data file), i.e. two specific variants of transposable elements,
## obtaining a consensus hitfile
## input file: pos\tnumber_of_nucleotides\n
#####################################

import sys
from itertools import izip_longest


#for i in xrange(1,1001):
#for (c1,c2) in izip_longest(a,b):
#  print c1,c2

endf1=False
endf2=False


try:
 with open(sys.argv[1]) as f1:
    with open(sys.argv[2]) as f2:
        #zahadzujeme hlavicku
        for i in xrange(0,2):
          f1.readline()
          f2.readline()
        pos1,count1=f1.readline().split()
        pos2,count2=f2.readline().split()
        i=0
        while (i<=1001):
           #print pos1,pos2
           if ((pos1>i and  pos2>i) or (pos2==-100 or pos1==-200)):
             i=i+1
           if int(i)==int(pos1):
             if int(i)==int(pos2):
               print i,int(count1)+int(count2)
               tmp=f2.readline().split()
               if tmp:
                 pos2,count2=tmp
               else: 
                 pos2=-100
                 count2=-100
             else:
               print i,int(count1)
             tmp2=f1.readline().split()
             if tmp2:
               pos1,count1=tmp2
             else:
               pos1=-200
               count1=-200          
           elif int(i)==int(pos2):
             print i,int(count2)
             tmp=f2.readline().split()
             if tmp:
               pos2,count2=tmp
             else:
               pos2=-100
               count2=-100


 
#except Exception:
#  pass
except:
   #print "Unexpected error:", sys.exc_info()[0] 
   pass
    
   
