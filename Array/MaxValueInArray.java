public class MaxValueInArray {
    public static void main(String[] args) {
        int[] arr = {1,3,23,34,4,12};
        int length = arr.length;
        System.out.println(maxNum(arr, length));;
    }
    static String maxNum(int[] arr, int length){
        int max=0;
        for(int i=0; i<length; i++ ){
            if(arr[i]>max){
                max=arr[i];
            }
        }
        return max+ " is the Greatest Number.";
    }
}
