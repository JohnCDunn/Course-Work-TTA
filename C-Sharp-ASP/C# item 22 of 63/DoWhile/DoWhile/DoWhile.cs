using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace DoWhile
{
    class DoWhile
    {
        static void Main(string[] args)
        {
            // The do while loop will go through the loop at least once
            string guess;
            do
            {
                Console.WriteLine("Guess a Number ");
                guess = Console.ReadLine();
            } while (!guess.Equals("15")); // How to check String equality
            Console.WriteLine("Press Enter to terminate...");
            Console.Read();
        }
    }
}
