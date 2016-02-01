using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

// ---------- STRUCT ----------
// A struct is a custom type that holds data made up from different data types
struct Customers
{
    private string name;
    private double balance;
    private int id;

    public void createCust(string n, double b, int i)
    {
        name = n;
        balance = b;
        id = i;
    }

    public void showCust()
    {
        Console.WriteLine("Name : " + name);
        Console.WriteLine("Balance : " + balance);
        Console.WriteLine("ID : " + id);
    }
}

namespace Structs
{
    class Structs
    {
        static void Main(string[] args)
        {
            // ---------- STRUCTS ----------
            Customers bob = new Customers();

            bob.createCust("Bob", 15.50, 12345);

            bob.showCust();
            Console.WriteLine("Press Enter to terminate...");
            Console.Read();
        }
    }
}
