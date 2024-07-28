import java.util.Scanner;

public class Counting_Occurence {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter the number: ");
        long num = sc.nextLong();
        System.out.println("Enter the number to be checked: ");
        int numCheck = sc.nextInt();
        int length = Long.toString(num).length();
        int occurence = 0;
        long num1 = num;
        for(int i=1; i<=length; i++){
            long rem = num1 % 10;
            if(rem==numCheck){
                occurence+=1;
            }
            num1/=10;

        }
        System.out.println(numCheck+ " Occured For "+ occurence+ " Times");
    }
}
