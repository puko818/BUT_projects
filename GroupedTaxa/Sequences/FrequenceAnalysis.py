'''
Created on 19.1.2011

@author: Ivan Vogel
'''

from Sequences import SequenceDecorator
from Sequences import GenericSequence

params = { 'IgnoreGaps': 1
          }


class FrequenceAnalysis(SequenceDecorator.SequenceDecorator):
    def __init__(self, decorated,type):
        self.decorated = decorated
        if type is "N":
            self.__do = nucleotide_analysis
        else:
            self.__do = protein_analysis
        self.__do(self)
        
    
    def __iter__(self):
        #return self.decorated.__iter__()
        self.position=0
        self.maxpos = len(self.frequences)
        return self
    
    def next(self):
        if self.position > (self.maxpos-1):
            raise StopIteration
        try:
            actual = self.frequences[self.position]
        except IndexError:
            actual = ('X','X')
        self.position+= 1
        return actual
    
    def __len__(self):
        return len(self.frequences)
    
    
def protein_analysis(obj):
        An=Bn=Cn=Dn=En=Fn=Gn=Hn=In=Jn=Kn=Ln=Mn=Nn=On=Pn=Qn=Rn=Sn=Tn=Un=Vn=Wn=Yn=Zn=Xn=0
        frequencies = []
        for column in obj.decorated:
            for s in column:
                An += (s=='A')
                Bn += (s=='B')
                Cn += (s=='C')
                Dn += (s=='D')
                En += (s=='E')
                Fn += (s=='F')
                Gn += (s=='G')
                Hn += (s=='H')
                In += (s=='I')
                Jn += (s=='J')
                Kn += (s=='K')
                Ln += (s=='L')
                Mn += (s=='M')
                Nn += (s=='N')
                On += (s=='O')
                Pn += (s=='P')
                Qn += (s=='Q')
                Rn += (s=='R')
                Sn += (s=='S')
                Tn += (s=='T')
                Un += (s=='U')
                Vn += (s=='V')
                Wn += (s=='W')
                Yn += (s=='Y')
                Zn += (s=='Z')
                Xn += (s=='X')
            #print Tn,Cn,Gn,An
            if params['IgnoreGaps']:
                sum = An+Bn+Cn+Dn+En+Fn+Gn+Hn+In+Jn+Kn+Ln+Mn+Nn+On+Pn+Qn+Rn+Sn+Tn+Un+Vn+Wn+Yn+Zn+Xn
            else:
                sum = len(obj.decorated.getSequences())
            if sum == 0:
                frequencies.append((0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0))
            else:
                frequencies.append((float(An)/sum,float(Bn)/sum,float(Cn)/sum,float(Dn)/sum,float(En)/sum,float(Fn)/sum,float(Gn)/sum,
                float(Hn)/sum,float(In)/sum,float(Jn)/sum,float(Kn)/sum,float(Ln)/sum,float(Mn)/sum,float(Nn)/sum,float(On)/sum,
                float(Pn)/sum,float(Qn)/sum,float(Rn)/sum,float(Sn)/sum,float(Tn)/sum,float(Un)/sum,float(Vn)/sum,float(Wn)/sum,
                float(Yn)/sum,float(Zn)/sum,float(Xn)/sum))
            An=Bn=Cn=Dn=En=Fn=Gn=Hn=In=Jn=Kn=Ln=Mn=Nn=On=Pn=Qn=Rn=Sn=Tn=Un=Vn=Wn=Yn=Zn=Xn=0
        obj.frequences = frequencies


def nucleotide_analysis(obj):
        Tn=Cn=Gn=An =0
        frequencies = []
        for column in obj.decorated:
            for s in column:
                Tn += (s=='T')
                Cn += (s=='C')
                An += (s=='A')
                Gn += (s=='G')
            #print Tn,Cn,Gn,An
            if params['IgnoreGaps']:
                sum = Tn + Cn + An + Gn
            else:
                sum = len(obj.decorated.getSequences())
            if sum == 0:
                frequencies.append((0.0,0.0,0.0,0.0))
            else:
                frequencies.append((float(Tn)/sum,float(Cn)/sum,float(An)/sum,float(Gn)/sum))
            Tn=Cn=Gn=An =0
        obj.frequences = frequencies
         
if __name__ == "__main__":    
 
    example = ['ABCDEFGH','HGFEDSBA']
    basic_seq = GenericSequence.GenericSequence(example)
    freqanal = FrequenceAnalysis(basic_seq,"P")
    print freqanal