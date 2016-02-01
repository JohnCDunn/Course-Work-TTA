using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Enumerable
{
    class Enumerable
    {
        static void Main(string[] args)
        {
            Customer[] customers = new Customer[3];

            customers[0] = new Customer
            {
                Name = "Mark",
                Gender = Gender.Male
            };
            customers[1] = new Customer
            {
                Name = "Mary",
                Gender = Gender.Female
            };
            customers[2] = new Customer
            {
                Name = "Sam",
                Gender = Gender.Unknown
            };

            foreach (Customer customer in customers)
            {
                Console.WriteLine("Name = {0} && Gender = {1}", customer.Name, GetGender(customer.Gender));

            }

            Console.WriteLine("Press Enter to terminate...");
            Console.Read();
        }

        public static string GetGender(Gender gender)
        {
            switch (gender)
            {
                case Gender.Unknown:
                    return "unknown";
                case Gender.Male:
                    return "male";
                case Gender.Female:
                    return "female";
                default:
                    return "Invalid data detected";

            }
        }
    }
}

public enum Gender
{
    Unknown,
    Male,
    Female
}

 
public class Customer
{
    public string Name { get; set; }
    public Gender Gender { get; set; }
}  

