#include <iostream>
#include <vector>
#include <list>
#include <fstream>
#include <sstream>
#include <valarray>
#include <cmath>
#include "clustering.h"
//#define X 3
//#define Y 5


/*Bazova trieda objektov Cluster a Gene*/


/*Pristupove metody*/
float GeneAnc::Deviation()
{
	float sum = 0.0;
	if (deviation == 0.0)
	{
		for (unsigned int i = 0; i < _v.size(); i++)
		{
			sum += pow(_v[i] - Average(),2);
		}
		deviation = sqrt(sum/_v.size());
	}
	return deviation;
}

float GeneAnc::DeviationUnc()
{
	float sum = 0.0;
	if (deviationunc == 0.0)
	{
		for (unsigned int i = 0; i < _v.size(); i++)
		{
			sum += pow(_v[i],2);
		}
		deviationunc = sqrt(sum/_v.size());
	}
	return deviationunc;
}

float GeneAnc::Average()
{
	if (average == 0.0)
	{
        float sum;
        for (std::vector<float>::iterator I = _v.begin(); I != _v.end(); I++)
        {
            if (*I > -100.0) sum += *I;
        }
		average = sum / (_v.size() - _nodatacount);
	}
	return average;
}

float& GeneAnc::operator [](int i)
{
	return _v[i];
}

int GeneAnc::Size()
{
 return _v.size();
}

int GeneAnc::Count()
{
 return (_v.size() - _nodatacount);

}

std::list<int>& GeneAnc::GetIndexes()
{
    return _indexes;
}

std::string GeneAnc::GetName()
{
    return name;
}

/*-----------------------------*/
/*implementacia triedy Gene*/
Gene::Gene(FileLoader *loader, int index,bool &status) : GeneAnc(index)
{
    status = loader->FillDataStruct(name,_v,_nodatacount);
    if (status) _indexes.push_back(index);
}

float Gene::compare(GeneAnc *g, void (*FunPtr)(GeneAnc*,GeneAnc*,float&),std::vector<GeneAnc*>& genes)
{
    float ret;
    FunPtr(this,g,ret);
    return ret;
}

void Gene::PrintOut()
{
  std::cout << name << " ";
  for (std::vector<float>::iterator I = _v.begin(); I != _v.end(); I++ )
  {
      if (I == (_v.begin()-1)) std::cout << *I << std::endl << std::endl;
      else std::cout << *I << std::endl;//";";
  }


}

GeneAnc* Gene::LeftNode()
{
  return NULL;
}

GeneAnc* Gene::RightNode()
{
  return NULL;
}

int Cluster::cluster_count = 0;

Cluster::Cluster(GeneAnc *l, GeneAnc *p, int _id, Linkage _link,std::vector<GeneAnc*>& genes) : GeneAnc(_id), left(NULL),right(NULL)
{
    cluster_count++;
    name = this->numToStr(cluster_count);
    link = _link;
    left = l;
    right = p;
    std::list<int> lvect = l->GetIndexes();
    std::list<int> pvect = p->GetIndexes();
    std::list<int>::iterator It = _indexes.begin();
    _indexes.insert(It,lvect.begin(),lvect.end());
    _indexes.insert(It, pvect.begin(),pvect.end());
    if (link == average_lin) saveAverageVector(genes);
}


GeneAnc* Cluster::LeftNode()
{
  return this->left;
}

GeneAnc* Cluster::RightNode()
{
 return this->right;
}

void Cluster::PrintIndexes()
{
   for (std::list<int>::iterator I = _indexes.begin(); I != _indexes.end(); I++)
   {
     std::cout<< name << ":";
     std::cout << *I << std::endl;

   }

}

void Cluster::SetLinkage(Linkage newl)
{
  link = newl;
}

void Cluster::saveAverageVector(std::vector<GeneAnc*> &v)
{
    int size = (v.at(0))->Count();
    for (int i = 0; i < size; i++)
    {
        int count = 0;
        float tmp_sum = 0.0;
        for (std::list<int>::iterator I = _indexes.begin(); I != _indexes.end(); I++)
        {
          if ((*(v.at(*I)))[i] == -100.0) break;
          else
            {
              tmp_sum += (*(v.at(*I)))[i];
              count++;
            }
        }
        if (count == 0) _v.push_back(-100.0);//_v[i] = -100.0;
        else            _v.push_back(tmp_sum/count);//_v[i] = (float)(tmp_sum/count);
    }

}

std::string Cluster::numToStr(int id)
 {
  	std::stringstream stream1;
  	std::string name("node");
  	std::string tmp;
    stream1.clear();
    stream1 << id;
    stream1 >> tmp;
    name = name + tmp;
    return name;

 }


float Cluster::compare(GeneAnc *g, void (*FunPtr)(GeneAnc*,GeneAnc*,float&), std::vector<GeneAnc*>& genes)
{
    float ret;
    std::vector<float>::iterator ReTi;
    if (link != average_lin)
    {
      std::vector<float> values;
      std::list <int> comparingGene = g->GetIndexes();
        for (std::list<int>::iterator I = this->_indexes.begin();
             I != this->_indexes.end();
             I++)
        {
            for (std::list<int>::iterator J = comparingGene.begin();
                 J != comparingGene.end();
                 J++)
            {
                float value;
                FunPtr(genes.at(*I),genes.at(*J),value);
                values.push_back(value);
            }
        }
        if (link == single_lin)
        {
            ReTi = max(values.begin(),values.end());
            ret = *ReTi;
        }
        else
        {
            ReTi = min(values.begin(),values.end());
            ret = *ReTi;
        }
    }

    else
    {
        FunPtr(this,g,ret);
    }

    return ret;
}

