using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;





namespace SOM.interfaces
{
    public interface iNode
    {
        double distance(double []d);
        void Init(int inputsize);
        void UpdateWeights();
    }

}
