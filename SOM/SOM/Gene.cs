using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace SOM.implementation
{
    /// <summary>
    /// class for saving loaded data
    /// </summary>
    class Gene
    {
        private double[] _values = null;
        private string _name = null;

        public string Name
        {
            get
            {
                return this._name;
            }

        }

        public double[] Values
        {
            get
            {
                return this._values;
            }

        }

        
        
        public Gene(double []vector, string name)
        {
            this._name = name;
            this._values = vector;
        }
    }
}
