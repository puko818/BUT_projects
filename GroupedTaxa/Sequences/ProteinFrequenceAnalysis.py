'''
Created on 20.4.2011

@author: Ivan Vogel
'''
from Sequences import SequenceDecorator

params = { 'IgnoreGaps': 1
          }


class ProteinFrequenceAnalysis(FrequenceAnalysis.FrequenceAnalysis):
    '''
    classdocs
    '''
    
    def __init__(self,decorated):
        '''
        Constructor
        '''
        FrequenceAnalysis.FrequenceAnalysis.__init__(self,decorated)
        FrequenceAnalysis.FrequenceAnalysis.__do = self.__do
        
    
    def __do(self):
        An=Bn=Cn=Dn=En=Fn=Gn=Hn=In=Jn=Kn=Ln=Mn=Nn=On=Pn=Qn=Rn=Sn=Tn=Un=Vn=Wn=Yn=Zn=Xn=0
        frequencies = []
        for column in self.decorated:
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
                sum = len(self.decorated.getSequences())
            if sum == 0:
                frequencies.append((0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0,0.0))
            else:
                frequencies.append((float(An)/sum,float(Bn)/sum,float(Cn)/sum,float(Dn)/sum,float(En)/sum,float(Fn)/sum,float(Gn)/sum,
                float(Hn)/sum,float(In)/sum,float(Jn)/sum,float(Kn)/sum,float(Ln)/sum,float(Mn)/sum,float(Nn)/sum,float(On)/sum,
                float(Pn)/sum,float(Qn)/sum,float(Rn)/sum,float(Sn)/sum,float(Tn)/sum,float(Un)/sum,float(Vn)/sum,float(Wn)/sum,
                float(Yn)/sum,float(Zn)/sum,float(Xn)/sum))
            An=Bn=Cn=Dn=En=Fn=Gn=Hn=In=Jn=Kn=Ln=Mn=Nn=On=Pn=Qn=Rn=Sn=Tn=Un=Vn=Wn=Yn=Zn=Xn=0
        self.frequences = frequencies
        
if __name__ == "__main__":    
    example = ['ABCDEFGH']
    from Sequences import GenericSequence
    basic_seq = GenericSequence.GenericSequence(example)
    freqanal = ProteinFrequenceAnalysis(basic_seq)
    print freqanal
    
        