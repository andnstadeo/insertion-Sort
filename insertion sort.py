from flask import Flask, render_template, request

app = Flask(__name__)

def perform_insertion_sort(input_list):
    length = len(input_list)

    for i in range(1, length):
        key = input_list[i]
        j = i - 1

        while j >= 0 and key < input_list[j]:
            input_list[j + 1] = input_list[j]
            j -= 1  

        input_list[j + 1] = key

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/sort', methods=['POST'])
def sort():
    user_input = request.form['numbers']
    unsorted_list = [int(x) for x in user_input.split()]

    perform_insertion_sort(unsorted_list)

    return render_template('result.html', unsorted_list=user_input, sorted_list=unsorted_list)

if __name__ == "__main__":
    app.run(debug=True)
