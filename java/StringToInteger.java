/**
 * Q9. String to Integer (atoi) (Category: Strings)
 *
 * Problem: Implement the myAtoi(string s) function, which converts a string
 *          to a 32-bit signed integer. Handle leading whitespace, optional sign,
 *          non-digit characters, and integer overflow.
 *
 * Approach: Step through the string handling whitespace, sign, digits, and overflow.
 *
 * Time Complexity : O(n)
 * Space Complexity: O(1)
 */
public class StringToInteger {

    public int myAtoi(String s) {
        int i = 0, n = s.length();
        long result = 0;
        int sign = 1;

        // Skip leading whitespace
        while (i < n && s.charAt(i) == ' ') i++;

        // Handle optional sign
        if (i < n && (s.charAt(i) == '+' || s.charAt(i) == '-')) {
            sign = (s.charAt(i) == '-') ? -1 : 1;
            i++;
        }

        // Read digits and handle overflow
        while (i < n && Character.isDigit(s.charAt(i))) {
            result = result * 10 + (s.charAt(i) - '0');
            if (result * sign >= Integer.MAX_VALUE) return Integer.MAX_VALUE;
            if (result * sign <= Integer.MIN_VALUE) return Integer.MIN_VALUE;
            i++;
        }
        return (int) (result * sign);
    }

    public static void main(String[] args) {
        StringToInteger solution = new StringToInteger();
        System.out.println(solution.myAtoi("42"));            // 42
        System.out.println(solution.myAtoi("   -42"));        // -42
        System.out.println(solution.myAtoi("4193 with words")); // 4193
        System.out.println(solution.myAtoi("-91283472332"));  // -2147483648
    }
}
