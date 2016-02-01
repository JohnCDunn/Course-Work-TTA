using System;
using System.IO;
using System.Collections;
using System.Runtime.Serialization.Formatters.Binary;
using System.Runtime.Serialization;
using System.Text;

public class App
{
    [STAThread]
    static void Main()
    {
        Serialize();
        Deserialize();
    }

    static void Serialize()

    {
        int CHUNK_SIZE = 1024;
        // Create a hashtable of values that will eventually be serialized.
        Hashtable addresses = new Hashtable();
        addresses.Add("Jeff", "123 Main Street, Redmond, WA 98052");
        addresses.Add("Fred", "987 Pine Road, Phila., PA 19116");
        addresses.Add("Mary", "PO Box 112233, Palo Alto, CA 94301");

        Console.WriteLine("Initial Hash Table");
        foreach (DictionaryEntry de in addresses)
        {
            Console.WriteLine("{0} lives at {1}.", de.Key, de.Value);
        }


        // To serialize the hashtable and its key/value pairs,  
        // you must first open a stream for writing. 
        // In this case, use a file stream.
        FileStream fs = new FileStream("DataFile.dat", FileMode.Create);

        // Construct a BinaryFormatter and use it to serialize the data to the stream.
        BinaryFormatter formatter = new BinaryFormatter();
        try
        {
            formatter.Serialize(fs, addresses);
        }
        catch (SerializationException e)
        {
            Console.WriteLine("Failed to serialize. Reason: " + e.Message);
            throw;
        }
        finally
        {
            fs.Seek(0, SeekOrigin.Begin);
            Console.WriteLine("Reset the file to the beginning, display file contents, Binary");
            Console.WriteLine("Serialized");
            {
                using (BinaryReader br = new BinaryReader(fs, new ASCIIEncoding()))
                {
                    byte[] chunk;

                    chunk = br.ReadBytes(CHUNK_SIZE);
                    while (chunk.Length > 0)
                    {
                        DumpBytes(chunk, chunk.Length);
                        chunk = br.ReadBytes(CHUNK_SIZE);
                    }
                }
            }
        }
    }

    public static void DumpBytes(byte[] bdata, int len)
    {
        int i;
        int j = 0;
        char dchar;
        // 3 * 16 chars for hex display, 16 chars for text and 8 chars
        // for the 'gutter' int the middle.
        StringBuilder dumptext = new StringBuilder("        ", 16 * 4 + 8);
        for (i = 0; i < len; i++)
        {
            dumptext.Insert(j * 3, String.Format("{0:X2} ", (int)bdata[i]));
            dchar = (char)bdata[i];
            //' replace 'non-printable' chars with a '.'.
            if (Char.IsWhiteSpace(dchar) || Char.IsControl(dchar))
            {
                dchar = '.';
            }
            dumptext.Append(dchar);
            j++;
            if (j == 16)
            {
                Console.WriteLine(dumptext);
                dumptext.Length = 0;
                dumptext.Append("        ");
                j = 0;
            }
        }
        // display the remaining line
        if (j > 0)
        {
            for (i = j; i < 16; i++)
            {
                dumptext.Insert(j * 3, "   ");
            }
            Console.WriteLine(dumptext);
        }
    }
    static void Deserialize()
    {
        // Declare the hashtable reference.
        Hashtable addresses = null;

        // Open the file containing the data that you want to deserialize.
        FileStream fs = new FileStream("DataFile.dat", FileMode.Open);
        try
        {
            BinaryFormatter formatter = new BinaryFormatter();

            // Deserialize the hashtable from the file and 
            // assign the reference to the local variable.
            addresses = (Hashtable)formatter.Deserialize(fs);
        }
        catch (SerializationException e)
        {
            Console.WriteLine("Failed to deserialize. Reason: " + e.Message);
            throw;
        }
        finally
        {
            fs.Close();
        }

        // To prove that the table deserialized correctly, 
        // display the key/value pairs.
        Console.WriteLine("deserialized");
        foreach (DictionaryEntry de in addresses)
        {
            Console.WriteLine("{0} lives at {1}.", de.Key, de.Value);
            

        }
        Console.WriteLine("Press Enter to terminate...");
        Console.Read();
    }
}
 