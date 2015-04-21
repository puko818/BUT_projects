using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Collections;

using SOM.interfaces;

namespace SOM.implementation
{
    class Map: iMap
    {
        //private iNode[,] _interconnections;
       // private double[,] _interconnections;
        private iNode[,] _neurons;
        private int width = 10;
        private int height = 10;
        private int t = 100;
        private int delta_t = 10;
        private int distancemax;
        private double learning_rate = 0.1;
        private double delta_learning_rate;


        public double LearningRate 
        { 
            get
            {
                return this.learning_rate; 
            }
            set
            {
                this.learning_rate = value;           
            }

        }
        
        /*
         *size = number of dimensions of the input vector
         * 
         * 
         */
        public void Initialize(int x, int y, int size)
        {
            this.distancemax = Math.Max(x, y) - 1;
            this.width = x;
            this.height = y;
            _neurons = new iNode[x, y]; //2D array of x rows and y columns
            
            //2D map initialization with random input weights  <0;1>
            for (int i = 0; i < x; i++)
            {
                for (int j = 0; j < y; j++)
                {
                    _neurons[i, j] = new Neuron(i,j);
                    _neurons[i, j].Init(size);

                }
            }
        }


        public int DistanceMax
        {
            get
            {
                return this.distancemax;
            }
        }
        
        public iNode[,] Neurons
        {
            get 
            {
                return this._neurons;
            }


        }
        

        
        
        /*
         * 
         */
        public void Train(int distance, double learning_rate, double []vector)
        {
            ArrayList ar = new ArrayList();
            iNode winner = this.Compete(vector);
            ar.Add(winner);
            this.GetNeighbourhood(distance, winner as Neuron, ar);
            
            
            

        }

        
        //returns ID of the winning Neuron
        public iNode Compete(double[] vector)
        {
            double distancetmp = 0.0;
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

        private void UpdateWeights(int distance, double learning_rate,double []vector)
        {
            


        }

        public  ArrayList GetNeighbourhood(int distance, Neuron n, ArrayList a)
        {
            if (distance >= 1)
            {
                int tmp_x = n.X;
                int tmp_y = n.Y;
                //horizontal neighbors
                if (tmp_y > 0)
                {
                    if (!a.Contains(this._neurons[tmp_x,tmp_y-1])) a.Add(this._neurons[tmp_x,tmp_y-1]);
                    this.GetNeighbourhood(distance-1,this._neurons[tmp_x,tmp_y-1] as Neuron,a);
                }   
                if (tmp_y < this.width)
                {
                    if (!a.Contains(this._neurons[tmp_x, tmp_y + 1])) a.Add(this._neurons[tmp_x, tmp_y + 1]);
                    this.GetNeighbourhood(distance-1,this._neurons[tmp_x,tmp_y+1] as Neuron,a);
                }

                //vertical neighbors
                if (tmp_x > 0)
                {
                    if (!a.Contains(this._neurons[tmp_x - 1, tmp_y])) a.Add(this._neurons[tmp_x - 1, tmp_y]);
                    this.GetNeighbourhood(distance-1,this._neurons[tmp_x-1,tmp_y] as Neuron,a);
                }
                if (tmp_x < this.height)
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
    }
}
