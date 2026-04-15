from flask import Flask,render_template,request

app = Flask (__name__) 

@app.route("/")
#rota vazia
#definir função 
def home():
    return render_template("index.html")
#vai acessar o index    

@app.route("/login" , methods=["POST"])
# @app.route("/***") padrão
def login():

    user = request.form.get("user")
    password = request.form.get("password")

    if user == "MariaE" and password == "1234":
        return "Acesso liberado"
    else:
        return "Acesso Negado"
    # == comparação

if __name__ == "__main__":
    app.run("0.0.0.0", port=8000)