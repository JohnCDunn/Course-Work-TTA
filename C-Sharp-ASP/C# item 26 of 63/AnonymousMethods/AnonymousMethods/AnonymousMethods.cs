using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

delegate double GetSum(double num1, double num2);

namespace AnonymousMethods
{
    class AnonymousMethods
    {
        static void Main(string[] args)
        {
            // ---------- ANONYMOUS METHODS ----------
            // An anonymous method has no name and its return type is defined by the return used in the method

            GetSum sum = delegate (double num1, double num2) 
            {
                return num1 + num2;
            };

            Console.WriteLine("5 + 10 = " + sum(5, 10));

            Console.WriteLine("Press Enter to terminate...");
            Console.Read();
        }
    }
}
