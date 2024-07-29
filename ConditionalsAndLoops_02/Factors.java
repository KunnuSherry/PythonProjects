import java.util.Scanner;

//Input a number and print all the factors of that number (use loops).
public class Factors {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.println("Enter The Number: ");
        long num = sc.nextLong();

        for(int i=1; i<=num; i++){
            if(num%i==0){
                System.out.println(i+" is the factor of"+num);
            }
        }
    }
}
