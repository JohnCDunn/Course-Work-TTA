using System;
using System.Collections.Generic;
using System.Linq;
using System.Text;
using System.Threading.Tasks;

namespace Generics
{
    class Generic
    {

        static void Main(string[] args)
        {

            // ---------- GENERICS ----------
            // With Generics you don't have to specify the data type of an element in a class or method
            KeyValue<string, string> superman = new KeyValue<string, string>("", "");
            superman.key = "Superman";
            superman.value = "Clark Kent";
            superman.showData();

            // Now use completely different types
            KeyValue<int, string> samsungTV = new KeyValue<int, string>(0, "");
            samsungTV.key = 123456;
            samsungTV.value = "a 50in Samsung TV";
            samsungTV.showData();

            Console.Write("Hit Enter to Exit");
            string exitApp = Console.ReadLine();

        }
        // ---------- GENERIC CLASS ----------

        class KeyValue<TKey, TValue>
        {
            public TKey key { get; set; }
            public TValue value { get; set; }

            public KeyValue(TKey k, TValue v)
            {
                key = k;
                value = v;
            }

            public void showData()
            {
                Console.WriteLine("{0} is {1}", this.key, this.value);
            }

        }

    }

    
}
