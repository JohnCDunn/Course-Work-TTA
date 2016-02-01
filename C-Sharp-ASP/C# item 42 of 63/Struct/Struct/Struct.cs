using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

struct SimpleStruct
{
    private int xval;
    public int X
    {
        get
        {
            return xval;
        }
        set
        {
            if (value < 100)
                xval = value;
        }
    }
    public void DisplayX()
    {
        Console.WriteLine("The stored value is: {0}", xval);


            Console.WriteLine("Press Enter to terminate...");
            Console.Read();


    }
}

class TestClass
{
    public static void Main()
    {
        Console.WriteLine("instaniante a ss structure object");
        SimpleStruct ss = new SimpleStruct();
        Console.WriteLine("Set the integer to 5 in the ss structure object");
        ss.X = 5;
        Console.WriteLine("Call the Displayx function in the ss structure object");
        ss.DisplayX();
    }
}