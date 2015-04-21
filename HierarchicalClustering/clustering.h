#ifndef _clustering_h_
#define _clustering_h_

#include <iostream>
#include <vector>
#include <fstream>
#include <sstream>
#include <valarray>
#include <list>
#include <algorithm>
#include "io.h"
/*#include "methods.h"*/
#include <boost/numeric/ublas/triangular.hpp>
#include <boost/numeric/ublas/io.hpp>
#include "tinyxml.h"
/*Generic class for Cluster a Gene objects*/
using namespace boost::numeric::ublas;

/**
 * Enumeration of linkage methods
 */
enum Linkage
{
  single_lin,
  complete_lin,
  average_lin
};

/**
 * Base class for classes Cluster and Gene, it encapsulates the basic mathematic operations
 * with the gene expression data
 */
class GeneAnc
{
  /*Constructor*/
  public:
 /**
  * Constructor
  * @param _id Identification of the object
  */
    GeneAnc(int _id) : deviation(0.0), average(0.0), id(_id),deviationunc(0.0) {};
    float& operator[](int);
 /**
  * @return Number of items in the float vector, also empty indexes are included
  */
    int Count();
 /**
  * @return Number of non empty items in the float vector
  */
    int Size();
 /**
  * Virtual destructor
  */
    virtual ~GeneAnc() {};
///void (*MethodPtr)(GeneAnc*,GeneAnc*,float&)
 /**
  * Returns an std::list that includes all indexes actually included in the object
  */
    std::list<int>& GetIndexes();
 /**
  * @return Standard deviation
  */
    float Deviation();
 /**
  * @return Modified deviation for uncentered correlation method
  */
    float DeviationUnc();
 /**
  * @return Average of float values in the vector
  */
    float Average();
 /**
  * Pure virtual method
  */
    virtual float compare(GeneAnc *g, void (*MethodPtr)(GeneAnc*,GeneAnc*,float&),std::vector<GeneAnc*>& genes) = 0;
 /**
  * Pure virtual method
  */
    virtual GeneAnc* LeftNode() = 0;
 /**
  * Pure virtual method
  */
    virtual GeneAnc* RightNode() = 0;
 /**
  * @return Name of the object
  */
    std::string GetName();
  /*Protected variables*/
  protected:
 /**
  * protected float vector of gene expressions
  */
   std::vector <float> _v;
 /**
  * protected list of indexes, that are included in the object
  */
   std::list <int> _indexes;
   float deviation;
   float deviationunc;
   float average;
   int id;
   int _nodatacount;
   std::string name;





  /*Protected methods*/
    //virtual void countArray() = 0;

};

/**
 * Implementation of Gene Class, the GeneAnc's descendant
 *
 */

class Gene: public GeneAnc
{
  /*Constructor*/
  public:
  /**
   * Constructor
   * @param loader Pointer to the FileLoader instance, that loads the input data
   * @param index Index for internal representation of this instance
   * @param status Informs about the result of the operation
   */
    Gene(FileLoader *loader, int index,bool& status);
  /**
   * Public compare method
   * @param g pointer to another instance of GeneAnc descendant
   * @param MethodPtr pointer to the similarity measurement method
   * @param genes vector of pointers to Gene instances
   */
    float compare(GeneAnc *g, void (*MethodPtr)(GeneAnc*,GeneAnc*,float&),std::vector<GeneAnc*>& genes);
    void PrintOut();
  /**
   * @return a pointer to the left child
   *
   */
    GeneAnc* LeftNode();
  /**
   * @return a pointer to the right child
   */
    GeneAnc* RightNode();
  /**
   * Gene Destructor
   */
    ~Gene() {};
};

/*---------------------------------------------*/

/**
 * Class Cluster as descendant of class GeneAnc implements a cluster objects that stores all
 * needed information about children, that are contained
 *
 */
class Cluster: public GeneAnc
{
  /*Private variables*/
  GeneAnc *left;
  GeneAnc *right;
  static int cluster_count;
  Linkage link;
 /**
  * Saves the average vector. Average vector is computed as average value vector of all nodes, that are within this cluster object
  * @p reference to the vector of Genes
  */
  void saveAverageVector(std::vector<GeneAnc*> &p);
 /**
  *@return the maximal similarity of included clusters
  */
  float FindMaxSim();
 /**
  *@return the minimal similarity of included clusters
  */
  float FindMinSim();
 /**
  * Converts numeric value to string
  *@return string variable
  */
  std::string numToStr(int);
  /*Constructor*/
  public:
 //   Cluster(): left(NULL),right(NULL) {};
    Cluster(GeneAnc *, GeneAnc *, int , Linkage,std::vector<GeneAnc*>&);
    void SetLinkage(Linkage);
    void PrintIndexes();
    float compare(GeneAnc*, void (*MethodPtr)(GeneAnc*,GeneAnc*,float&),std::vector<GeneAnc*>& genes);
    /**
     * @return left child of the cluster
     *
     */
    GeneAnc *LeftNode();
    /**
     * @return right child of the cluster
     */
    GeneAnc *RightNode();
    /**
     * Destructor
     */
    ~Cluster() {};
};

struct Indexes
{
	int x;
	int y;
};

/*Trojuholnikova matica*/
class Matrix
{
  /*Private members*/
	std::vector<float> _array;
	Indexes CountIndex(int);
	int CountIndex(Indexes);
  public:
  /*Constructor*/
  Matrix();
  /*Public members*/
  /*Metoda vlozi desatinne cislo na zadane miesto*/
  void SetValue(float,Indexes);
  /*Vymaze hodnotu na zadanom mieste*/
  void DeleteValue(Indexes);
  /*Najde najvacsiu hodnotu vo vectore a vrati suradnice*/
  void FindMax(Indexes &);
};

struct Info
{
  private:
   float max_value;
   int position;
   bool empty;

  public:
    Info(float _max, int _pos) : max_value(_max), position(_pos), empty(true) {};
    float Max_Value();
    int Position();
    bool Empty();
    void Actualise(float _max, int pos);
    void Clear(int pos);
    void Max_Value(float _val);
    void Position(int pos);
    void Empty(bool);


};

class TriangMatrix
{

  private:
    triangular_matrix <float, lower> mu;
    std::vector<Info> infos;
    void Actualise(int);
    void ActualiseColummMax(int);
  public:
    void Clear();
    bool IsEmpty(int);
    TriangMatrix(unsigned int);
    void PrintMatrix();
    void PrintVector();
    void SetValue(unsigned int,unsigned int,float);
    void GetValue(int,int,float&);
    void GetMax(int&,int&,bool &status);
    void Clear(int);
};


class XmlSaver
{
    TiXmlDocument doc;
    std::string doc_name;
  public:
    XmlSaver(std::string _name) : doc_name(_name) {};
    void PreOrderSave(GeneAnc*, TiXmlElement *);
    void SaveDendrogram(GeneAnc*);
};

#endif
