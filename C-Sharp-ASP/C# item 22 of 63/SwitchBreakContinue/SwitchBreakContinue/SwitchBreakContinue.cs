using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace SwitchBreakContinue
{
    class SwitchBreakContinue
    {
        static void Main(string[] args)
        {
            // Switch is used when you have limited options
            // F2all through isn't allowed with C# unless there are no statements between cases
            // You can't check multiple values at once

            int age = 0;

            switch (age)
            {
                case 0:
                    Console.WriteLine("Infant");
                    break;
                case 1:
                case 2:
                    Console.WriteLine("Toddler");

                    // Goto can be used to jump to a label elsewhere in the code
                    goto Cute;
                default:
                    Console.WriteLine("Child");
                    break;
            }

            // Lable we can jump to with Goto
            Cute:
            Console.WriteLine("Toddlers are cute");

            Console.WriteLine("Press Enter to terminate...");
            Console.Read();

        }
    }
}
