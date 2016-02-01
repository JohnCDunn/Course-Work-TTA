using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ConsoleApplication1
{
    class Program
    {
        static void Main(string[] args)
        {

            // Casting : If no magnitude is lost casting happens automatically, but otherwise it must be done
            // like this

            double pi = 3.14;
            Console.WriteLine("double Pi = " + pi);
            int intPi = (int)pi;
            Console.WriteLine("int intPi = " + intPi);

            Console.WriteLine("Press Enter to terminate...");
            Console.Read();

        }
    }
}
            