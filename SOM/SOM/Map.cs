using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Collections;

using SOM.interfaces;

namespace SOM.implementation
{
    /// <summary>
    /// Class implements the SOM algorithm including supporting structures management 
    /// </summary>


    class Map: iMap
    {

        private iNode[,] _neurons;
        private int width = 10;
        private int height = 10;
        private int distance;
        private int distancemax;
        private Hashtable _asociationtable = null;
        private Iteration it = null;
        private Array _a;



        /// <value>
        /// Array of genes to analyze
        /// </value>
        public Array GenesData
        {
            get
            {
                return this._a;
            }
        }
        
        /// <value>
        /// Global number of iterations for the SOM algorithm
        /// </value>
        public int IterationsNumber
        {
            get
            {
                return this.it.IterationsNumber;
            }

            set
            {
                this.it.IterationsNumber = value;

            }


        }    
        
        /// <value>
        /// Holds the actual iteration
        /// </value>

        public int ActualIteration
        {
            get
            {

                return this.it.ActualIteration;

            }
        }
        
        /// <value>
        /// Classified hash pairs gene->neuron table
        /// </value>
        public Hashtable AsociationTable
        {
            get
            {
                return this._asociationtable;
            }


        }

        /// <value>
        /// The actually used distance for specifing the neighbourhood
        /// </value>
        public int ActualDistance
        {
            get
            {
                return this.distance;
            }

            set
            {
                this.distance = value;
            }

        }
        
        
        /// <value>
        /// Actual width of the SOM
        /// </value>

        public int Width
        {
            get
            {
                return this.width;
            }
        }

        /// <value>
        /// Actual height of the SOM
        /// </value>
        public int Height
        {
            get
            {
                return this.height;

            }

        }

        /// <value>
        /// maximal distance regarding to the size of the map
        /// </value>
        public int DistanceMax
        {
            get
            {
                return this.distancemax;
            }
        }

        /// <value>
        /// Initialized array of neurons
        /// </value>

        public iNode[,] Neurons
        {
            get
            {
                return this._neurons;
            }


        }   


        
        /// <summary>
        /// The initialization method for loading the basic management and/or saving structures
        /// </summary>
        /// <param name="x">map width</param>
        /// <param name="y">map height</param>
        /// <param name="size">size of the input vector</param>
        /// <param name="dic">dictionary for the hashtable</param>
        /// <param name="it">istance of the iteration class with intervals-values</param>
        public void Initialize(int x, int y, int size, Hashtable dic, Iteration it)
        {
            this.it = it;
            this.distancemax = Math.Max(x, y) - 1;
            this.width = x;
            this.height = y;
            _neurons = new iNode[x, y]; //pole o x riadkoch a y stlpcoch
            this._asociationtable = dic;
            this._a = new Gene[this._asociationtable.Keys.Count];
            this._asociationtable.Keys.CopyTo(this._a, 0);
            //initialization of 2D neurons-map with random weights <0;1>
            for (int i = 0; i < x; i++)
            {
                for (int j = 0; j < y; j++)
                {
                    _neurons[i, j] = new Neuron(i,j);
                    _neurons[i, j].Init(size);

                }
            }
        }



        
        /// <summary>
        /// Method for training the network/updating the weights
        /// </summary>
        /// <param name="g">actually analyzed gene</param>
        public void Train(Gene g)
        {
            ArrayList ar = new ArrayList();
            iNode winner = this.Compete(g.Values);
            if (!this._asociationtable.Contains(g))
                throw new System.Exception("Hashtable doesn't contain all genes from input file!");
            Neuron n =  (Neuron) this.AsociationTable[g];

            if (n != winner as Neuron)
            {
                if (n != null)
                {//gen bol klasifikovany k inemu neuronu ako predtym
                    n.Genes.Remove(g);
                    this.AsociationTable[g] = winner;
                }
                else this.AsociationTable[g] = winner;
            }
            ar.Add(winner);
            this.GetNeighbourhood(this.it.ActualDistance, winner as Neuron, ar);
            (winner as Neuron).Genes.Add(g);
            foreach (Neuron ne in ar)
            {
                this.UpdateWeights(g.Values, ne);
            }
            
            

        }


