using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.IO;
using System.Collections;

//Reader class for reading the microarray data matrix
namespace SOM.implementation
{
    class Reader
    {
        private StreamReader stream = null;
        //data start position
        private int linepos = 3;
        private int columnpos = 5;
        private Hashtable table = null;
        private int _size = -1;

        public Hashtable Table
        {
            get
            {
                return table;
            }
        }

        public int Size
        {
            get
            {
                if (this._size < 0 || this.table == null) throw (new System.Exception("Error input vector length!"));
                return this._size;

            }
        }
        
        public Reader(string filename)
        {
            try
            {
                this.stream = new StreamReader(new FileStream(filename, FileMode.Open));
                table = new System.Collections.Hashtable();

            }
            catch (System.Exception ex)
            {

                System.Windows.Forms.MessageBox.Show(ex.Message);
            }

        }

        public void ReadFile()
        {
            //
            try
            {
                for (int i = 1; i < linepos; i++)
                {
                    if (!stream.EndOfStream)
                        stream.ReadLine();
                }

                while (!stream.EndOfStream)
                {

                    string s = stream.ReadLine();
                    string[] ar = s.Split('\t');
                    double[] values = new double[ar.Length];
                    string name = ar[0];
                    int j = 0;
                    
                    System.Globalization.NumberFormatInfo f = new System.Globalization.NumberFormatInfo();
                    f.NumberGroupSeparator = ".";


                    for (int i = columnpos-1; i < ar.Length; i++)
                    {
                        string test = ar[i];
                        if (test == "")
                        {//value is missing
                            values[j++] = Double.NaN;
                        }
                        else values[j++] = Double.Parse(ar[i], f);         
                    }
                    //IEnumerator e = ar.GetEnumerator

                    this.table.Add(name, values);
                    if (this._size < 0) this._size = values.Length;
                }
                //this.test();
            }
            catch (System.Exception ex)
            {
                System.Windows.Forms.MessageBox.Show(ex.Message);
            }
            
        }

        //length of the output vector
        private void setSize()
        {

        }
    }
}
