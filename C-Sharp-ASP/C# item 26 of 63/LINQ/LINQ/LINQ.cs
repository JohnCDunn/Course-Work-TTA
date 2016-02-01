using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace LINQ
{
    class LINQ
    {
        static void Main(string[] args)
        {
            var sample = "I enjoy writing uber-software in C#";

            var result = from c in sample
                         select c;

            foreach (var item in result)
            {
                Console.WriteLine(item);
            }
            Console.WriteLine("Press Enter to terminate...");
            Console.Read();

        }
    }
}
