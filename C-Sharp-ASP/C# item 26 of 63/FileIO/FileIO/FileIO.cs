﻿using System;
using System.Collections.Generic;
using System.IO;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace FileIO
{
    class FileIO
    {
        static void Main(string[] args)
        {
            // ---------- FILE I/O ----------
            // The StreamReader and StreamWriter allows you to create text files while reading and
            // writing to them

            string[] custs = new string[] { "Tom", "Paul", "Greg" };

            using (StreamWriter sw = new StreamWriter("custs.txt"))
            {
                foreach (string cust in custs)
                {
                    sw.WriteLine(cust);
                }
            }

            string custName = "";
            using (StreamReader sr = new StreamReader("custs.txt"))
            {
                while ((custName = sr.ReadLine()) != null)
                {
                    Console.WriteLine(custName);
                }
            }

            Console.Write("Hit Enter to Exit");
            string exitApp = Console.ReadLine();
 
        }
    }
}
