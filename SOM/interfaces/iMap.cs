using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace SOM.interfaces
{

        public interface iMap
        {
            void Initialize(int x, int y, int size);
            void Train(int distance, double learning_rate, double []vector);

        }
    }


