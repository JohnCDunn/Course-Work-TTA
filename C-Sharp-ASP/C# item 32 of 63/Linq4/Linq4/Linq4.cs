using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Linq4
{
    class Linq4
    {
        static void Main(string[] args)
        {
            var sample = "I enjoy writing uber-software in C#";

            var result = from c in sample.ToLower()
                         where c == 'a' || c == 'e' || c == 'i' || c == 'o' || c == 'u'
                         orderby c
                         group c by c;
                         

            foreach (var item in result)
            {
                Console.WriteLine("{0} - {1}", item.Key, item.Count());
            }
            Console.WriteLine("Press Enter to terminate...");
            Console.Read();

        }
    }
}