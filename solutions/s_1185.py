class Solution:
    def dayOfTheWeek(self, day: int, month: int, year: int) -> str:
        def isLeapYear(year: int):
            return (0 == year%4 and 0 != year%100) or 0 == year%400
        weeks = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
        res = 2
        if year > 1970:
            for i in range(1970, year):
                res += 366 if isLeapYear(i) else 365
        months = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
        for i in range(0, month-1):
            res += months[i]
        if month > 2 and isLeapYear(year):
            res += 1
        res += day
        return weeks[res % 7]

if __name__ == "__main__":
    s = Solution()
    #assert("Thursday" == s.dayOfTheWeek(1, 1, 1970))
    #assert("Thursday" == s.dayOfTheWeek(31, 12, 1970))
    assert("Saturday" == s.dayOfTheWeek(1, 1, 2000))
    assert("Sunday" == s.dayOfTheWeek(18, 7, 1999))
