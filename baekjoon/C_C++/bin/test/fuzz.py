#!/usr/bin/env python

import subprocess
import random
from time import sleep

testcase = "./testcase.txt"
process_1 = "./baek_1343"
process_2 = "./baek_1343_other"


def check_testcase(testcase_str):
    with open(testcase, "w") as f:
        f.write(testcase_str)

    with open(testcase, "r") as f:
        res1 = subprocess.run(process_1, stdin=f, shell=True, capture_output=True, text=True)
        print(res1.stdout, end="")

    with open(testcase, "r") as f:
        res2 = subprocess.run(process_2, stdin=f, shell=True, capture_output=True, text=True)
        print(res2.stdout, end="")

    return res1, res2

if __name__=="__main__":
    string = ""
    for i in range(1, 51):
        string = "." * i
        print(string)
        res1, res2 = check_testcase(string)
        if (res1.stdout != res2.stdout):
            print("RESULT IS NOT SAME")
        print()

    sleep(0.2)

    for i in range(1, 51):
        string = "X" * i
        print(string)
        res1, res2 = check_testcase(string)
        if (res1.stdout != res2.stdout):
            print("RESULT IS NOT SAME")
        print()

    sleep(0.2)

    while True:
        string = ""
        str_num = random.randint(1, 51)

        for i in range(str_num):
            string += random.choice(["XX", ".", "X", "XX", "XX"])

        if (len(string) >= 50):
            continue

        print(string)
        res1, res2 = check_testcase(string)

        if (res1.stdout != res2.stdout):
            print("RESULT IS NOT SAME")
            break
        print()
        sleep(0.1)
