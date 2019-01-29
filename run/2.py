class Solution:
    def strStr(self, source, target):
        # write your code here

        if ( source == '' and target == '' ):
            return 0

        int_source_len = len(source)
        int_target_len = len(target)
        if (int_source_len == 0 or int_target_len == 0):
            return -1

        j = 0
        z = 0

        while (True):

            if (j + 1 > int_source_len):
                return -1

            if (source[j] == target[z]):
                if (z + 1 == int_target_len):
                    return 1
            z += 1

            if (z + 1 > int_target_len):
                j += 1
                z = 0

a = Solution()
print(a.strStr('abcdabcdefg', 'dab'))