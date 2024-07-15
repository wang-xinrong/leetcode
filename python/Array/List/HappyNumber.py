class Solution:
    def isHappy(self, n: int) -> bool:
        curr = n
        for i in range(50):
            sum = 0
            while curr > 0:
                sum+=(curr%10) ** 2
                curr = curr // 10
            if sum == 1:
                return True
            curr = sum
        return False

    def isHappyUseTorquoiseAndHare(self, n: int) -> bool:
	#20 -> 4 -> 16 -> 37 -> 58 -> 89 -> 145 > 42 -> 20
        slow = self.squared(n)
        fast = self.squared(self.squared(n))

        while slow!=fast and fast!=1:
            slow = self.squared(slow)
            fast = self.squared(self.squared(fast))

        return fast==1

    def squared(self, n):
        result = 0
        while n>0:
            last = n%10
            result += last * last
            n = n//10
        return result

    def isHappyUseSet(self, n: int) -> bool:
        myset = set()
        result = n
        while result not in myset:
            if result == 1:
                return True
            myset.add(result)
            n = result
            result = 0
            while n > 0:
                last = n%10
                result += last * last
                n = n//10
        return False
