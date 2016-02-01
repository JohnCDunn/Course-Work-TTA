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
            Console.Write("What is your name? ");
            string name = Console.ReadLine();
            Console.WriteLine("Hi " + name);

            // code from my toolbox
            Console.WriteLine("Press Enter to terminate...");
            Console.Read();


        }
    }
}
            