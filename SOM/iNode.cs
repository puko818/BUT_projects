using System;



namespace SOM.interfaces
{
    public interface iNode
    {
        private string _id;
        private int _x;
        private int _y;
        public void Method1();
        public void Method2();
    }

    public interface iMap
    {
        private struct size
        {
            int x;
            int y;

        }

        private iNode[,] _interconnections;
        private double[,] _interconnections;
    }
}


