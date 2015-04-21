######################
#Transposon encapsulation as a Python object, main purpose: convenient information about transposon nucleotide coverage in the genome
#####################
import csv
import sys
import re
import os

'''
Sequences IDs excluded from the analysis
'''
banlist = []

csv.field_size_limit(sys.maxint)



class TransposableElement:
  '''
  konstruktor
  '''
  def __init__(self,length,name):
    print length
    self.__hits_per_position = [0 for x in range(length+1)]
    self.__name = name
    self.__length = length  
  def Inc(self,start,end, linenumber):
    tmp = None
    if start >= end:
      tmp = start
      start = end
      end = tmp
    for i in range(start-1,end):
        try:
            self.__hits_per_position[i]+=1
        except Exception:
            print >> sys.stderr,  "Error parsing -> line nr.%i" % (linenumber)
            
  def Dump(self):
    pass

  def HitsPerPos(self):
      return self.__hits_per_position
  '''
  Dump inf to text file
  '''
  def Dump(self,file_handle, evalue):
    file_handle.write("#Sequence:%s,Length:%s\n#E-value: %s\n" % (str(self.__name),str(self.__length),str(evalue)))
    for x,y in enumerate(self.__hits_per_position):
      file_handle.write(str(x+1) + "\t" + str(y) + "\n")


'''
Parameters:
1. file - alignment file
2. output directory
3. evalue
'''
def parse(file, outputdir,evalue = 0.000331):
   f=open(file,'r')
   reader = csv.reader(f, delimiter='\t', quoting=csv.QUOTE_NONE)
   actual_read = ''
   transposones = {}
   qlen = None
   rowcount = 0
   for row in reader:
   #for line in f.readline():
     #print line
     #row=line.split("\t")
     if row[0]=='#':
       continue
     rowcount +=1
     #if int(row[3]) >=43 and row[1] not in banlist:# and int(row[0])>=31:
     if row[1] not in banlist:
       if row[6] != actual_read:
         actual_read = row[0]
         if row[1] not in transposones:
           #match = re.search('_([0-9]+)[a-z]*$', row[1])
           #if match:
           qlen = int(row[5])
             #print row[0],match.group(1)
           transposones[row[1]] = TransposableElement(qlen,row[1])
         start = int(row[2])
         end = int(row[2])+int(row[3])
         transposones[row[1]].Inc(start,end, rowcount)
   f.close()

   #dump each of the TEs to separate files
   for i in transposones.keys():
     #print i
     eva=str(evalue)
     fout = open(outputdir + i  + '.hits.' + eva,'w')
     transposones[i].Dump(fout, eva)
     fout.close()
   return transposones

if __name__ == "__main__":
  #arguments: input file and e-value treshold and output folder
  if len(sys.argv[1:]) > 1:
    ##1
    inputfile = sys.argv[1]
    ##2
    evalue = float(sys.argv[2])
    ##3
    outputdir = sys.argv[3]
    parse(sys.argv[1], outputdir ,evalue)




















