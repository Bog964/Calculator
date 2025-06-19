from flask import Flask, request, session, render_template_string

app = Flask(__name__)
app.secret_key = 'your_secret_key'

HTML_TEMPLATE = '''


@app.route('/', methods=['GET', 'POST'])
def calculator():
    result = session.get('last_result')
    if request.method == 'POST':
        try:
            num1 = float(request.form['num1'])
            num2 = float(request.form['num2'])
            op = request.form['operation']

            if op == '+':
                result = num1 + num2
            elif op == '-':
                result = num1 - num2
            elif op == '*':
                result = num1 * num2
            elif op == '/':
                result = num1 / num2 if num2 != 0 else 'Ділення на нуль!'
            else:
                result = 'Невідома операція'

            session['last_result'] = result
        except Exception as e:
            result = f'Помилка: {e}'
    return render_template_string(HTML_TEMPLATE, result=result)

if __name__ == '__main__':
    app.run(debug=True)
def on_button_click(button):
    global current_expression

    if button == "C":
        current_expression = ""
        display.delete(0, tk.END)
    elif button == "=":
        try:
            result = str(eval(current_expression))
            display.delete(0, tk.END)
            display.insert(0, result)
            current_expression = result
        except Exception:
            display.delete(0, tk.END)
            display.insert(0, "Помилка")
            current_expression = ""
    else:
        current_expression += str(button)
        display.delete(0, tk.END)
        display.insert(0, current_expression)

root = tk.Tk()
root.title("Калькулятор")
root.geometry("400x600")

display = tk.Entry(root, font=('Arial', 24), justify='right')
display.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

buttons = []
button_texts = [
    '7', '8', '9', '/',
    '4', '5', '6', '*',
    '1', '2', '3', '-',
    'C', '0', '=', '+'
]

row_val = 1
col_val = 0
for text in button_texts:
    button = tk.Button(root, text=text, font=('Arial', 18), width=5, height=2,
                       command=lambda text=text: on_button_click(text))
    button.grid(row=row_val, column=col_val)
    buttons.append(button)
    col_val += 1
    if col_val > 3:
        col_val = 0
        row_val += 1

root.mainloop()
