import java.util.Scanner;

//Check whether a number is Palindrome or not
public class Palindrome {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number: ");
        int num = sc.nextInt();
        String numSt = Integer.toString(num);
        int length = numSt.length();
        boolean isPalindrome = true;
        for(int i=0; i<length; i++){
            if(numSt.charAt(i)!=numSt.charAt(length-i-1)){
                isPalindrome = false;
                break;
            }
        }
        if(isPalindrome){
            System.out.println("Is a Palindrome");
        }
        else{
            System.out.println("Is not a Palindrome");
        }
    }
}
