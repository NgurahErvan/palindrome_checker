from flask import Flask, render_template, request

app = Flask(__name__)


def is_palindrome_basic(s):
    return s == s[::-1]


def is_palindrome_clean(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    return cleaned == cleaned[::-1], cleaned


def is_palindrome_iterative(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())
    left, right = 0, len(cleaned) - 1
    while left < right:
        if cleaned[left] != cleaned[right]:
            return False
        left += 1
        right -= 1
    return True


def is_palindrome_recursive(s):
    cleaned = ''.join(char.lower() for char in s if char.isalnum())

    def check_recursive(text, start, end):
        if start >= end:
            return True
        if text[start] != text[end]:
            return False
        return check_recursive(text, start + 1, end - 1)
    return check_recursive(cleaned, 0, len(cleaned) - 1)


def is_palindrome_automata_case_insensitive(input_str):
    input_str = ''.join(char.lower() for char in input_str if char.isalnum())
    stack = []
    state = "PUSH"
    i = 0
    n = len(input_str)
    while i < n:
        if state == "PUSH":
            if n % 2 == 1 and i == n // 2:
                state = "POP"
                i += 1
                continue
            elif i == n // 2:
                state = "POP"
                continue
            else:
                stack.append(input_str[i])
                i += 1
        elif state == "POP":
            if not stack:
                return False
            top = stack.pop()
            if top != input_str[i]:
                return False
            i += 1
    return True


@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        user_input = request.form["textInput"]
        basic = is_palindrome_basic(user_input)
        clean, cleaned_text = is_palindrome_clean(user_input)
        iterative = is_palindrome_iterative(user_input)
        recursive = is_palindrome_recursive(user_input)
        automata = is_palindrome_automata_case_insensitive(user_input)
        result = {
            "original": user_input,
            "cleaned": cleaned_text,
            "basic": basic,
            "clean": clean,
            "iterative": iterative,
            "recursive": recursive,
            "automata": automata
        }
    return render_template("index.html", result=result)


if __name__ == "__main__":
    app.run(debug=True)
