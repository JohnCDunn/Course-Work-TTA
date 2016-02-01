using System;
using System.Collections.Generic;
using System;
public class Employee
{
    public string name;
    public string alias;
    public decimal salary = 3000.00m;

    // Constructor:
    public Employee(string name, string alias)
    {
        // Use this to qualify the fields, name and alias:
        this.name = name;
        this.alias = alias;
    }

    // Printing method:
    public void printEmployee()
    {
        Console.WriteLine("Name: {0}\nAlias: {1}", name, alias);
        // Passing the object to the CalcTax method by using this:
        Console.WriteLine("Taxes: {0:C}", Tax.CalcTax(this));
        Console.WriteLine("Press Enter to terminate...");
        Console.Read();
    }
}
public class Tax
{
    public static decimal CalcTax(Employee E)
    {
        return (0.08m * (E.salary));
    }
}

public class MainClass
{
    public static void Main()
    {
        // Create objects:
        Employee E1 = new Employee("John M. Trainer", "jtrainer");

        // Display results:
        E1.printEmployee();
    }
}
