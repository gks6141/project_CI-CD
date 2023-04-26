from flask import Flask, render_template
import requets

app = Flask(__name__)

@app.route("/")
def index():
    services = [
        {"name": "Web Service" , "url" : "https://www.example.com"},
        {"name": "Database Service", "url" : "https://db.example.com"},
        {"name": "Email Serviece" , "url" : "https://email.example.com"}
    ]
    status_list = []
    for service in services:
        try:
            response = requests.get(service["url"])
            if response.status_code == 200:
                status_list.append({"name":service["name"], "status": "OK"})
            else :
                status_list.append({"name":service["name"],"status":"Error"})
        except:
            status_list.append({"name":service["name"],"status":"Error"})
    return render_template("index.html", service=stauts_list)

if __name__ == "__main__":
    app.run(debug=True)