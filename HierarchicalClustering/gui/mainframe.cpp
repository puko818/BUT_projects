#include "mainframe.h"
#include "algorithm.h"


MainFrame::MainFrame( wxWindow* parent )
:
GUI_MainFrame( parent )
{

}

void MainFrame::OnStartClick( wxCommandEvent& event )
{
	// TODO: Implement OnStartClick
    //m_filePicker1
    GeneAnc *rootnode= NULL;
    MainApp *main = new MainApp("10","output.xml");
    int count = main->GenesCount();
    main->CalculateCorrelations();
    while ((rootnode = main->DoClustering()) == NULL)
    {}
  /*  while (main->DoClustering(rootnode))
    {
    tmp = rootnode;
    }*/
    main->saver->SaveDendrogram(rootnode);
}

void MainFrame::OnCloseClick( wxCommandEvent& event )
{
	Close();
}
