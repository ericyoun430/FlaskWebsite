from website import create_app

app = create_app()

if __name__ == '__main__':
    #debug = True reruns the web server when we change the code
    app.run(debug=True)
    