class Solution {
public:
    int sum(int num1, int num2) {
        while(num2 != 0){
            int carry = num1 & num2;
            num1 = num1^num2;
            num2 = (carry & 0xffffffff)<< 1;
        }
        return num1;
    }
};