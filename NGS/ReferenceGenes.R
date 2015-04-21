#Script for examining most stable genes (according to their expression) in specific treatment (according to coefficient of variation over control and treatment values)
#the input dataset is the raw count dataset of barley genes set under different treatments


library("edgeR")
library("gplots")
library(raster)


countTable <- read.csv( "/home/ivogel/metacentrum/RNA_seq_barley_Nicolas/results/bam/counts/output", header=TRUE, row.names=1,sep = ";")


treatment=c(rep("cadmium",6),rep("control",18),rep("copper",6),rep("zinc",6))
tissue=c(rep("root",3),rep("shoot",3),rep("root",9),rep("shoot",9),rep("root",3),rep("shoot",3),rep("root",3),rep("shoot",3))
experiment=c(rep(3,6),rep(1,3),rep(2,3),rep(3,3),rep(1,3),rep(2,3),rep(3,3),rep(1,6),rep(2,6))


exprdesign=data.frame(file=colnames(countTable),treatment,tissue,experiment)

exprCus=exprdesign[exprdesign$experiment==1 & exprdesign$tissue=="shoot",]
exprCur=exprdesign[exprdesign$experiment==1 & exprdesign$tissue=="root",]
exprCds=exprdesign[exprdesign$experiment==3 & exprdesign$tissue=="shoot",]
exprCdr=exprdesign[exprdesign$experiment==3 & exprdesign$tissue=="root",]
exprZns=exprdesign[exprdesign$experiment==2 & exprdesign$tissue=="shoot",]
exprZnr=exprdesign[exprdesign$experiment==2 & exprdesign$tissue=="root",]



convertToStr <- function(v1) {
  deparse(substitute(v1))
}

setwd('/home/ivogel/Documents/barley_regulated_genes/')

normalizeCounts <- function(condition,countsT=countTable,outputName)
{
  counts=countsT[as.character(condition$file)]
  y <- DGEList(counts, group=as.character(condition$treatment),genes=rownames(counts))
  keep <- rowSums(cpm(y)>10) >= 2
  y <- y[keep,keep.lib.sizes=FALSE]
  y <- calcNormFactors(y,method="TMM")
  norm <- cpm(y)
  output=sort(apply(norm,1,cv))
  write.table(output,file=outputName,quote=FALSE,sep="\t",col.names=FALSE)
  return (output)
}



normalizedCus<-normalizeCounts(exprCus,countTable,"cus")
normalizedCur<-normalizeCounts(exprCur,countTable,"cur")
normalizedCds<-normalizeCounts(exprCds,countTable,"cds")
normalizedCdr<-normalizeCounts(exprCdr,countTable,"cdr")
normalizedZns<-normalizeCounts(exprZns,countTable,"zns")
normalizedZnr<-normalizeCounts(exprZnr,countTable,"znr")







