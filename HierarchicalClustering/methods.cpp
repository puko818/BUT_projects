#include <vector>
#include <algorithm>
#include "methods.h"



Methods::Methods(MethodType t)
{
    Allocate();
    type = t;
}

void Methods::PearsonCorrelationCen(GeneAnc *first, GeneAnc *second, float &correlation)
{
    correlation = 0;
    float sum = 0.0;
    int bound = std::min(first->Size(),second->Size());
    for (int i = 0; i <= bound; i++)
    {
        if ((*first)[i] == -100.0 || (*second)[i]== -100.0) break;
        sum += (((*first)[i] - first->Average()) / first->Deviation()) *
        (((*second)[i] - second->Average()) / second->Deviation());
    }

		correlation = (sum / first->Count());
}

void Methods::PearsonCorrelationUncen(GeneAnc *first, GeneAnc *second, float &correlation)
{
    correlation = 0;
    float sum = 0.0;
    int bound = std::min(first->Size(),second->Size());
    for (int i = 0; i <= bound; i++)
    {
        if ((*first)[i] == -100.0 || (*second)[i]== -100.0) break;
        sum += (((*first)[i]) / first->DeviationUnc()) *
        (((*second)[i]) / second->DeviationUnc());
    }

		correlation = (sum / first->Count());
}


void Methods::PearsonCorrelationUncenAbs(GeneAnc *first, GeneAnc *second, float &correlation)
{
  Methods::PearsonCorrelationUncen(first,second,correlation);
  correlation = std::abs(correlation);
}

void Methods::PearsonCorrelationCenAbs(GeneAnc *first, GeneAnc *second, float &correlation)
{
  Methods::PearsonCorrelationCen(first,second,correlation);
  correlation = std::abs(correlation);
}

void Methods::Allocate()
{
   ptr[0] = &PearsonCorrelationUncen;
   ptr[1] = &PearsonCorrelationCen;
   ptr[2] = &PearsonCorrelationUncenAbs;
   ptr[3] = &PearsonCorrelationCenAbs;

}

void Methods::SetMethod(MethodType t)
{

}

MethodPtr Methods::GetMethod()
{
    return (ptr[type]);
}

