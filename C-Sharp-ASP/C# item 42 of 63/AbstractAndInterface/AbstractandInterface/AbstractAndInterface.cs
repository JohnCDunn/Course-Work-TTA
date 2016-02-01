using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace AbstractAndInterface
{
    abstract class M1
    {
        public int add(int a, int b)
        {
            Console.WriteLine("Abstract Creation and Usage");
            Console.WriteLine("Using Class M1");
            return (a + b);
        }
    }
    class M2 : M1
    {
        public int mul(int a, int b)
        {
            Console.WriteLine("Using Class M2");
            return a * b;
        }
    }
    public interface ITransactions
    {
        // interface members
        void showTransaction();
        double getAmount();
    }

    public class Transaction : ITransactions
    {
        private string tCode;
        private string date;
        private double amount;
        public Transaction()
        {
            tCode = " ";
            date = " ";
            amount = 0.0;
        }

        public Transaction(string c, string d, double a)
        {
            tCode = c;
            date = d;
            amount = a;
        }

        public double getAmount()
        {
            return amount;
        }

        public void showTransaction()
        {
            Console.WriteLine("Transaction: {0}", tCode);
            Console.WriteLine("Date: {0}", date);
            Console.WriteLine("Amount: {0}", getAmount());
        }
    }
    class test
    {
        static void Main(string[] args)
        {
            M2 ob = new M2();
            int result = ob.add(10, 20);
            Console.WriteLine("the result is {0}", result);
            result = ob.mul(10, 20);
            Console.WriteLine("the result is {0}", result);

            Console.WriteLine();
            Console.WriteLine("Creation and usage of an iterface");
            Transaction t1 = new Transaction("001", "8/10/2012", 78900.00);
            Transaction t2 = new Transaction("002", "9/10/2012", 451900.00);
            t1.showTransaction();
            t2.showTransaction();
            Console.ReadKey();

        }
    }
}
