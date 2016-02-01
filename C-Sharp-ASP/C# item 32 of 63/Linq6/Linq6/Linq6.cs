using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Linq6
{
    class Linq6
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
                         group p by p.LastName;


            foreach (var item in result)
            {
                Console.WriteLine(item.Key + " - " + item.Count());
                foreach (var p in item)
                {
                    Console.WriteLine("\t{0}, {1}", p.LastName, p.FirstName);
                }
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
