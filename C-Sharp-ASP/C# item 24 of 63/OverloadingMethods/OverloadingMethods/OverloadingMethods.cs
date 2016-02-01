using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace OverloadingMethods
{
    class Animal
    {

        public double height { get; set; }
        public double weight { get; set; }
        public string sound { get; set; }


        public string name;
        public string Name


        {
            get { return name; }
            set { name = value; }
        }


        public Animal()
        {
            this.height = 0;
            this.weight = 0;
            this.name = "No Name";
            this.sound = "No Sound";

            numOfAnimals++;
        }


        public Animal(double height, double weight, string name, string sound)
        {
            this.height = height;
            this.weight = weight;
            this.name = name;
            this.sound = sound;

            numOfAnimals++;
        }


        static int numOfAnimals = 0;


        public static int getNumOfAnimals()
        {
            return numOfAnimals;
        }

        public string toString()
        {
            return String.Format("{0} is {1} inches tall, weighs {2} lbs and likes to say {3}", name, height, weight, sound);
        }

        // Overloading methods works if you have methods with different attribute data types
        // You can give attributes default values
        public int getSum(int num1 = 1, int num2 = 1)
        {
            Console.WriteLine("");
            Console.WriteLine("Overloading the getSum method (int num1 = 1, int num2 = 1)");

            return num1 + num2;
        }

        public double getSum(double num1, double num2)
        {
            Console.WriteLine("");
            Console.WriteLine("Overloading the getSum method (double num1, double num2)");
            return num1 + num2;
        }

        static void Main(string[] args)
        {

            Animal spot = new Animal(15, 10, "Spot", "Woof");


            Console.WriteLine("{0} says {1}", spot.name, spot.sound);


            Console.WriteLine("Number of Animals " + Animal.getNumOfAnimals());

            Console.WriteLine(spot.toString());

            Console.WriteLine("3 + 4 = " + spot.getSum(3, 4));
            Console.WriteLine("");


            Console.WriteLine("3.4 + 4.5 = " + spot.getSum(num2: 3.4, num1: 4.5));
            Console.WriteLine("");


            Animal grover = new Animal
            {
                name = "Grover",
                height = 16,
                weight = 18,
                sound = "Grrr"
            };

            Console.WriteLine(grover.toString());

            Dog spike = new Dog();

            Console.WriteLine(spike.toString());

            spike = new Dog(20, 15, "Spike", "Grrr Woof", "Chicken");

            Console.WriteLine(spike.toString());

            Console.Write("Hit Enter to Exit");
            string exitApp = Console.ReadLine();

        }
    }

    class Dog : Animal
    {
        public string favFood { get; set; }


        public Dog() : base()
        {
            this.favFood = "No Favorite Food";
        }

        public Dog(double height, double weight, string name, string sound, string favFood) :
            base(height, weight, name, sound)
        {
            this.favFood = favFood;
        }

        new public string toString()
        {
            return String.Format("{0} is {1} inches tall, weighs {2} lbs, likes to say {3} and eats {4}", name, height, weight, sound, favFood);
        }

    }
}
