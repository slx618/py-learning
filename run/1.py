class Solution:
    """
    @param s: The first string
    @param b: The second string
    @return true or false
    """

    def anagram1(self, s, t):
        # write your code here
        int_s_count = 0
        int_t_count = 0

        for a in s:
            int_s_count += ord(a)

        for b in t:
            int_t_count += ord(b)

        if (int_s_count != int_t_count):
            return False
        else:
            return True

    def anagram2(self, s, t):
        # write your code here

        int_s_length = len(s)
        int_t_length = len(t)

        if ( int_s_length != int_t_length ):
            return False

        count = []
        count1 = []
        for a in s:
            count.append(a)

        for b in t:
            count1.append(b)

        if ( set(count) != set(count1) ):
            return False
        else:
            return True


    def anagram(self, s, t):
        # write your code here

        int_s_length = len(s)
        int_t_length = len(t)

        if (int_s_length != int_t_length):
            return False

        count = []
        count1 = []
        for a in s:
            count.append(a)

        for b in t:
            count1.append(b)

        count.sort()
        count1.sort()
        if (count != count1):
            return False
        else:
            return True


a = Solution()
print(a.anagram('abed', 'aedb'))