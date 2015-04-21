'''
Created on 21.4.2011

@author: Ivan Vogel
'''


def extractGroup_gypExyr(fasta_head):
    return fasta_head[fasta_head.find("gypE"):fasta_head.find("gypE")+7]
