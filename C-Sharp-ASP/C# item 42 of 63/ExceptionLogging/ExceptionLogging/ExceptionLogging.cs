using System;
using System.IO;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace ExceptionLogging
{
    class ExceptionLogging
    {
        public static void Main(string[] args)
        {
            StreamReader streamReader = null;
            try
            {
                streamReader = new StreamReader(@"C:\Users\Student\Text\Data.txt");
                Console.WriteLine(streamReader.ReadToEnd());
                           }
            catch (Exception ex)
            {
                string filePath = @"C:\Users\Student\Text\Log.txt";
                if (File.Exists(filePath))
                {
                    StreamWriter sw = new StreamWriter(filePath);
                    sw.Write(ex.GetType().Name);
                    sw.WriteLine();
                    sw.Write(ex.Message);
                    sw.Close();
                    Console.WriteLine("There is a Problem, Please try later");
                }
                else
                {
                    throw new FileNotFoundException(filePath + " is not present", ex);
                }


                Console.WriteLine(ex.Message);
               
            }
            finally
            {
                if (streamReader != null)
                {
                    streamReader.Close();
                }
                
                Console.WriteLine("Finally Block");
                Console.Read();
            }
        }
        
    }
}
