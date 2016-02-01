using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

class BC
{
    public void Display()
    {
        System.Console.WriteLine("BC::Display");


    }
}
class DC : BC
{
    new public void Display()
    {
        System.Console.WriteLine("DC::Display");

    }
}
class Demo
{
    public static void Main()
    {
        BC b;
        b = new BC();
        b.Display();
        Console.WriteLine("BC");

        b = new DC();
        b.Display();
        Console.WriteLine("DC");
        Console.Read();
        Console.WriteLine("Press Enter to terminate...");
        Console.Read();
    }
}            