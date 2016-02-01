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
            var people = new List<Person>
            {
                new Person{FirstName = "John", LastName = "Doe", Age = 25},
                new Person{FirstName = "Jane", LastName = "Doe", Age = 26},
                new Person{FirstName = "John", LastName = "Williams", Age = 40},
                new Person{FirstName = "Samantha", LastName = "Williams", Age = 34},
                new Person{FirstName = "Bob", LastName = "Walters", Age = 12},
            };

            var result = from p in people
                         orderby p.LastName
                         select p;


            foreach (var item in result)
            {
                Console.WriteLine("{0} - {1}", item.FirstName, item.LastName);
            }

            Console.WriteLine("Press Enter to terminate...");
            Console.Read();

        }

        public class Person
        {
            public string FirstName { get; set; }

            public string LastName { get; set; }

            public int Age { get; set; }
        }
    }
}
