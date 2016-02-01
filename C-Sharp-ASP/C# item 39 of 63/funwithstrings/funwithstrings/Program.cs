using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace funwithstrings
{
    class Program
    {
        static void Main(string[] args)
        {
            string str1 =  "hi ";
            Console.WriteLine("First instance of str1 = " + str1);
            str1 += "hello "; // New string instance will be created, instead of changing the old one
            Console.WriteLine("Second instance of str1 = " + str1);
            str1 += "hw r u"; // One more instance of str1
            Console.WriteLine("Third instance of str1 = " + str1);
            Console.WriteLine("String str = " + str1);
            Console.WriteLine("");

            StringBuilder sb = new StringBuilder("");
            sb.Append("hi ");
            sb.Append("Hello ");
            sb.Append("hw r u");
            string str2 = sb.ToString();
            Console.WriteLine("Only one instance of str2 = " + str2);
            Console.WriteLine("StringBuilder str = " + str2);

            Console.WriteLine("");
            Console.WriteLine("Press Enter to terminate...");
            Console.Read();

        }
    }
}
