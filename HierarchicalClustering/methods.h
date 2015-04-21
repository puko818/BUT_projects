#ifndef _methods_h_
#define _methods_h_

#include "clustering.h"

typedef void (*MethodPtr)(GeneAnc*,GeneAnc*,float&);

enum MethodType
{
    PearsonCen = 0,
    PearsonUnc,
    PearsonCenAbs,
    PearsonUncAbs
};


class Methods
{
MethodType type;
void Allocate();
MethodPtr ptr[3];
static void PearsonCorrelationCen(GeneAnc *first, GeneAnc *second, float &correlation);
static void PearsonCorrelationUncen(GeneAnc *first, GeneAnc *second, float &correlation);
static void PearsonCorrelationCenAbs(GeneAnc *first, GeneAnc *second, float &correlation);
static void PearsonCorrelationUncenAbs(GeneAnc *first, GeneAnc *second, float &correlation);

public:
  Methods(MethodType);
  void SetMethod(MethodType);
  MethodPtr GetMethod();

};

#endif
