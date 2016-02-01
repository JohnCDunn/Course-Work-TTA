using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ForLoop
{
    class ForLoop
    {
        static void Main(string[] args)
        {
            // Puts all changes to the iterator in one place
            for (int j = 0; j < 10; j++)
            {
                if ((j % 2) > 0)
                {
                    Console.WriteLine(j);
                }
            }

            Console.WriteLine("Press Enter to terminate...");
            Console.Read();

        }
    }
}
