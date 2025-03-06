from flask import Flask, render_template, request

app = Flask(__name__)

def validate_national_id(national_id: str):
    if len(national_id) != 10 or not national_id.isdigit():
        return "❌ کد ملی نامعتبر است!"

    digits = list(map(int, national_id))
    control_digit = digits[-1]
    multipliers = list(range(10, 1, -1))

    total = sum(d * m for d, m in zip(digits[:-1], multipliers))
    remainder = total % 11

    if remainder < 2:
        expected_control_digit = remainder
    else:
        expected_control_digit = 11 - remainder

    if control_digit == expected_control_digit:
        return "✅ کد ملی معتبر است."
    else:
        return "❌ کد ملی نامعتبر است!"

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        national_id = request.form.get("national_id")
        result = validate_national_id(national_id)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
