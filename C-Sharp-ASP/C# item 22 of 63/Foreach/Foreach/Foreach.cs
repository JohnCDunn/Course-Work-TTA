using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Foreach
{
    class Foreach
    {
        static void Main(string[] args)
        {
            // foreach cycles through every item in an array or collection
            string randStr = "Here are some random characters";

            foreach (char c in randStr)
            {
                Console.WriteLine(c);
            }
            Console.WriteLine("Press Enter to terminate...");
            Console.Read();
        }
    }
}
