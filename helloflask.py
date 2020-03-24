from flask import Flask, request, render_template


app = Flask(__name__)


@app.route("/index")
@app.route("/")
def hello_flask():
    return "Hello World"

@app.route("/new/")
def query_strings(greetings="hello"):
    query_val=request.args.get("greetings", greetings)
    return '<h1> the greeting is: {0}'.format(query_val)

@app.route("/user")
@app.route("/user/<name>")
def no_query_strings(name="German"):
    return '<h1> the greeting is: {0}'.format(name)


@app.route("/watch")
def top_movies():
    movie_list=['Lion King',
                'John Wick 2',
                'Spiderman',
                "Once upon a time in America"
                ]

    return render_template('movies.html', movies=movie_list, name="German Villalpando Novelo")


@app.route("/tables")
def movies_plus():
    movie_dic={'Lion King':02.14,
                'John Wick 2': 3.20,
                'Spiderman': 1.50,
                "Once upon a time in America" : 1.40
               }

    return render_template('table_data.html', movies=movie_dic, name="German Villalpando Novelo")



if __name__ == "__main__":
    app.run(debug=True)