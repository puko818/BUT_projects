///////////////////////////////////////////////////////////////////////////
// C++ code generated with wxFormBuilder (version Apr 16 2008)
// http://www.wxformbuilder.org/
//
// PLEASE DO "NOT" EDIT THIS FILE!
///////////////////////////////////////////////////////////////////////////

#ifndef __gui__
#define __gui__

#include <wx/string.h>
#include <wx/stattext.h>
#include <wx/gdicmn.h>
#include <wx/font.h>
#include <wx/colour.h>
#include <wx/settings.h>
#include <wx/filepicker.h>
#include <wx/spinctrl.h>
#include <wx/sizer.h>
#include <wx/statline.h>
#include <wx/combobox.h>
#include <wx/textctrl.h>
#include <wx/button.h>
#include <wx/panel.h>
#include <wx/frame.h>

///////////////////////////////////////////////////////////////////////////


///////////////////////////////////////////////////////////////////////////////
/// Class GUI_MainFrame
///////////////////////////////////////////////////////////////////////////////
class GUI_MainFrame : public wxFrame 
{
	private:
	
	protected:
		wxPanel* m_panel1;
		wxStaticText* m_staticText1;
		wxFilePickerCtrl* m_filePicker1;
		wxStaticText* m_staticText2;
		wxSpinCtrl* m_spinCtrl1;
		wxStaticText* m_staticText3;
		wxSpinCtrl* m_spinCtrl2;
		wxStaticLine* m_staticline2;
		wxStaticText* m_staticText10;
		wxComboBox* m_comboBox1;
		wxStaticText* m_staticText11;
		wxComboBox* m_comboBox2;
		wxStaticText* m_staticText6;
		wxTextCtrl* m_textCtrl1;
		wxTextCtrl* m_textCtrl2;
		wxStaticLine* m_staticline6;
		wxButton* m_button1;
		wxButton* m_button3;
		
		// Virtual event handlers, overide them in your derived class
		virtual void OnStartClick( wxCommandEvent& event ){ event.Skip(); }
		virtual void OnCloseClick( wxCommandEvent& event ){ event.Skip(); }
		
	
	public:
		GUI_MainFrame( wxWindow* parent, wxWindowID id = wxID_ANY, const wxString& title = wxT("Hierarchical clustering"), const wxPoint& pos = wxDefaultPosition, const wxSize& size = wxSize( 500,500 ), long style = wxDEFAULT_FRAME_STYLE|wxTAB_TRAVERSAL );
		~GUI_MainFrame();
	
};

#endif //__gui__
