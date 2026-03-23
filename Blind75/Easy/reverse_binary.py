class Solution:
    def reverseBits(self, n: int) -> int:
        #Method 1
        result = 0
        for i in range(32):  # MUST process all 32 bits!
            result = (result << 1) | (n & 1)  # Take rightmost bit of n, add to result
            n = n >> 1                        # Shift n right
        return result

        #Method 2
        binary = format(n, '032b')
        binary_reversed = binary[::-1]
        return int(binary_reversed, 2)

if __name__ == "__main__":
    #print(Solution().reverseBits(1))
    num = 10
    result = 0
    for i in range(4):
        result = (result << 1) | (num & 1)
        print(result)