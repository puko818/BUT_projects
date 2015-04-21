using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Collections;

using SOM.interfaces;

namespace SOM.implementation
{
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
       

        public static int GetStaticID
        {
            get
            {
                return id;

            }

        }

        public static void ClearStaticID()
        {
            Neuron.id = 0;

        }
       

        //properties
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


        public Neuron(int posx, int posy)
        {
            this._x = posx;
            this._y = posy;
            this._id = ++(Neuron.id);
            this._genes = new ArrayList();
            


        }
        
        public void Init(int inputsize)
        {
           // this._id = ++(Neuron._id);
            this._inputs = inputsize;
            this._r = new Random();
            this.initWeights();
        }
        
      /*  
        public Neuron(int size)
        { 
            this._inputs = size;
            this._r = new Random();
            this.initWeights();
        }
        */

        private void initWeights()
        {
            if (this.weights == null)
                this.weights = new double[this._inputs];

            for (int i = 0; i < this._inputs; i++)
            {
                this.weights[i] = this._r.NextDouble();
            }

        }
        public double distance(double []d) 
        {
            double sum = 0.0;
            for (int i = 0; i < d.Length; i++)
            {
                sum += Math.Pow(d[i] - this.weights[i], 2);
            }
            return sum;
        }
        public void UpdateWeights() { }
    }
}
