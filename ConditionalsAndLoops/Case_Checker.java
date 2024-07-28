//To Check Whether a String is Upper Case or Lower Case
import java.util.Scanner;

public class Case_Checker {
    public static void main(String[] args) {
        System.out.print("Enter a String: ");
        Scanner input = new Scanner(System.in);
        String st = input.next();
        char ch = st.trim().charAt(0);
        //Method1:
//        if(ch>='a' && ch<='z'){
//            System.out.println("Lower Case");
//        }
//        else{
//            System.out.println("Upper Case");
//        }
        //Method 2:
        if(Character.isUpperCase(ch)){
            System.out.println("Upper Case");
        }
        else{
            System.out.println("Lower Case");
        }
    }
}
