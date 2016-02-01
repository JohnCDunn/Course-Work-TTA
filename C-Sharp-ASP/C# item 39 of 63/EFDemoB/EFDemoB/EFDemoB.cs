using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EFDemoB
{
    class EFDemoB
    {
        static void Main(string[] args)
        {
            using (NORTHWINDEnt ctx = new NORTHWINDEnt())
            {
                IOrderedQueryable<Category> categories = from c in ctx.Categories
                                                         orderby c.CategoryName
                                                         select c;
                foreach (Category category in categories)
                {
                    Console.WriteLine(category.CategoryName);
                }

            }
            Console.WriteLine("Press Enter to terminate...");
            Console.Read();
        }
    }
}
