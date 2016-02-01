using System;
using System.Collections.Generic;
using System.Data.Entity.Infrastructure;

using System.Linq;
using System.Text;
using System.Threading.Tasks;
using System.Data.Entity;

namespace ExecutingSQL
{
    class ExecutingSQL
    {
        static void Main(string[] args)
        {
            using (NORTHWINDEntities ctx = new NORTHWINDEntities())
            {
                Console.Write("Enter catagory id:");
                string id = Console.ReadLine();
                string sqlSelect = "Select * from Products Where CategoryID = " + id;
                DbSqlQuery<Product> query = ctx.Products.SqlQuery(sqlSelect);
                foreach (Product product in query)
                {
                    Console.WriteLine("{0} {1} {2:c}", product.ProductID, product.ProductName, product.UnitPrice);
                }

            }
            Console.ReadLine();
        }
    }
}

