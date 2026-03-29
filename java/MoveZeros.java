import java.util.Arrays;

/**
 * Q3. Move Zeros (Category: Arrays)
 *
 * Problem: Move all zeros to the end of the array while maintaining
 *          the relative order of non-zero elements. Do it in-place.
 *
 * Approach: Two-pointer technique. Keep a pointer for the next non-zero position.
 *
 * Time Complexity : O(n)
 * Space Complexity: O(1)
 */
public class MoveZeros {

    public void moveZeroes(int[] nums) {
        int insertPos = 0;
        // Move all non-zero elements forward
        for (int num : nums) {
            if (num != 0) {
                nums[insertPos++] = num;
            }
        }
        // Fill remaining positions with zeros
        while (insertPos < nums.length) {
            nums[insertPos++] = 0;
        }
    }

    public static void main(String[] args) {
        MoveZeros solution = new MoveZeros();
        int[] nums = {0, 1, 0, 3, 12};
        solution.moveZeroes(nums);
        System.out.println(Arrays.toString(nums)); // [1, 3, 12, 0, 0]
    }
}
