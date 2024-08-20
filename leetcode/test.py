class Solution:
    def reverseBits(self, n: int) -> int:
        # Initializing the result to 0 
        result = 0 

        for i in range(32):
            # print("------")
            # Extract the least significant bit
            # Since 1 equates to 0000...01, think of this as a mask
            # Doing an & operation where only the last digit is 1 will give you the least significant bit because -- 
            # --- an add operation with anything but 1 will be 0
            leastSignificantBit = n & 1

            print("Extracted least significant bit: ", leastSignificantBit)

            # right shift the integer to get the next digit
            n = n >> 1

            # Shift the least significant bit to the left first so that you don't override the bit set from the last loop
            # This step is how we'll get the reversed bits at the end of the loop
            result = result << 1

            # Once you have the least significant bit, assign this bit to the least significant bit of the result variable
            result = result | leastSignificantBit

            print("Result variable: ", leastSignificantBit)
        
        return result
    n = 00000010100101000001111010011100
    print(reverseBits(n))