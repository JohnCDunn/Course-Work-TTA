using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
using AssemblyOne;
using AssemblyTwo;
using AssemblyThree;


namespace InternalProtectedInternal
{
    class ExecuteInternal
    {
        static void Main(string[] args)
        {
            Console.WriteLine("Created three assemblies for DEMO");
            Console.WriteLine("All Assemblies have one field, Ax_ID:");
            Console.WriteLine("");


            Console.WriteLine("Using AssemblOneClass to display A1_ID will not compile becauese A1_ID is internal to AssemblyOneClass");
            Console.WriteLine("");
            AssemblyOneClass As1 = new AssemblyOneClass();
            //As1.A1_ID;

            Console.WriteLine("Using AssemblTwoClass to display A2_ID will not compile becauese the AssemblyTwoClass is internal");
            Console.WriteLine("");
            //AssemblyTwoClass As2 = new AssemblyTwoClass();

            Console.WriteLine("We can instantiate the AssemblyThreeClass!");
            Console.WriteLine("We cannot access A3_ID because it is defined as internal to AssemblyThreeClass");
            Console.WriteLine("");
            AssemblyThreeClass As3 = new AssemblyThreeClass();
            //AssemblyThreeClass.A3_ID = 333;

            Console.WriteLine("Press Enter to terminate...");
            Console.Read();
     
        }

    }
   
}
