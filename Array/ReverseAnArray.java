import java.util.Arrays;

public class ReverseAnArray {
    public static void main(String[] args) {
        char[] arr = {'k', 'u', 'n', 'a', 'l'};
        System.out.println(Arrays.toString(arr) + " is the array.");
        reverse(arr);
        System.out.println(Arrays.toString(arr) + " is the updated array.");
    }
    static void reverse(char[] arr){
        for(int i=0; i< arr.length/2; i++){
            char temp = arr[i];
            arr[i] = arr[arr.length-1-i];
            arr[arr.length-1-i] = temp;
        }
    }

}
