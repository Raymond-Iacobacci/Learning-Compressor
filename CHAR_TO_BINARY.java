import java.io.*;
public class CHAR_TO_BINARY {
  public static String AsciiToBinary(String asciiString){  

          byte[] bytes = asciiString.getBytes();  
          StringBuilder binary = new StringBuilder();  
          for (byte b : bytes)  
          {  
             int val = b;  
             for (int i = 0; i < 8; i++)  
             {
                binary.append((val & 128) == 0 ? 0 : 1);
                val <<= 1;
             }
          }
          return binary.toString();  
    }
  public static void main(String [] args) throws Exception {
    File file = new File(args[0]);
    BufferedReader br = new BufferedReader(new FileReader(file));
    String st;
    StringBuilder stMaster = new StringBuilder();
    while((st = br.readLine()) != null) {
      stMaster.append(st); 
      stMaster.append("\n");
    }
    BufferedWriter out = null;
    try {
      FileWriter fstream = new FileWriter(args[0]+".binary_encoding", true);
      out = new BufferedWriter(fstream);
      out.write(AsciiToBinary(stMaster.toString()));
    } catch (IOException e) {
      e.printStackTrace();
    } finally {
      if(out != null) {
        out.close();
      }
    }
  }
}
