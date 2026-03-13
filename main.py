# (12,3):+/-/*
def solution(s: str) -> int:
    nums = [int(i) for i in find_nums(s).split(",")]
    sign = s.split(":")[1]
    if sign == "*" : return nums[0] * nums[1]
    elif sign == "+": return nums[0] + nums[1]
    elif sign == "-": return nums[0] - nums[1]



def find_nums(s: str) -> str:
    answer = ""
    status = False
    for i in range(len(s)):
        if not status and s[i] == "(": check = True
        elif status and s[i] == ")": return answer
        elif status: answer += s[i]