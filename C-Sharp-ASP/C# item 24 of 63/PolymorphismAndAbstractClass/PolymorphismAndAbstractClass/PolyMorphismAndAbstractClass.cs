using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;
 
namespace PolymorphismAndAbstract
{
    class Shapes
    {

        static void Main(string[] args)
        {
            Console.WriteLine("Using an Abstract Class to Determine what shape to calculate the area");
            Console.WriteLine("using this abstract class we can calculate the area for a Triangle or Rectangle, polymorphism");


            // One way to implement polymorphism is through an abstract class
            Shape rect = new Rectangle(5, 5);
            Shape tri = new Triangle(5, 5);
            Console.WriteLine("Rect Area " + rect.area());
            Console.WriteLine("Trit Area " + tri.area());

            // Using the overloaded + on 2 Rectangles
            Rectangle combRect = new Rectangle(5, 5) + new Rectangle(5, 5);

            Console.WriteLine("combRect Area = " + combRect.area());

            Console.Write("Hit Enter to Exit");
            string exitApp = Console.ReadLine();

        }
    }

    // Abstract classes define methods that must be defined by derived classes
    // You can only inherit one abstract class per class
    // You can't instantiate an abstract class
    abstract class Shape
    {

        public abstract double area();

        
        // An abstract class can contain complete or default code for methods
        public void sayHi()
        {
            Console.WriteLine("Hello");
        }
    }

    // A class can have many interfaces
    // An interface can't have concrete code
    public interface ShapeItem
    {
        double area();
    }

    class Rectangle : Shape
    {
        private double length;
        private double width;

        public Rectangle(double num1, double num2)
        {
            length = num1;
            width = num2;
        }

        public override double area()
        {
            return length * width;
        }

        // You can redefine many built in operators so that you can define what happens when you
        // add to Rectangles
        public static Rectangle operator +(Rectangle rect1, Rectangle rect2)
        {
            double rectLength = rect1.length + rect2.length;
            double rectWidth = rect1.width + rect2.width;

            return new Rectangle(rectLength, rectWidth);

        }

    }

    class Triangle : Shape
    {
        private double theBase;
        private double height;

        public Triangle(double num1, double num2)
        {
            theBase = num1;
            height = num2;
        }

        public override double area()
        {
            return .5 * (theBase * height);
        }
    }

    
}

