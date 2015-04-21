using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;

namespace SOM
{
    public partial class Details : Form
    {
        public Details()
        {
            InitializeComponent();
        }

        public void InsertText(string[] text)
        {
            //this.textBox1.Text = text;
            this.textBox1.Lines = text;
            
        }
    }
}
