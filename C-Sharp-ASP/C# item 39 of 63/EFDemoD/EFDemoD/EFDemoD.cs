using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EFDemoD
{
    class EFDemoD
    {
        static void Main(string[] args)
        {
            using (NORTHWINDEntitiesD ctx = new NORTHWINDEntitiesD())
            {
                IOrderedQueryable<Category> categories = from c in ctx.Categories
                                                         orderby c.CategoryName
                                                         select c;
                foreach (Category category in categories)
                {
                    Console.WriteLine(category.CategoryName);

                    foreach (var product in category.Products)
                    {
                        product.UnitPrice++;
                        Console.WriteLine("\t{0} {1:c}", product.ProductName, product.UnitPrice);
                    }

                }
                ctx.SaveChanges();

            }
            Console.WriteLine("Press Enter to terminate...");
            Console.Read();
        }
    }
}
