#include "mainframe.h"
#include "algorithm.h"
#include <stdexcept>

MainFrame::MainFrame( wxWindow* parent )
:
GUI_MainFrame( parent )
{

}

void MainFrame::OnStartClick( wxCommandEvent& event )
{
	// TODO: Implement OnStartClick
 try
 {
    GeneAnc *rootnode= NULL;
    GeneAnc *tmpnode = NULL;
    int similarity = m_comboBox1->GetCurrentSelection();
    int linkage = m_comboBox2->GetCurrentSelection();
    wxString input = m_filePicker1->GetPath();
    wxString output = m_textCtrl1->GetValue();
    std::string input_clas,output_clas;
    input_clas.append((const char*)input.mb_str());
    output_clas.append((const char*)output.mb_str());
    m_spinCtrl1->GetValue();
    MainApp *main = new MainApp(input_clas,
                                output_clas,
                                MainApp::converterCor(similarity),
                                m_spinCtrl2->GetValue(),
                                m_spinCtrl1->GetValue()
                                );
    int count = main->GenesCount();
    main->SetLinkage(MainApp::converterLin(linkage));
    m_textCtrl2->Clear();
    wxString text1= wxT("Calculating similarity matrix ...\n");
    m_textCtrl2->AppendText(text1);
    main->CalculateCorrelations();
    wxString text2= wxT("Clustering ...\n");
    m_textCtrl2->AppendText(text2);
    while ((tmpnode = main->DoClustering()) != NULL)
    {
      rootnode = tmpnode;
    }
  /*  while (main->DoClustering(rootnode))
    {
    tmp = rootnode;
    }*/
    wxString text3= wxT("Saving to XML ...\n");
    m_textCtrl2->AppendText(text3);
    main->saver->SaveDendrogram(rootnode);
    wxString text4= wxT("Done ...\n");
    m_textCtrl2->AppendText(text4);
    delete main;
  }
  catch(std::exception &e)
  {
      std::cout << "problem" << std::endl;
      m_textCtrl2->AppendText(wxT("Error ocurred, is input file valid?"));
  }
}

void MainFrame::OnCloseClick( wxCommandEvent& event )
{
	Close();
}
