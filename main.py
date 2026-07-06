import re

def is_valid_commit(message):
    pattern = r"^(feat|refactor|chore|docs|fix|style|test)(\(.+\))?: .{1, 100}$"
    return bool(re.match(pattern, message))

if __name__ == "__main__":
    print(is_valid_commit("fixed stuff"))
    print(is_valid_commit("fix: correct regex"))
    
