using System;
using System.IO;
using System.Linq;

class GetFiles {

    public string[] findFiles(string directory) {

        int i = 0;

        System.IO.DirectoryInfo dir = new System.IO.DirectoryInfo(directory);
        int fileCount = Directory.GetFiles(directory, "*.*", SearchOption.AllDirectories).Length;
        string[] files = new string[fileCount];

        foreach (System.IO.FileInfo f in dir.GetFiles("*.*"))
        {
            string[] array = new string[2];
            DateTime datetime = f.LastWriteTime;
            string format = "u";   // Use this format.
            array[0] = f.Name;
            array[1] = datetime.ToString(format);
            string result = string.Join("#", array);
            files[i] = result;
            i++;
        }

        return files;
    }
}


class CheckDates
{

    public string[] checkDates(string[] fileList)
    {
        int numOfFiles = fileList.Length;
        string[] xferFiles = new string[numOfFiles]; 

        DateTime todaysDate = DateTime.Now;

        //Capture hours mins & secs of current dateTime
        int TDHour = todaysDate.Hour;
        int TDMin = todaysDate.Minute;
        int TDSec = todaysDate.Second;
        int y = 0;

        DateTime yesterday = DateTime.Today.AddDays(-1);

        //update yesterdays dateTime with"the correct Hours, Min & Secs from current Date4Time
        yesterday = yesterday.AddHours(TDHour).AddMinutes(TDMin).AddSeconds(TDSec);

        string todaysDateFormatted = todaysDate.ToString("yyyyMMddHHmmss");
        string yesterdaysDateFormatted = yesterday.ToString("yyyyMMddHHmmss");
      
        char[] delimiterChars = { '#' };

        foreach (string value in fileList)
        {
            string[] FileAndDate = value.Split(delimiterChars);

            string fileDate = FileAndDate[1];
            string fileRecord = value;
            
            int index = 0;
            char[] result1 = new char[fileDate.Length];
            for (int i = 0; i < fileDate.Length; i++)
            {
                if (fileDate[i] != '-'
                &&  fileDate[i] != ':'
                &&  fileDate[i] != 'Z'
                &&  fileDate[i] != ' ')
                {
                    result1[index++] = fileDate[i];
                }
            }
     
            string result3 = new string(result1);

            long fileIntDate = Convert.ToInt64(result3);
            long yesterdayIntDate = Convert.ToInt64(yesterdaysDateFormatted);
            long todayIntDate = Convert.ToInt64(todaysDateFormatted);

            Console.WriteLine("Yesterday = " + yesterdayIntDate);
            Console.WriteLine("FIle Date = " + fileIntDate);
            Console.WriteLine("Today     = " + todayIntDate);
            Console.WriteLine("");

            if (fileIntDate >= yesterdayIntDate
            && fileIntDate <= todayIntDate)
            { 
                xferFiles[y] = fileRecord;
                y++;
                Console.WriteLine("Found One: " + fileRecord + " " + y);
            }

        }
        
        return xferFiles;
    }
}



class TransferFiles
{
    public void transferFiles(string[] xferFiles, string fromDir, string toDir)
    {
        System.IO.DirectoryInfo fromDirectory = new System.IO.DirectoryInfo(fromDir);
        System.IO.DirectoryInfo toDirectory = new System.IO.DirectoryInfo(toDir);

        int numOfFiles = xferFiles.Length;

        char[] delimiterChars = { '#' };


        for (int i = 0; i < xferFiles.Length; i++)
        {
            if (xferFiles[i] != null)
            {
                string[] FileAndDate = xferFiles[i].Split(delimiterChars);
                string fileName = FileAndDate[0];
                string fromXfrDir = fromDir + "//" + fileName;
                string toXfrDir = toDir + "//" + fileName;
                File.Move(fromXfrDir, toXfrDir);
            }
        }
    }
}

class Program
{
    static void Main(string[] args)
    {
        string fromDir = "C://Users//Student//Desktop//From";
        string toDir = "C://Users//Student//Desktop//To";
        string[] fileList;
        string[] xferFiles;
        
        GetFiles fl = new GetFiles();
        fileList = fl.findFiles(fromDir);
  
        CheckDates cd = new CheckDates();
        xferFiles = cd.checkDates(fileList);

        TransferFiles tf = new TransferFiles();
        tf.transferFiles(xferFiles, fromDir, toDir);

        Console.WriteLine("Press Enter to terminate...");
        Console.Read();
    }
}


    
        





