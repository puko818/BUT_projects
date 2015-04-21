using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Collections;

using SOM.interfaces;

namespace SOM.implementation
{
    /// <summary>
    /// Class implements the neuron node
    /// </summary>
    class Neuron: iNode
    {
        //private members
        private int _x;
        private int _y;
        private string _label = null;
        private int _id;
        private double[] weights = null;
        private int _inputs;
        private ArrayList _genes = null;
        private Random _r;
        private static int id = 0;


        /// <value>
        /// list of genes that were actually classified to this neuron
        /// </value>
        public ArrayList Genes
        {
            get
            {
                return this._genes;
            }

        }
        /// <value>
        /// static property for identifing the order in the neuron sequence
        /// </value>
 
        public static int GetStaticID
        {
            get
            {
                return id;

            }

        }

        

        //properties
        public double[] Weights
        {
            get
            {

                return this.weights;
            }


        }
        
      
        public int ID
        {
            get
            {
                return this._id;
            }
        }
        
        public int X
        {
            get
            {
                return this._x;
            }


            set
            {
                this._x = value;
            }


        }

        public int Y
        {
            get
            {
                return this._y;
            }
            set
            {
                this._y = value;
            }
        }

        public string Label
        {
            get
            {
                if (this._label == null)
                    return "undefined label";
                else return this._label;

            }

            set
            {
                this._label = value;
            }


        }

        /// <summary>
        /// Constructor
        /// </summary>
        /// <param name="posx">position x in the map</param>
        /// <param name="posy">position y in the map</param>
        public Neuron(int posx, int posy)
        {
            this._x = posx;
            this._y = posy;
            this._id = ++(Neuron.id);
            this._genes = new ArrayList();
            


        }

        public static void ClearStaticID()
        {
            Neuron.id = 0;

        }
       
        /// <summary>
        /// Initialization method for the neuron weights
        /// </summary>
        /// <param name="inputsize">size of input vector</param>
        public void Init(int inputsize)
        {
           // this._id = ++(Neuron._id);
            this._inputs = inputsize;
            this._r = new Random();
            this.initWeights();
        }

        private void initWeights()
        {
            if (this.weights == null)
                this.weights = new double[this._inputs];

            for (int i = 0; i < this._inputs; i++)
            {
                this.weights[i] = this._r.NextDouble();
            }

        }
        /// <summary>
        /// Distance metrics
        /// </summary>
        /// <param name="d">input vector</param>
        /// <returns>the euclidian distance of input vector and neuron weights</returns>
        public double distance(double []d) 
        {
            double sum = 0.0;
            for (int i = 0; i < d.Length; i++)
            {
                if (Double.IsNaN(d[i])) 
                    continue;
                else sum += Math.Pow(d[i] - this.weights[i], 2);
            }
            return Math.Sqrt(sum);
        }
       


    }
}
