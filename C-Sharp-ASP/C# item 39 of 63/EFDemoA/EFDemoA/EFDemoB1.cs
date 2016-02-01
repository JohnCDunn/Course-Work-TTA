using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;


namespace EFDemoB1
{
    class EFDemoB1
    {
        static void Main(string[] args)
        {
            using (NORTHWINDEntities ctx = new NORTHWINDEntities())
            {
                IOrderedQueryable<Category> categories = from c in ctx.Categories
                                 orderby c.CategoryName
                                 select c;

                foreach (Category category in categories)
                {
                    Console.WriteLine(categories.ToString());
                }               
            }
            Console.WriteLine("Press Enter to terminate...");
            Console.Read();

        }
    }

}
