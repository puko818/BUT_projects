#####
#Collection of SAM,BAM,FASTA,FASTQ and MicroRazers parsers
#####
#import pysam
import re
import sys

#sys.path.append('/storage/brno2/home/ivogel/.local/lib/python2.7/site-packages')
#sys.path.append('/storage/brno2/home/ivogel/.local/lib/python2.7/site-packages')

import pysam


def parseGenomicID(name):
  if name=="*" or name=="NONTE": return None
  head=name.split("|")[0]
  return ("_".join(head.split("_")[:-1]),head)
  

#stare,pomale
def parseGenomicID_(name):
     if name=="*" or name=="NONTE": return None
     head=name.split("|")
     m=re.match(r"(?P<family>.+)_[0-9]+", head[0])
     if m:
       family=m.group("family")
       return  (family,head[0])




class ParseSam(object):
  def __init__(self,filePath):
     self._samfile=pysam.AlignmentFile(filePath,'r')

  def __iter__(self):
     return self


  def next(self):
    elemList=[]
    read=self._samfile.next()
    ref="NONTE"
    if (read.tid != -1):
      ref=self._samfile.getrname(read.tid)
    elemList.append(ref)
    elemList.append(read.query_name)
    elemList.append(read.query_sequence)
    return tuple(elemList)




class ParseBam(object):
  def __init__(self,filePath):
     self._samfile=pysam.AlignmentFile(filePath,'rb')
     self._currentLineNumber=0

  def __iter__(self):
     return self

  
  def next(self):
    elemList=[]
    read=self._samfile.next()
    ref="NONTE"
    if (read.tid != -1):
      ref=self._samfile.getrname(read.tid)
    self._currentLineNumber+=1
    elemList.append(ref)
    elemList.append(read.query_name)
    elemList.append(read.query_sequence)
    #print self._currentLineNumber
    return tuple(elemList)
      
   



'''
samfile=pysam.AlignmentFile(sys.argv[1],'r')
for read in samfile.fetch():
  if read.tid != -1:
    h=samfile.getrname(read.tid)
    h=h.split("|")
    print h[0]
    #print read.seq
samfile.close()
'''

     

class ParseMicroRazers(object):
  def __init__(self,filePath):
     self._file=open(filePath,'rU')
     self._currentLineNumber=0

  def __iter__(self):
     return self

  def next(self):
    elemList=[]
    line=self._file.readline()
    self._currentLineNumber +=1
    if line:
      elems=line.strip('\n').split()
      elemList=(elems[0],elems[4])
    else:
      raise StopIteration
    return elemList

class ParseFasta(object):
  def __init__(self,filePath):
      self._file = open(filePath, 'rU')
      self._currentLineNumber = 0
  def __iter__(self):
    return self

  def next(self):
    # ++++ Get Next Four Lines ++++
    elemList = []
    for i in range(2):
      line = self._file.readline()
      self._currentLineNumber += 1 ## increment file position
      if line:
        elemList.append(line.strip('\n'))
      else: 
        raise StopIteration
      # ++++ Check Lines For Expected Form +++
    return (elemList[0][1:],elemList[1])


class ParseGenomicFasta(ParseFasta):
  def __init__(self,filePath):
      ParseFasta.__init__(self,filePath)
   
  def __iter__(self):
     return self
 
  def next(self):
     t=ParseFasta.next(self)
     head=t[0].split("|")
     sequence=t[1]
     #m=re.match(r"(?P<family>.+)_[0-9]+", head[0])
     #family=m.group("family")
     family=parseGenomicID(head[0])
     return tuple([sequence]+[family[0]]+head)
     #return tuple([sequence]+[family[1:]]+ head)



class ParsesRNACluster(ParseFasta):
  def __init__(self,filepath):
     ParseFasta.__init__(self,filepath)
   
  def __iter__(self):
     return self

  def next(self):
    # ++++ Get Next Four Lines ++++
    elemList = []
    header=self._file.readline()
    self._currentLineNumber += 1
    sequence=self._file.readline()
    self._currentLineNumber += 1
    if header and sequence:
      elemList=elemList+ header.strip('\n').split("|")
      elemList.append(sequence.strip('\n'))
    else:
      raise StopIteration
      # ++++ Check Lines For Expected Form +++
    return tuple(elemList)
     
class ParseFastQ(object):
    """Returns a read-by-read fastQ parser analogous to file.readline()"""
    def __init__(self,filePath,headerSymbols=['@','+']):
        """Returns a read-by-read fastQ parser analogous to file.readline().
        Exmpl: parser.next()
        -OR-
        Its an iterator so you can do:
        for rec in parser:
            ... do something with rec ...
 
        rec is tuple: (seqHeader,seqStr,qualHeader,qualStr)
        """
        if filePath.endswith('.gz'):
            self._file = gzip.open(filePath)
        else:
            self._file = open(filePath, 'rU')
        self._currentLineNumber = 0
        self._hdSyms = headerSymbols
         
    def __iter__(self):
        return self
     
    def next(self):
        """Reads in next element, parses, and does minimal verification.
        Returns: tuple: (seqHeader,seqStr,qualHeader,qualStr)"""
        # ++++ Get Next Four Lines ++++
        elemList = []
        for i in range(4):
            line = self._file.readline()
            self._currentLineNumber += 1 ## increment file position
            if line:
                elemList.append(line.strip('\n'))
            else:
                elemList.append(None)
         
        # ++++ Check Lines For Expected Form ++++
        trues = [bool(x) for x in elemList].count(True)
        nones = elemList.count(None)
        # -- Check for acceptable end of file --
        if nones == 4:
            raise StopIteration
        # -- Make sure we got 4 full lines of data --
        assert trues == 4,\
               "** ERROR: It looks like I encountered a premature EOF or empty line.\n\
               Please check FastQ file near line number %s (plus or minus ~4 lines) and try again**" % (self._currentLineNumber)
        # -- Make sure we are in the correct "register" --
        assert elemList[0].startswith(self._hdSyms[0]),\
               "** ERROR: The 1st line in fastq element does not start with '%s'.\n\
               Please check FastQ file near line number %s (plus or minus ~4 lines) and try again**" % (self._hdSyms[0],self._currentLineNumber)
        assert elemList[2].startswith(self._hdSyms[1]),\
               "** ERROR: The 3rd line in fastq element does not start with '%s'.\n\
               Please check FastQ file near line number %s (plus or minus ~4 lines) and try again**" % (self._hdSyms[1],self._currentLineNumber)
        # -- Make sure the seq line and qual line have equal lengths --
        assert len(elemList[1]) == len(elemList[3]), "** ERROR: The length of Sequence data and Quality data of the last record aren't equal.\n\
               Please check FastQ file near line number %s (plus or minus ~4 lines) and try again**" % (self._currentLineNumber)
         
        # ++++ Return fatsQ data as tuple ++++
        return tuple(elemList)





