import java.io.*;
public class BINARY_TO_CHAR {
  public static String BinaryToAscii(String binaryString) {
    char nextChar;
    String asciiString = "";
    for(int i=0; i<= binaryString.length()-8; i += 9) {
      nextChar = (char)Integer.parseInt(binaryString.substring(i, i+8), 2);
      asciiString += nextChar;
    }
    return asciiString;
  }
  public static void main(String[] args) throws Exception {
    File file = new File(args[0]);
    BufferedReader br = new BufferedReader(new FileReader(file));
    String st;
    StringBuilder stMaster = new StringBuilder();
    while((st = br.readLine()) != null) {
      stMaster.append(st);
      stMaster.append("\n");
    }
    br.close();
    BufferedWriter out = null;
    try {
      FileWriter fstream = new FileWriter(args[0].substring(0, args[0].length()-16), true);
      out = new BufferedWriter(fstream);
      out.write(BinaryToAscii(stMaster.toString()));
    } catch (IOException e) {
      e.printStackTrace();
    } finally {
      if(out != null) {
        out.close();
      }
    }
  }
}

