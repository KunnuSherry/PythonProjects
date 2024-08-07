import java.lang.reflect.Array;
import java.util.Arrays;
import java.util.Scanner;

public class SwapElementsOfArray   {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        int[] arr = {34,12,23,56,67};
        System.out.println(Arrays.toString(arr) + " is the array. Write the indices to be swapped: ");
        System.out.print("Index 1 : ");
        int ind1 = sc.nextInt();
        System.out.print("Index 2 : ");
        int ind2 = sc.nextInt();
        swap(arr, ind1, ind2);
        System.out.println(Arrays.toString(arr)+ " is the updated array.");
    }
    static void swap(int[] arr, int index1, int index2){
        int temp = arr[index1];
        arr[index1] = arr[index2];
        arr[index2] = temp;
    }
}
