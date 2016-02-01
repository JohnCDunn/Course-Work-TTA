using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace While
{
    class While
    {
        static void Main(string[] args)
        {
            // ---------- WHILE LOOPING ----------

            int i = 0;

            while (i < 10)
            {
                // If i = 7 then skip the rest of the code and start with i = 8
                if (i == 7)
                {
                    i++;
                    continue;
                }

                // Jump completely out of the loop if i = 9
                if (i == 9)
                {
                    break;
                }

                // You can't convert an int into a bool : Print out only odds
                if ((i % 2) > 0)
                {
                    Console.WriteLine(i);
                }
                i++;
                
            }
            Console.WriteLine("Press Enter to terminate...");
            Console.Read();
        }           
    }
}
