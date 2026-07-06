#!/usr/bin/env python

import re
import sys

def main():
    commit_msg_file = sys.argv[1]
    with open(commit_msg_file, 'r') as f:
        message= f.readline().strip()
    
    if not is_valid_commit(message):
        print("The commit message doesn't follow conventional commit message format!")
        print("eg. 'feat: implement commit message validator using regex'")
        sys.exit(1)
    sys.exit(0)

def is_valid_commit(message):
    pattern = r"^(feat|refactor|chore|docs|fix|style|test)(\(.+\))?: .{1,100}$"
    return bool(re.match(pattern, message))

if __name__ == "__main__":
    main()

    # print(is_valid_commit("fixed stuff"))
    # print(is_valid_commit("fix: correct regex"))
    
