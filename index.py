from flask import Flask, request, render_template_string
import pyautogui

app = Flask(__name__)

# HTML template for the web page
html_template = '''
<!DOCTYPE html>
<html lang="en">

<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>Document</title>
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Inter:ital,opsz,wght@0,14..32,100..900;1,14..32,100..900&display=swap');

        :root {
            --allBlack: #000;
            --allBlack2: #0A0A0A;
            --allBlack3: #1a1a1a;
            --border-color: #2D2D2D;
            --cblack: #101010;
            --grey1: #3a3a3a;
            --grey2: #242424;
            --green: #008a2e;
            --font-fallback: -apple-system, BlinkMacSystemFont, 'Segoe UI', Helvetica, Arial,
                sans-serif, 'Apple Color Emoji', 'Segoe UI Emoji', 'Segoe UI Symbol', system-ui;
            --font-inter: "Inter", var(--font-fallback);
        }

        body {
            background-color: var(--allBlack2);
            color: #EDEDED;
            font-family: var(--font-inter);
            display: flex;
            justify-content: center;
            align-items: center;
            height: 100vh;
            width: 100vw;
            margin: 0;
        }

        h1 {
            color: #FFFFFF;
            margin: 0 0 20px 0;
            font-weight: 500;
            font-size: 1.5rem;
            line-height: 2rem;
            letter-spacing: -.05em;
        }

        .container {
            width: 50%;
            height: 80%;
        }

        .verticle-wrapper {
            display: flex;
            flex-direction: column;
        }

        .verticle-wrapper::after {
            content: "";
            display: flex;
            width: 1px;
            height: 20px;
        }

        label {
            color: #D4D4D4;
            margin-bottom: 10px;
        }

        form {
            width: 100%;
        }

        .input-field {
            width: 100%;
            background-color: var(--allBlack);
            color: #FFFFFF;
            border: 1px solid var(--border-color);
            border-radius: 6px;
            padding: 10px;
            font-size: 14px;
            box-sizing: border-box;
        }

        .answer-text-area {
            width: 100%;
            min-height: 300px;
            max-height: 500px;
            resize: none !important;
        }

        textarea {
            font-family: var(--font-inter);
        }

        textarea:focus-visible,
        input:focus-visible {
            outline: 1px solid var(--border-color);
        }

        input[type="submit"] {
            background-color: var(--grey2);
            color: #FFFFFF;
            border: none;
            border-radius: 5px;
            padding: 10px 20px;
            font-size: 16px;
            cursor: pointer;
            margin-top: 10px;
            transition: all .3s ease-in-out;
            /* Corrected duration */
        }

        input[type="submit"]:hover {
            background-color: var(--grey1);
        }

        .alert {
            display: none;
            position: absolute;
            top: 5vh;
            left: 5vh;
            padding: 10px;
            margin-top: 10px;
            border-radius: 5px;
            text-align: center;
        }

        .alert-success {
            background-color: #007f7a;
            color: #000000;
        }

        .alert-error {
            background-color: #e02518;
            color: #FFFFFF;
        }

        @media screen and (max-width: 800px) {
            .container {
                width: 90%;
                height: 80%;
            }
        }
    </style>
    <script>
        function showAlert(message, isSuccess) {
            var alertBox = document.getElementById('alert');
            alertBox.innerHTML = message;
            if (isSuccess) {
                alertBox.className = 'alert alert-success';
            } else {
                alertBox.className = 'alert alert-error';
            }
            alertBox.style.display = 'block';
            setTimeout(function () {
                alertBox.style.display = 'none';
            }, 3000);
        }
    </script>
</head>

<body>
    <div class="container">
        <h1>Send Text to the Device</h1>
        <form action="/" method="post">
            <div class="verticle-wrapper">
                <label for="interval">Enter the interval</label>
                <input class="input-field" id="interval" name="interval" style="margin-bottom: 10px;"
                    value="0.02"></input>
            </div>
            <div class="verticle-wrapper">
                <label for="answertext">Enter the answer</label>
                <textarea class="input-field answer-text-area" id="answertext" name="text"
                    placeholder="Paste the answer here..." autofocus></textarea>
            </div>

            <input type="submit" value="Send">
        </form>
        <div id="alert" class="alert"></div>
    </div>
    {% if success %}
    <script>
        showAlert('Text sent successfully!', true);
    </script>
    {% elif error %}
    <script>
        showAlert('Failed to send text!', false);
    </script>
    {% endif %}
</body>

</html>
'''

@app.route('/', methods=['GET', 'POST'])
def index():
    success = False
    error = False
    if request.method == 'POST':
        try:
            text = request.form['text']
            interval = request.form['interval']
            pyautogui.write(text, interval=interval)
            success = True
        except Exception as e:
            error = True
    return render_template_string(html_template, success=success, error=error)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=9999)