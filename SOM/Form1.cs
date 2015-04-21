using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Linq;
using System.Text;
using System.Windows.Forms;
using SOM.implementation;

using System.IO;
using System.Threading;

namespace SOM
{
    public partial class Form1 : Form
    {
        private bool clicked = false;
        
        public Form1()
        {
            InitializeComponent();
        }

        private void button1_Click(object sender, EventArgs e)
        {
            try
            {
                SOM.implementation.Map map = new SOM.implementation.Map();
                map.Clear();
                map.Initialize(10, 10, 3);
                this.dataGridView1.Rows.Clear();
                this.dataGridView1.Columns.Clear();
                
                this.dataGridView1.ColumnCount = 10;
                this.dataGridView1.Rows.Add(9);
                this.dataGridView1[0, 0].Selected = false;
                
                for (int i = 0; i < map.Neurons.GetLength(0); i++)
                {



                    for (int j = 0; j < map.Neurons.GetLength(1); j++)
                    {
                        DataGridViewCell cell = new DataGridViewTextBoxCell();
                        // this.dataGridView1.

                        this.dataGridView1[j, i].Value = (map.Neurons[i, j] as Neuron).ID;
                        this.dataGridView1[j, i].Tag = map.Neurons[i, j];
                        //this.dataGridView1[j, i] = cell;
                        //this.dataGridView1.Rows.Add();

                    }
                }
                System.Collections.ArrayList a = new System.Collections.ArrayList();
                this.dataGridView1[4, 4].Selected = true;             
                int dist = Int16.Parse(this.textBox2.Text);
                a.Add(map.Neurons[4, 4]);
                map.GetNeighbourhood(dist, map.Neurons[4, 4] as Neuron, a);
               
                string text = null;
                foreach (Neuron n in a)
                {
                    text = text + n.ID.ToString() + ";";

                }
                this.textBox1.Text = text;
            }
            catch (System.Exception ex)
            {
                System.Windows.Forms.MessageBox.Show(ex.Message);
            }
        }

        private void dataGridView1_CellContentClick(object sender, DataGridViewCellEventArgs e)
        {

        }



        private void textBox2_TextChanged(object sender, EventArgs e)
        {

        }

        private void label1_Click(object sender, EventArgs e)
        {

        }

        private void backgroundWorker1_DoWork(object sender, DoWorkEventArgs e)
        {

        }

        private void folderBrowserDialog1_HelpRequest(object sender, EventArgs e)
        {

        }

        private void button2_Click(object sender, EventArgs e)
        {
            this.openFileDialog1.ShowDialog();

        }


        // This delegate tells which function to call. It matches the signature
        // of our UpdateProgress function. During the invoke in ReadFile, we give it
        // the function to call which matches. In this case UpdateProgress.

        public delegate void updatebar();

        // This will run in the main thread so it can update the controls for us.
        private void UpdateProgress()
        {
            if (progressBar1.Value == progressBar1.Maximum)
                progressBar1.Value = 0;
            else
            progressBar1.Value += 1;

            // Here we are just updating a label to show the progressbar value
            label5.Text = Convert.ToString(Convert.ToInt64(label5.Text) + 1);
        }
        
        private void openFileDialog1_FileOk(object sender, CancelEventArgs e)
        {
            this.fileTextbox.Text = this.openFileDialog1.FileName;
            //// Start by setting up a new thread using the delegate ThreadStart
            //// We tell it the entry function (the function to call first in the thread)
            //// Think of it as main() for the new thread.
            //ThreadStart theprogress = new ThreadStart(readFile);

            //// Now the thread which we create using the delegate
            //Thread startprogress = new Thread(theprogress);

            //// We can give it a name (optional)
            //startprogress.Name = "Update ProgressBar";

            //// Start the execution
            //startprogress.Start();
            //Reader r = new Reader(this.fileTextbox.Text);
            //r.ReadFile();
        }

        private void readFile()
        {
            try
            {
                String file = this.fileTextbox.Text;
                // Lets get the length so that when we are reading we know
                // when we have hit a "milestone" and to update the progress bar.
                FileInfo fileSize = new FileInfo(file);
                long size = fileSize.Length;
                

                // Next we need to know where we are at and what defines a milestone in the
                // progress. So take the size of the file and divide it into 100 milestones
                // (which will match our 100 marks on the progress bar.

                long currentSize = 0;
               // long incrementSize = (size / 100);

                // Open the big text file with open filemode access.
                StreamReader stream = new StreamReader(new FileStream(file, FileMode.Open));
                String line = stream.ReadLine();
                
                int a = line.Length;
                //priblizny pocet riadkov:
                long linescount = size / line.Length;
                long incrementSize = linescount / 100;
                // This buffer is only 10 characters long so we process the file in 10 char chunks.
                // We could have boosted this up, but we want a slow process to show the slow progress.
                char[] buff = new char[10];

                stream.ReadLine();
                string testing_line = stream.ReadLine();
                List<string> aa = new List<string>();
                string[] ar = new string[1];
                
                //f.
                ar = testing_line.Split('\t');
                //aa. = ar.ToList<string>;
                
                // Read through the file until end of file
                while (!stream.EndOfStream)
                {
                    // Add to the current position in the file
                    //currentSize += stream.Read(buff, 0, buff.Length);
                    stream.ReadLine();
                    currentSize++;
                    
                    // Once we hit a milestone, subtract the milestone value and
                    // call our delegate we defined above.
                    // We must do this through invoke since progressbar was defined in the other
                    // thread.
                    if (currentSize >= incrementSize)
                    {
                        
                        //currentSize -= incrementSize;
                        currentSize = 0;
                        progressBar1.Invoke(new updatebar(this.UpdateProgress));
                    }
                }

                // Close the stream and show we are done.
                // At the end of this ends the run of our thread.
                stream.Close();
                MessageBox.Show("Done");
            }
            catch (System.Exception ex)
            {
                System.Windows.Forms.MessageBox.Show(ex.Message);

            }



        }

        private void dataGridView1_SelectionChanged(object sender, EventArgs e)
        {
           
        }

        private void dataGridView1_MultiSelectChanged(object sender, EventArgs e)
        {
            MessageBox.Show("select!");
        }

        private void dataGridView1_ColumnStateChanged(object sender, DataGridViewColumnStateChangedEventArgs e)
        {
            
        }

        private void dataGridView1_MouseDown(object sender, MouseEventArgs e)
        {
            this.clicked = true;
        }

        private void dataGridView1_MouseUp(object sender, MouseEventArgs e)
        {
            if (this.clicked == true)
            {
                this.clicked = false;
                foreach (DataGridViewTextBoxCell c in this.dataGridView1.SelectedCells)
                {
                    if (c.Tag != null)
                    {
                        MessageBox.Show((c.Tag as Neuron).ID.ToString());
                    }
                }

            }
        }

        private void button3_Click(object sender, EventArgs e)
        {
            try
            {
            SOM.implementation.Map m = new Map();
            SOM.implementation.Reader  r = new Reader(this.fileTextbox.Text);
            r.ReadFile();
            m.Initialize(int.Parse(this.WidthG.Text), int.Parse(this.HeightG.Text),r.Size);
            this.numericUpDown2.Value = m.DistanceMax;
            this.textBox7.Text = r.Table.Count.ToString();
            }
            catch (System.Exception ex)
            {
                MessageBox.Show(ex.Message);

            }

        }





    }
}
