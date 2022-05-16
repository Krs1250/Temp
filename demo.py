from cgi import print_arguments


class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s = list(s)
        t = list(t)

        n=0
        m=0
        l=0
        for i in range(len(s)):
            if s[i] == "#":
                if i != 0:
                    n += 1
                    l = len(s)-2*n
                    for j in range(i-1,l):
                        s[j]=s[j+2]
                    i -= 2
                elif i == 0:
                    while s[0] == "#":
                        m += 1
                        for j in range(0,len(s)-m):
                            s[j] = s[j+1]
        s = s[:len(s)-2*n]
        print(n,m)
        n=0
        m=0
        l=0
        for i in range(len(t)):
            if t[i] == "#":
                if i != 0:
                    n += 1
                    l = len(t)-2*n
                    for j in range(i-1,l):
                        t[j]=t[j+2]
                    i -= 2
                elif i == 0:
                    while t[0] == "#":
                        m += 1
                        for j in range(0,len(t)-m):
                            t[j] = t[j+1]
        t = t[0:len(t)-2*n-m]
        print(n,m)
        print(s,t)

        if s == t:
            return True
        else:
            return False

s = "a##c"
t = "#a#c"
a = Solution()
x = a.backspaceCompare(s,t)
print(x)