from flask import Flask, request, jsonify, send_file
from contact_manager import ContactManager

app = Flask(__name__)
obj = ContactManager()

@app.route("/")
def home(): return send_file("index.html")

@app.route("/style.css")
def style(): return send_file("style.css")

@app.route("/contacts")
def contacts(): return jsonify(obj.get_contacts())

@app.route("/add", methods=["POST"])
def add():
    data = request.json
    obj.add_contact(data["name"], data["mobile"], data["mail"])
    return jsonify({"message": "Added"})

@app.route("/update", methods=["POST"])
def update():
    data = request.json
    obj.update_contact(data["old_mobile"], data["new_mobile"])
    return jsonify({"message": "Updated"})

@app.route("/delete", methods=["POST"])
def delete():
    data = request.json
    obj.delete_contact(data["mobile"])
    return jsonify({"message": "Deleted"})

if __name__ == "__main__":
    app.run(debug=True)