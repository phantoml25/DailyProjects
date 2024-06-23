/*********************************
 * Daily Project June 10th - Kevin Adams
 * 
 * The number 6174 is known as Kaprekar's contant, after the mathematician who discovered an associated property: for all four-digit numbers with at least two distinct digits, repeatedly applying a simple procedure eventually results in this value. The procedure is as follows:
 *
 *  1. For a given input x, create two new numbers that consist of the digits in x in ascending and descending order.
 *  2. Subtract the smaller number from the larger number.
 *
 * Write a function that returns how many steps this will take for a given input N.
 *
 *********************************/

import java.io.BufferedReader;
import java.io.IOException;
import java.io.InputStreamReader;
import java.util.ArrayList;

public class Kaprekar {
    public static int Kaprekar_Num = 6174;
    //First, Create a short script to run the algorithm and count the steps
    public static void main(String[] args)
        throws IOException
    {
        //Enter Data using BufferReader
        BufferedReader reader = new BufferedReader(
            new InputStreamReader(System.in));
        
        // Reading data using readLine
        System.out.print("Enter Number to test: ");
        String input = reader.readLine();

        int origin = Integer.parseInt(input);
        int current_num = origin;
        int count = 0;
        while (current_num != Kaprekar_Num) {
            String num_str = String.valueOf(current_num);
            String[] digits = num_str.split("");
            //Insertion Sort array, we will read it into a reversed list after
            for (int i = 1; i< digits.length;i++){
                int key = Integer.parseInt(digits[i]);
                int j = i-1;
                while (j>=0 && Integer.parseInt(digits[j])>key){
                    digits[j+1] = digits[j];
                    j = j-1;
                }
                digits[j+1] = String.valueOf(key);
            }
            String[] rev_digits = new String[digits.length];
            String str1 = "";
            String str2 = "";
            for (int i=0;i<digits.length;i++){
                rev_digits[i] = digits[digits.length-i-1];
                str1 = str1+digits[i];
                str2 = str2+rev_digits[i];
            }
            int num1 = Integer.parseInt(str1);
            int num2 = Integer.parseInt(str2);
            //now subtract the two numbers and increment count
            if (num1>=num2){
                current_num = num1-num2;
                String result = num1+ " - " + num2 + " = " + current_num;
                System.out.println(result);
            }
            else{
                current_num = num2-num1;
                String result = num2+ " - " + num1 + " = " + current_num;
                System.out.println(result);
            }
            count++;
        };
        
        System.out.print("Number of loops:");
        System.out.print(count);
    }
    //Second, attempt an algorithm to count the steps without needing to actually run them
}
