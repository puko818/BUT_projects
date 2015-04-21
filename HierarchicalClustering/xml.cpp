#include "clustering.h"


void XmlSaver::PreOrderSave(GeneAnc *node, TiXmlElement *xmlfather)
{
   if (node != NULL)
   {
      std::string tmp = node->GetName();
      TiXmlElement * newnode = new TiXmlElement( tmp.c_str() );
	  xmlfather->LinkEndChild( newnode );
      this->PreOrderSave(node->LeftNode(),newnode);
      this->PreOrderSave(node->RightNode(),newnode);
   }

}

void XmlSaver::SaveDendrogram(GeneAnc *root)
{
    std::string tmp;
    tmp = root->GetName();
  	TiXmlElement * xmlroot = new TiXmlElement( tmp.c_str() );
	doc.LinkEndChild( xmlroot );
    PreOrderSave(root->LeftNode(),xmlroot);
    PreOrderSave(root->RightNode(),xmlroot);
    doc.SaveFile( doc_name.c_str() );
}
