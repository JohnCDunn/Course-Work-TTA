using System;

namespace SealedClass
{
    class Program
    {
        static void Main(string[] args)
        {
            SealedClass sealedCls = new SealedClass();
            int total = sealedCls.Add(4, 5);
            Console.WriteLine("Total = " + total.ToString());
            Console.WriteLine("This wont Work: class DerivedFromSealed : SealedClass");
            Console.WriteLine("Error: Cannot derive from sealed type");
            Console.WriteLine("Press Enter to terminate...");
            Console.Read();
        }
    }
            
    sealed class SealedClass
    {
        public int Add(int x, int y)
        {
            return x + y;
        }
    }
    //class DerivedFromSealed : SealedClass
    //{
    //    public int Add(int x, int y)
    //    {
    //        return 2*x + 3*y;
    //    }
    //}

}
