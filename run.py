from application import application_run

app = application_run()
app.app_context().push()

if __name__ == '__main__':
    app.run(debug=True, port=8031)