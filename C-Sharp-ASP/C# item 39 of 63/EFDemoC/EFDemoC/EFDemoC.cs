using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EFDemoC
{
    class EFDemoC
    {
        static void Main(string[] args)
        {
            using (NORTHWINDEntities2 ctx = new NORTHWINDEntities2())
            {
                IOrderedQueryable<Category> categories = from c in ctx.Categories
                                                         orderby c.CategoryName
                                                         select c;
                foreach (Category category in categories)
                {
                    Console.WriteLine(category.CategoryName);

                    foreach (var product in category.Products)
                    {
                        Console.WriteLine("\t{0} {1:c}", product.ProductName, product.UnitPrice);
                    }

                }

            }
            Console.WriteLine("Press Enter to terminate...");
            Console.Read();
        }
    }
}
