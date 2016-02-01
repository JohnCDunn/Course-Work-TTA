using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Ternary
{
    class Ternary
    {
        static void Main(string[] args)
        {
            // Ternary Operator
            int age = 17;
            Console.WriteLine("Age = 17");
            Console.WriteLine("set canDrive to true if >= 16 or false if < 16");

            bool canDrive = age >= 16 ? true : false;

            Console.WriteLine("Can Drive?: " + canDrive);

            Console.WriteLine("Press Enter to terminate...");
            Console.Read();
        }
    }
}
            