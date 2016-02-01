using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ValueVSReferenceTypes
{
    
    class Program
    {
        
        static void Main(string[] args)
        {
            Console.WriteLine("This is a value type");
            int x = 5;
            Console.WriteLine("int x = " + x);
            int y = x;
            Console.WriteLine("int y = x, value of y = " + y);
            y = 10;
            Console.WriteLine("now y = 10, value of x = " + x + ", value of y = " + y);
            Change(x);
            Console.WriteLine("After calling function x = " + x);

            Console.WriteLine();
            Console.WriteLine("This is a reference type");
            Console.WriteLine("Reference type creates a pointer to the data");
            Student s = new Student();
            s.id = 6;
            s.name = "Bob";
            Console.WriteLine("new student ID = " + s.id + " Name = " + s.name);
            ChangeStudent(s);
            Console.WriteLine("changed student ID = " + s.id + " and name = " + s.name + " after function call");




            Console.WriteLine();

            Console.WriteLine("Press Enter to terminate...");
            Console.Read();
        }
        static void Change(int x)
        {
            Console.WriteLine("Change x in a function");
            x = 500;
            Console.WriteLine("Function x = " + x);
        }

        static void ChangeStudent(Student s)
        {
            Console.WriteLine("Change student ID and name in a function");
            s.id = 12;
            s.name = "clyde";
            Console.WriteLine("Changed student ID = " + s.id + " and name = " + s.name + " inside function");


        }
    }
    
}
