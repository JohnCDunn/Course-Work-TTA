using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Linq3
{
    class Linq3
    {
        static void Main(string[] args)
        {
            var sample = "I enjoy writing uber-software in C#";

            var result = from c in sample.ToLower()
                         where c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
                         orderby c
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
