using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

class BC
{
    public virtual void Display()
    {
        System.Console.WriteLine("BC Class no override");
        System.Console.WriteLine("BC::Display");
    }
}

class DC : BC
{
    public override void Display()
    {
        System.Console.WriteLine("DC overiding BC Class");
        System.Console.WriteLine("DC::Display");
    }
}

class TC : DC
{
    public override void Display()
    {
        System.Console.WriteLine("TC overiding DC Class");
        System.Console.WriteLine("TC::Display");
    }
}


class Test
{
    static void Foo(int x)
    {
        Console.WriteLine("Overloading the Foo class with int");

        Console.WriteLine("Foo(int x) = " + x);
       
    }
    static void Foo(double y)
    {
        Console.WriteLine("Overloading the Foo class with double");
        Console.WriteLine("Foo(double y) = " + y);
        
    }

    static void Main()
    {
        Console.WriteLine("Overloading");
        Foo(105);
        Foo(18039932103);

        //Overriding
        Console.WriteLine("");
        Console.WriteLine("Overriding");
        BC b;
        b = new BC();
        b.Display();

        b = new DC();
        b.Display();

        b = new TC();
        b.Display();
        Console.Read();
    }
}

