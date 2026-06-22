class Solution(object):
    def isPalindrome(self, s):
        lst=list(s)
        clean=[]
        for i in lst:
            if i.isalnum():
                clean.append(i.lower())
        return clean == clean[::-1]
        