Indexes Matrix::CountIndex(int index)
{
    int i = 1;
    int tmp_index = 0;
    Indexes tmp;
    tmp.x = 0;

    if (index == 0)
    {
      tmp.y = 0;
    }

    else
    {
        do
        {
          tmp_index += i;
          i++;
        }
        while (tmp_index+i-1 < index);

        tmp.y = i;
        tmp.x = index - tmp_index;
    }
    return tmp;
}

int Matrix::CountIndex(Indexes I)
{

	int i = 0;
	int sum = 0;

	while (i < I.y)
	{
		sum += i++;
	}

	return (sum + I.x);
}

void Matrix::DeleteValue(Indexes pos)
{

    int index = CountIndex(pos);
    _array.erase(_array.begin() + index);
}

void Matrix::SetValue(float f,Indexes pos)
{
   int index = CountIndex(pos);
   _array.insert(_array.begin() + index,f);
}

void Info::Actualise(float _max, int pos)
{
   max_value = _max;
   position = pos;
   empty = false;
}

float Info::Max_Value()
{
  return max_value;
}

int Info::Position()
{
  return position;
}

bool Info::Empty()
{
  return empty;
}

void Info::Max_Value(float _val)
{
  max_value = _val;
}

void Info::Position(int _pos)
{
  position = _pos;
}

void Info::Empty(bool _b)
{
  empty = _b;
}




TriangMatrix::TriangMatrix(unsigned int _size)
{
    //infos(_size);
    triangular_matrix <float, lower> mv(_size,_size);
    mu = mv;
    Info inf(-100.0,-1);
    std::vector<Info> infos2(_size,inf);
    infos = infos2;
}

void TriangMatrix::Clear()
{
 mu.clear();
}

void TriangMatrix::PrintMatrix()
{
 std::cout << mu << std::endl;
}

void TriangMatrix::PrintVector()
{
 int i = 0;
 for (std::vector<Info>::iterator I = infos.begin(); I != infos.end(); I++,i++)
 {
    std::cout << "Pozicia c." << i << std::endl;
    if ((*I).Empty()) std::cout << "prazdny,";
    else std::cout << "neprazdny,";
    std::cout << (*I).Max_Value() << ",";
    std::cout << (*I).Position() << std::endl;


 }
}

void TriangMatrix::SetValue(unsigned int i, unsigned int j, float f)
{
  if ( i == j) return;
  if (i < j) std::swap(i,j);
  mu(i,j) = f;
  (infos.at(j)).Empty(false);
  if (f >= (infos.at(j)).Max_Value())
    {
       (infos.at(j)).Max_Value(f);
       (infos.at(j)).Position(i);
    }
}

void TriangMatrix::GetMax(int &row, int &col, bool &status)
{
   status = true;
   int tmp_i = 0, tmp_j = 0, j = 0;
   float tmp_value = -10;
   std::vector<Info>::iterator tmp_iterator;
   int noemptycol = 0;
   for (std::vector<Info>::iterator I = infos.begin(); I != infos.end(); I++, j++)
    {
        if (!((*I).Empty()))
        {
          //noemptycol++;
          if ((*I).Max_Value() >= tmp_value)
          {
           noemptycol++;
           tmp_iterator = I;
           tmp_value = (*I).Max_Value();
           tmp_i = (*I).Position();
           tmp_j = j;
          }
        }
        /*
        if (!((*I).Empty()) && (*I).Max_Value() >= tmp_value)
        {
           noemptycol++;
           tmp_iterator = I;
           tmp_value = (*I).Max_Value();
           tmp_i = (*I).Position();
           tmp_j = j;

        }*/
    }

    row = tmp_i;
    col = tmp_j;
    if (/*noemptycol == 1 ||*/ noemptycol == 0) status = false;
}

bool TriangMatrix::IsEmpty(int index)
{
   return infos.at(index).Empty();
}

void TriangMatrix::Actualise(int index)
{


}


void TriangMatrix::ActualiseColummMax(int pos)
{//prejdenie stlpca tabulky
    float tmp_max = -10.0;
    float tmp = 0;
    for (unsigned int i = pos + 1; i < this->mu.size1(); i++)
    {
        if (!(this->infos.at(i).Empty()) || i == this->mu.size1()-1)
        {
          tmp = this->mu(i,pos);
          if (tmp >= tmp_max)
          {
              this->infos.at(pos).Actualise(tmp, i);
              tmp_max = tmp;
          }
          if (i == this->mu.size1() - 1) mu(i,pos) = -100.0;
        }
    }
}

void TriangMatrix::Clear(int index)
{
   (infos.at(index)).Empty(true);
   (infos.at(index)).Max_Value(-100.0);
   /*if (index == this->mu.size2()-1)
   {//maze sa posledny prvok
        for (int j = 0; j < infos.size(); j++)
        {
         mu(index,j) = -100;
         ActualiseColummMax(j);
        }
   }*/
   if (index != 0)
   {
     for (int i = 0; i <= index - 1; i++)
     {
        if (!(infos.at(i).Empty()) && infos.at(i).Position() == index)
        {//ked najdeme poziciu, ktora hovori, ze na mazanom indexe je najvacsi prvok
         //treba prehladat cely tento stlpec a najst nove maximum
            ActualiseColummMax(i);
        }
     }
   }

}
