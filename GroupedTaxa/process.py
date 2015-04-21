'''
Created on 25.1.2011

@author: Ivan Vogel
'''


import zipfile
import os
import random
from cogent import LoadSeqs,DNA
from cogent.core.moltype import DNA


#import shutil
#from cogent.app.clustalw import align_unaligned_seqs as clustalw_align_unaligned_seqs 

params = {'extract' :0,
          'to_file': 1,
          'load': 1
          }

''''
fh = open('foo.zip', 'rb')
z = zipfile.ZipFile(fh)
for name in z.namelist():
    outfile = open(name, 'wb')
    outfile.write(z.read(name))
    outfile.close()
fh.close()

'''

input_path = r'/home/puko/Desktop/mtDNA/nations'
output_path = r'/home/puko/Desktop/mtDNA/nations/extracted'
final_path = r'/home/puko/Desktop/mtDNA/nations/final'
test_path = r'/home/puko/Desktop/mtDNA/nations/test'
destination_path = final_path + "/seqs.fasta"
aligned_path = r'/home/puko/Desktop/mtDNA/nations'
files =  os.listdir(input_path)
prefixes = os.listdir(output_path)
all_sequence_names = dict()
#print files


if params['extract']:  
    for file in files:
        if file.endswith('.zip'):
            print "Processing file",file
            f_zipped = open(input_path + '/' + file,'rb' )
            z = zipfile.ZipFile(f_zipped)
            z.extractall(output_path)
            f_zipped.close()        
 

if params['to_file']:    
    destination_file = open(destination_path,"w")
    #loop group names
    for prefix in prefixes:
        all_sequence_names[prefix]=[]
        actual_path = output_path + "/" + prefix
        content = os.listdir(actual_path)
        for i,file in enumerate(content):
            file_path =  actual_path+'/'+file
            source = open(file_path,"r")
            for j,line in enumerate(source):
                if j ==0:
                    id = ">" + prefix + "|" + file[:-4] +  "\n"
                    destination_file.write(id)
                    all_sequence_names[prefix].append(id.rstrip())
                destination_file.write(line)
            source.close()
            destination_file.write("\n")
    destination_file.close()
  
print 'Choose groups:'
for i,prefix in enumerate(all_sequence_names.keys()):
    print '{0}. {1} - {2} sequencies'.format(i,prefix,len(all_sequence_names[prefix]))


print "\nYour choice:",
selected = input()
selected = list(selected)        
#print selected

#vyber sekvencii
values = all_sequence_names.keys()


from cogent.parse.fasta import MinimalFastaParser
f=open(destination_path)
#seqs = [(name, seq) for name, seq in MinimalFastaParser(f)]
#seqs = {name:seq for name,seq in MinimalFastaParser(f)}
seqs = dict()
for name,seq in MinimalFastaParser(f):
    seqs[name]=seq[7900:8100]
#print seqs[all_sequence_names[values[1]]]
to_analyse = dict()
for i in selected:
    for sequence in all_sequence_names[values[i]]:#random.sample(all_sequence_names[values[i]],min(15,len(all_sequence_names[values[i]]))):
        #print sequence,seqs[sequence[1:]]
        to_analyse[sequence[1:]]= seqs[sequence[1:]]
    #print random.sample()
    



unaligned_seqs = LoadSeqs(data=to_analyse,aligned=False,moltype=DNA)
unaligned_seqs.writeToFile(final_path+ '/$australia_oceania_shorten.fasta', format = "FASTA")










                    
                
                
            
            
            

                   
