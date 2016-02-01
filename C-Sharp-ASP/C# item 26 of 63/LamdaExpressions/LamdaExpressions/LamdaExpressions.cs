using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

delegate double GetSum(double num1, double num2);

namespace LamdaExpressions
{
    class LamdaExpressions
    {
        static void Main(string[] args)
        {
            // ---------- LAMBDA EXPRESSIONS ----------
            // A lambda expression is used to act as an anonymous function or expression tree

            // You can assign the lambda expression to a function instance
            Func<int, int, int> getSum = (x, y) => x + y;
            Console.WriteLine("5 + 3 = " + getSum.Invoke(5, 3));
            Console.WriteLine("");

            // Get odd numbers from a list
            List<int> numList = new List<int> { 5, 10, 15, 20, 25 };

            // With an Expression Lambda the input goes in the left (n) and the statements go on the right
            List<int> oddNums = numList.Where(n => n % 2 == 1).ToList();

            foreach (int num in oddNums)
            {
                Console.Write(num + ", ");
            }
            Console.WriteLine("");
            Console.WriteLine("Press Enter to terminate...");
            Console.Read();
        }
    }
}