        /// <summary>
        /// Neuron competition
        /// </summary>
        /// <param name="vector">input vector</param>
        /// <returns>reference to the winner neuron</returns>
        public iNode Compete(double[] vector)
        {
            double distancetmp = Double.PositiveInfinity;
            int idtmp = -1;
            double tmp = 0.0;
            int tmp_x = 0, tmp_y = 0;
            iNode tmp_node = null;
            foreach (Neuron n in this._neurons)
            {
                tmp  = n.distance(vector);
                if (tmp < distancetmp)
                {
                    distancetmp = tmp;
                    tmp_node = n;
                    /*idtmp = n.ID;
                    tmp_x = n.X;
                    tmp_y = n.Y;*/
                }
            }
            return tmp_node;
        }

        private void UpdateWeights(double []vector, Neuron n)
        {
            int length = 0;
            length = (n.Weights.Length == vector.Length ? vector.Length : Math.Min(n.Weights.Length,vector.Length));
            for (int i = 0; i < length; i++)
            {
                if (Double.IsNaN(vector[i])) continue;
                n.Weights[i] = n.Weights[i] + this.it.ActualLearningRate * (vector[i] - n.Weights[i]);
            }
        }

        /// <summary>
        /// Recursive method for finding the neighbourhood of a specific neuron
        /// </summary>
        /// <param name="distance">actually used distance</param>
        /// <param name="n">neuron that the neighbourhood should be find for</param>
        /// <param name="a">collection for saving the result</param>
        /// <returns></returns>
        public ArrayList GetNeighbourhood(int distance, Neuron n, ArrayList a)
        {
            if (distance >= 1)
            {
                int tmp_x = n.X;
                int tmp_y = n.Y;
                //horizontal neighbours
                if (tmp_y > 0)
                {
                    if (!a.Contains(this._neurons[tmp_x,tmp_y-1])) a.Add(this._neurons[tmp_x,tmp_y-1]);
                    this.GetNeighbourhood(distance-1,this._neurons[tmp_x,tmp_y-1] as Neuron,a);
                }   
                if (tmp_y < this.width-1)
                {
                    if (!a.Contains(this._neurons[tmp_x, tmp_y + 1])) a.Add(this._neurons[tmp_x, tmp_y + 1]);
                    this.GetNeighbourhood(distance-1,this._neurons[tmp_x,tmp_y+1] as Neuron,a);
                }

                //vertical neighbours
                if (tmp_x > 0)
                {
                    if (!a.Contains(this._neurons[tmp_x - 1, tmp_y])) a.Add(this._neurons[tmp_x - 1, tmp_y]);
                    this.GetNeighbourhood(distance-1,this._neurons[tmp_x-1,tmp_y] as Neuron,a);
                }
                if (tmp_x < this.height-1)
                {
                    if (!a.Contains(this._neurons[tmp_x + 1, tmp_y])) a.Add(this._neurons[tmp_x + 1, tmp_y]);
                    this.GetNeighbourhood(distance - 1, this._neurons[tmp_x + 1, tmp_y] as Neuron, a);
                }

            }
            return a;
        }

        public void Clear()
        {
            Neuron.ClearStaticID();
        }

        /// <summary>
        /// algorithm for iterating and learning over the whole network
        /// </summary>
        public void Algorithmtest()
        {
           
            IEnumerator enumerator = this._a.GetEnumerator();
            enumerator.Reset();
            System.Windows.Forms.Cursor.Current = System.Windows.Forms.Cursors.WaitCursor;
            while (it.NextIteration())
            {
                if (enumerator.MoveNext())
                {

                }
                else
                {
                    enumerator.Reset();
                    enumerator.MoveNext();
                }
                Gene g = (Gene)enumerator.Current;
                //this._
                this.Train(g);
            }
            System.Windows.Forms.Cursor.Current = System.Windows.Forms.Cursors.Default;
            System.Windows.Forms.MessageBox.Show("Successfully done", "Analysis...");
        }

        public void Reset()
        {
            this.it.Reset();
        }
    }
}

