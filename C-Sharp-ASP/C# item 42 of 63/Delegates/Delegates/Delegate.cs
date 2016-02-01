using System;

delegate int NumberChanger(int n);

namespace Delegates
{
    class Delegate
    {
        static int num = 10;
        public static int AddNum(int p)
        {
            num += p;
            return num;
        }

        public static int MultNum(int q)
        {
            num *= q;
            return num;
        }
        public static int getNum()
        {
            return num;
        }

        static void Main(string[] args)
        {
            //create delegate instances
            Console.WriteLine("Create a delegate for AddNum method");
            NumberChanger nc1 = new NumberChanger(AddNum);
            Console.WriteLine("Create a delegate for MultNum method");
            NumberChanger nc2 = new NumberChanger(MultNum);

            //calling the methods using the delegate objects
            Console.WriteLine("Call the delegate for adding numbers " + num + " + 25");
            nc1(25);
            Console.WriteLine("Value of Num: {0}", getNum());
            Console.WriteLine("Call the delegate for Multipling numbers " + num  + " * 5");
            nc2(5);
            Console.WriteLine("Value of Num: {0}", getNum());
            Console.ReadKey();
        }
    }
}
