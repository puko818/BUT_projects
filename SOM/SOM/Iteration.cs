using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;

namespace SOM.implementation
{
    /// <summary>
    /// Class implements a decision logic for the algorithm runtime
    /// </summary>
    public class Iteration
    {
        private int _actual_iteration = -1;
        private int _number_of_iterations = 0;
        private double _learning_rate;
        private List<Interval> _intervals;
        private Interval _actual_interval;
        /// <summary>
        /// interval structure only for purpose of the Iteration class
        /// </summary>
        private struct Interval
        {
            int min;
            int max;
            int distance;
            double learning_rate;

            /// <value>
            /// lower bound
            /// </value>
            public int Min
            {
                get
                {
                    return this.min;
                }
            }
            /// <value>
            /// upper bound
            /// </value>
            public int Max
            {
                get
                {
                    return this.max;
                }

            }
            /// <value>
            /// actual distance
            /// </value>
            public int Distance
            {
                get
                {
                    return this.distance;

                }

            }
            /// <value>
            /// actual learning rate
            /// </value>
            public double LearningRate
            {
                get
                {

                    return this.learning_rate;
                }

            }
            /// <summary>
            /// Constructor of the Interval structure
            /// </summary>
            /// <param name="min"></param>
            /// <param name="max"></param>
            /// <param name="distance"></param>
            /// <param name="learning_rate"></param>
            public Interval(int min, int max, int distance, double learning_rate)
            {
                this.min = min;
                this.max = max;
                this.distance = distance;
                this.learning_rate = learning_rate;

            }
        }



        public Iteration()
        {
            this._intervals = new List<Interval>();
        }

        /// <summary>
        /// public properties, referencing to the actual interval
        /// </summary>
        public int ActualDistance
        {
            get
            {
                return this._actual_interval.Distance;
            }

        }

        public double ActualLearningRate
        {
            get
            {
                return this._actual_interval.LearningRate;
            }

        }
        
        public int ActualIteration
        {
            get
            {
                return this._actual_iteration;
            }

            set
            {
                this._actual_iteration = value;

            }
        }

        public int IterationsNumber
        {
            get
            {
                return this._number_of_iterations;
            }

            set
            {
                this._number_of_iterations = value;

            }
        }



        /// <summary>
        /// moves to the next iteration
        /// </summary>
        /// <returns>true if limits were not exceeded, false otherwise</returns>
        public bool NextIteration()
        {
            if (this._actual_iteration++ >= this._number_of_iterations)
                return false;
            foreach (Interval i in this._intervals)
            {
                if (this._actual_iteration >= i.Min && this._actual_iteration <= i.Max)
                {
                    this._actual_interval = i;
                }
            }
            return true;
        }

        /// <summary>
        /// method for adding a new interval
        /// </summary>
        /// <param name="min"></param>
        /// <param name="max"></param>
        /// <param name="distance"></param>
        /// <param name="learning_rate"></param>
        /// <returns></returns>
        public int ParseAndSave(int min, int max, int distance, double learning_rate)
        {
            int ret = 0;
            
            if (distance >= 0 && min >= 0 && /*max < this._number_of_iterations &&*/ learning_rate > 0.0 && min < max)
            {
                if (this._intervals.Count > 0)
                {
                    foreach (Interval i in this._intervals)
                    {
                        if ((min > i.Min && min < i.Max) || (max > i.Min && max < i.Max))
                            ret = -1;
                    }
                }
                this._intervals.Add(new Interval(min, max, distance, learning_rate));
                if (ret == 0 && max > this._number_of_iterations) this._number_of_iterations = max;
            }
            else ret = -1 ;

            return ret;
        }

        /// <summary>
        /// resets the whole iteration variable
        /// </summary>
        public void Reset()
        {
            this._actual_iteration = -1;
            this._number_of_iterations = 0;
            this._intervals.Clear();
            this._learning_rate = 0.0;

        }

        
    }
}
