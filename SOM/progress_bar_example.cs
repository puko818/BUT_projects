//ADAPTED from http://www.coderslexicon.com/threads-progressbar-and-file-processing-in-c/
using System;
using System.Collections.Generic;
using System.ComponentModel;
using System.Data;
using System.Drawing;
using System.Text;
using System.Windows.Forms;

// Namespaces to read files (IO) and to handle threads (Threading)
using System.IO;
using System.Threading;

namespace threadingexample
{
    public partial class Form1 : Form
    {
        public Form1()
        {
            InitializeComponent();
        }

        private void btnStart_Click(object sender, EventArgs e)
        {
            // Start by setting up a new thread using the delegate ThreadStart
            // We tell it the entry function (the function to call first in the thread)
            // Think of it as main() for the new thread.
            ThreadStart theprogress = new ThreadStart(ReadFile);

            // Now the thread which we create using the delegate
            Thread startprogress = new Thread(theprogress);

            // We can give it a name (optional)
            startprogress.Name = "Update ProgressBar";

            // Start the execution
            startprogress.Start();

        }

        // This delegate tells which function to call. It matches the signature
        // of our UpdateProgress function. During the invoke in ReadFile, we give it
        // the function to call which matches. In this case UpdateProgress.

        public delegate void updatebar();
        // This will run in the main thread so it can update the controls for us.
        private void UpdateProgress()
        {
            progressBar1.Value += 1;

            // Here we are just updating a label to show the progressbar value
            label1.Text = Convert.ToString(Convert.ToInt64(label1.Text) + 1);
        }

        // This would be our version of main() for the new thread.
        // We start reading a huge file with 17000+ lines in it.
        private void ReadFile()
        {
            String bigFile = @"c:\\bigfile.txt";

            // Lets get the length so that when we are reading we know
            // when we have hit a "milestone" and to update the progress bar.
            FileInfo fileSize = new FileInfo(bigFile);
            long size = fileSize.Length;

            // Next we need to know where we are at and what defines a milestone in the
            // progress. So take the size of the file and divide it into 100 milestones
            // (which will match our 100 marks on the progress bar.

            long currentSize = 0;
            long incrementSize = (size / 100);

            // Open the big text file with open filemode access.
            StreamReader stream = new StreamReader(new FileStream(bigFile, FileMode.Open));

            // This buffer is only 10 characters long so we process the file in 10 char chunks.
            // We could have boosted this up, but we want a slow process to show the slow progress.
            char[] buff = new char[10];

            // Read through the file until end of file
            while (!stream.EndOfStream)
            {
                // Add to the current position in the file
                currentSize += stream.Read(buff, 0, buff.Length);

                // Once we hit a milestone, subtract the milestone value and
                // call our delegate we defined above.
                // We must do this through invoke since progressbar was defined in the other
                // thread.
                if (currentSize >= incrementSize)
                {
                    currentSize -= incrementSize;
                    progressBar1.Invoke(new updatebar(this.UpdateProgress));
                }
            }

            // Close the stream and show we are done.
            // At the end of this ends the run of our thread.
            stream.Close();
            MessageBox.Show("Done");
        }
    }
}
