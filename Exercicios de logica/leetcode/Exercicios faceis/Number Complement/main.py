class Solution:
    def findComplement(self, num: int) -> int:
        def get_bin(nbin):
            return bin(nbin)[2:]

        bin_5 = get_bin(num)
        new_bin = ''.join('1' if b == '0' else '0' for b in bin_5)
        new_num = int(new_bin, 2)
        return new_num
