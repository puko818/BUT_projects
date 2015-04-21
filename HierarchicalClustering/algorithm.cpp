#include "algorithm.h"

MainApp::MainApp(const std::string &s,std::string output, MethodType type,int col, int row)
{
    loader = new FileLoader(s,col,row);
    saver = new XmlSaver(output);
    this->Init();
    m_template = new TriangMatrix((unsigned int)genes_template.size());
    method = new Methods(type);

}

int MainApp::GenesCount()
{
 return this->genes_template.size();
}

void MainApp::Init()
{
    int i = 0;
    bool status = true;
    while (status)
    {
        Gene *g = new Gene(loader,i,status);
        i++;
        if (status)
        {
            genes_template.push_back(g);
        }
    }

}

void MainApp::CalculateCorrelations()
{
    m_template->Clear();
   // m_working->Clear();
   // m_template->PrintMatrix();
    MethodPtr p = method->GetMethod();
   // int tmp = genes_template.size();
    GeneAnc *tmp = NULL;
    for (unsigned int j = 0; j <= genes_template.size() - 2; j++)
    {
        tmp = genes_template.at(j);
        for (unsigned int i = j+1; i <= genes_template.size() - 1; i++)
        {
            float correlation = tmp->compare(genes_template.at(i),p,this->genes_template);
            m_template->SetValue(i,j,correlation);
        }

    }
    m_working = m_template;
    genes_working = genes_template;
  //  m_template->
}

GeneAnc* MainApp::DoClustering()
{
  bool stat;
  int i_tmp, j_tmp;
  GeneAnc* tmp = NULL;
  //zistime indexy prvkov, medzi ktorymi je najvacsia korelacia
  //m_working->PrintMatrix();
 // m_working->PrintVector();
  m_working->GetMax(i_tmp,j_tmp,stat);
  int i = std::min(i_tmp,j_tmp);
  int j = std::max(i_tmp,j_tmp);
  std::cout << i << "," << j << std::endl;
  if (i == 0 || j == 0)
        int blabla = 6;

  if (stat == true)
  {
  GeneAnc* left = genes_working.at(i);
  GeneAnc* right = genes_working.at(j);

    Cluster *new_node = new Cluster(left, //lavy uzol
                                    right, //pravy uzol
                                    j,                   //novy cluster bude mat ID praveho uzlu
                                    average_lin,         //metoda
                                    genes_template       //odkial brat udaje o genoch
                                   );
   /*if (stat == false)*/ tmp = new_node;
    //poziciu j prepis novym klastrom, poziciu i zmaz z matice podobnosti
    std::vector<GeneAnc*>::iterator I = genes_working.begin();
   // genes_working.erase(I+j);
    genes_working.at(j) = new_node;
    m_working->Clear(i);
    MethodPtr p = method->GetMethod();
    /*for (unsigned int k = 0; k < genes_working.size() - 1; k++)
    {
        GeneAnc *tmp = NULL;
        tmp = genes_working.at(i);
        float correlation = tmp->compare(genes_working.at(j),p,this->genes_template);
        m_template->SetValue(i,j,correlation);
    }*/

    for (int k = 0; k <= genes_working.size() - 1; k++)
    {
        //pokial objekt,s ktorym porovnavame vzniknuty uzol,
        // este existuje
        if (!(m_working->IsEmpty(k)) || k == genes_working.size()-1)
        {
            GeneAnc *tmp = NULL;
            tmp = genes_working.at(k);
            float correlation = new_node->compare(tmp,p,this->genes_template);
            m_working->SetValue(k,j,correlation);
        }
    }

 // m_working->PrintMatrix();
 // m_working->PrintVector();
  }
  return tmp;
}

void MainApp::SetLinkage(Linkage _l)
{
 l = _l;
}

MethodType MainApp::converterCor(int choice)
{
    MethodType type = PearsonCen;
    switch(choice)
    {
       case 0: type = PearsonCen;break;
       case 1: type = PearsonUnc;break;
       case 2: type = PearsonCenAbs;break;
       case 3: type = PearsonUncAbs;break;
       default: type = PearsonCen; break;

    }
    return type;

}


Linkage MainApp::converterLin(int choice)
{
  Linkage lin = average_lin;
  switch(choice)
    {
       case 0: lin = average_lin;break;
       case 1: lin = complete_lin;break;
       case 2: lin = single_lin;break;
       default: lin = average_lin;break;

    }
    return lin;


}
