//Check Whether the number is armstrong number.

import java.util.Scanner;

public class ArmstrongNumber {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        System.out.print("Enter the number: ");
        int num = sc.nextInt();
        int length = Integer.toString(num).length();
        int num1=num;
        int ans=0;
        for(int i=0; i<length; i++){
            int rem = num1%10;
            ans += Math.pow(rem,length);
            num1/=10;
        }
        if(ans==num){
            System.out.println(num+ " is an Armstrong Number.");
        }
        else{
            System.out.println(num+ " is not an Armstrong Number.");
        }
    }
}
