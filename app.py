import sys
import os


def prime(s):
    # your code goes here
    s = int(input("Please input a number"))
    if s > 1:
        for i in range(2,s):
            if(s % i) == 0:
                print('%d is not prime'%(s))
                break
        else:
            print('%d is prime'%(s))  
    else:
        print('%d is not prime'%(s))

def solution(s):
    return prime(s)


if __name__ == "__main__":
    if len(sys.argv) <= 1:
        sys.exit(os.error("Argument required"))

    print(solution(sys.argv[1]))
