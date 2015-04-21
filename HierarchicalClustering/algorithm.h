#ifndef _algorithm_h_
#define _algorithm_h_

#include "clustering.h"
#include "io.h"
#include "methods.h"
#include <vector>
#include <algorithm>


 /**
  * Main Application Class, its purpose is to operate the whole clustering algorithm
  * with its public methods
  *
  *
  */
class MainApp
{
  public:
  /**
   * A constructor.
   * @param input is name of input data file with gene expressions
   * @param output is name of output XML file
   * @param MethodType is similarity metric type
   */
    MainApp(const std::string &input,std::string output,MethodType = PearsonUnc,int col=4,int row=2);
  /**
   * Similarity matrix calculation method
   * Calculates correlation between all genes and fills in the instance of TriangMatrix class
   */
    void CalculateCorrelations();
  /**
   * Provides one step of the clustering method
   * @return is the cluster actually created from two nearest objects
   */
    GeneAnc* DoClustering();

  /**
   * Public Method
   * @return number of loaded genes
   */
    int GenesCount();

  /**
   * Sets the linkage type
   * @param type of linkage method
   *
   */
    void SetLinkage(Linkage _l);
  /**
   * Converts the  type linkage type
   * @param choice number of choice, that was selected by gui
   * @return is the converted method enumeration type for internal app purpose
   */
     static MethodType converterCor(int choice);
  /**
   * Converts the linkage type
   * @param choice number of choice, that was selected by gui
   * @return is the converted linkage enumeration type for internal app purpose
   */
     static Linkage converterLin(int choice);

  /**
   * Instance of an XmlSaver class represented as public data structure
   */
    XmlSaver *saver;
  private:
  /**
   * Instance of an FileLoader class represented as private data structure
   */
    FileLoader *loader;

  /**
   *Private vector of pointers to GeneAnc
   */
    std::vector<GeneAnc*> genes_template;
  /**
   *Private vector of pointers to GeneAnc
   */
    std::vector<GeneAnc*> genes_working;
  /**
   * Instance of pointer to TriangMatrix structure, saves distances between Genes
   */
    TriangMatrix *m_template;
  /**
   * Instance of pointer to TriangMatrix structure, basicly the whole algorithm depends on this structure
   */
    TriangMatrix *m_working;
  /**
   * Initialisation private method, called from constructor
   */
    void Init();
  /**
   * Instance of pointer to similarity metrics object
   */

    Methods *method;
 /**
  * Instance of enumeration type that store the information about used linkage method
  */
    Linkage l;
};
#endif
