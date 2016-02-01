using System;

namespace AccessModifiers
{
    class Modifiers
    {
        static void AAA()
        {
            Console.WriteLine("Called the AAA method from withing the Modifiers class");
            Console.WriteLine("Modifiers AAA");
        }

        public static void BBB()
        {
            Console.WriteLine("the BBB method has a Public Modifier anyone can access this.");
            Console.WriteLine("Modifiers BBB");
            AAA();
            CCC();
        }

        protected static void CCC()
        {
            Console.WriteLine("Called the CCC method from withing the Modifiers class");
            Console.WriteLine("Modifiers CCC");
        }
    }

    class ModifiersBase
    {
        static void AAA()
        {
            Console.WriteLine("ModifiersBase AAA private static void");
        }
        public static void BBB()
        {
            Console.WriteLine("ModifiersBase BBB public static void");
            AAA();
        }
        protected static void CCC()
        {
            Console.WriteLine("ModifiersBase CCC protected static void");
        }
    }

    class ModifiersDerived : ModifiersBase
    {
        public static void XXX()
        {
            Console.WriteLine("ModifiersBase AAA cannot be accessed because of the private protection level");
            BBB();
            CCC();
        }
    }

    class Program
    {
        static void Main(string[] args)
        {
            Console.WriteLine("The AAA method is by default private and cannot be accessed out side the Modifiers Class");
            Console.WriteLine("The CCC method is protected and cannot be accessed out side the Modifiers Class");
            Modifiers.BBB();
            
            Console.WriteLine("");
            Console.WriteLine("ModifiersDerived !!!!!");
            ModifiersDerived.XXX();
            Console.WriteLine("Press Enter to terminate...");
            Console.Read();

        }
    }
}