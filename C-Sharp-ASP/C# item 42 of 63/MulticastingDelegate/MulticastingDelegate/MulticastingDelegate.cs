using System;

delegate int NumberChanger(int n);

namespace MulticastingDelegate
{
    class MulticastingDelegate
    {
        static int num = 10;

        public static int AddNum(int p)
        {
            Console.WriteLine("Adding " + p + " + " + num + " in nc1");
            num += p; 
            Console.WriteLine("num is now = " + num);
            return num;
        }

        public static int MultNum(int q)
        {
            Console.WriteLine("Multipling " + q + " & " + num + " in nc2");
            num *= q;
            Console.WriteLine("num is now = " + num);
            return num;
        }

        public static int getNum()
        {
            return num;
        }

        static void Main(string[] args)
        {
            //create delegate instances
            Console.WriteLine("Initialized num to 10");
            Console.WriteLine("Created nc, nc1 and nc2 delegates");
            NumberChanger nc;
            NumberChanger nc1 = new NumberChanger(AddNum);
            NumberChanger nc2 = new NumberChanger(MultNum);
            nc = nc1;
            nc += nc2;

            //calling multicast
            nc(5);
            Console.WriteLine("");
            Console.WriteLine("Value of Num: {0}", getNum());
            Console.ReadKey();
        }
    }
}
