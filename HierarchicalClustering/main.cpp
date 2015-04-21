#ifndef WX_PRECOMP 
#include "wx/wx.h" 
#endif 

#include "wx/wxprec.h"
#include "mainframe.h"

class MyApp: public wxApp 
{
public: 
  bool OnInit(); 
};

IMPLEMENT_APP(MyApp)

bool MyApp::OnInit()
{
  MainFrame *frame = new MainFrame(NULL);
  frame->Show( TRUE );
  return TRUE;
}
