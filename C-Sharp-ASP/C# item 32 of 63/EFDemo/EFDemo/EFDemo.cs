using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EFDemo
{
    class EFDemo
    {
        static void Main(string[] args)
        {
            using (NORTHWINDEntities ctx = new NORTHWINDEntities())
            {
                var categories = from c in ctx.Categories
                                 orderby c.CategoryName
                                 select c;
                foreach (var itme in categories) {
                    Console.WriteLine("itme = " + itme);
                }
            }


            Console.WriteLine("Press Enter to terminate...");
            Console.Read();

        }
    }

}
