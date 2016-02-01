using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace EntityState
{
    class Program
    {
        static void Main(string[] args)
            
        {
            using (NORTHWINDEntities ctx = new NORTHWINDEntities())
            {
                Console.WriteLine("\nGet product...");
                Console.ReadLine();
                Product chai = ctx.Products.Find(1);
                Display(ctx, chai);

                Console.WriteLine("\nUpdate price...");
                Console.ReadLine();
                ++chai.UnitPrice;
                Display(ctx, chai);

                Console.WriteLine("\nCreate new product...");
                Console.ReadLine();
                Product kahula = new Product() { ProductName = "Kahula Coffee", UnitPrice = 10 };
                Display(ctx, kahula);

                Console.WriteLine("\nAdd new product tocontext...");
                Console.ReadLine();
                ctx.Products.Add(kahula);
                Display(ctx, kahula);
                
                Console.WriteLine("\nSave changes....");
                Console.ReadLine();
                ctx.SaveChanges();
                Display(ctx, chai);
                Display(ctx, kahula);

                Console.WriteLine("\nDelete kahula...");
                Console.ReadLine();
                ctx.Products.Remove(kahula);
                Display(ctx, kahula);

                Console.WriteLine("\nSave changes....");
                Console.ReadLine();
                ctx.SaveChanges();
                Display(ctx, kahula);

                Console.WriteLine("Finished");
                Console.ReadLine();
            }
        }

        private static void Display(NORTHWINDEntities ctx, 
            
            
            
            
            
            
            Product entity)
        {
            Console.WriteLine("Product {0} {1} {2:C} {3}",
               entity.ProductID,
               entity.ProductName,
               entity.UnitPrice,
               ctx.Entry<Product>(entity).State.ToString());
            
        }
    }
}
