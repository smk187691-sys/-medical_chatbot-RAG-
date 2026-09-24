from flask import Flask, render_template,request,redirect,url_for
from app.componenets.retriver import create_qa_chain
from app.componenets.history import(create_table,save_chat,get_history,delet_chat,clear_history)

from dotenv import load_dotenv
from markupsafe import Markup
import os

load_dotenv()
app= Flask(__name__)
app.secret_key = os.urandom(24)

create_table()
#filter tags

def br_tag(value):
    return Markup(value.replace("\n","<br>\n"))

app.jinja_env.filters["br_tag"]= br_tag


@app.route("/", methods=['GET','POST'])

def index():
    if request.method == 'POST':
        user_input = request.form.get("prompts")
        if user_input:
            try:
                qa_chain= create_qa_chain()
                if qa_chain is None:
                    raise Exception("QA CHAIN COULD NOT BE CREATED.")
                response = qa_chain.invoke({"query":user_input})
                result = response.get("result","no result")
                save_chat(user_input,result)

            except Exception as e:
                history = get_history()
                return render_template("index.html",messages=[],history=history,error=str(e))
        return redirect(url_for("index"))


    history = get_history()
    messages =[]

    for chat_id, question,answer,chat_time in history:
        messages.append({"id": chat_id,"role":"user","content":question,"time":chat_time})
        messages.append({"id":chat_id,"role":"assistant", "content":answer, "time": chat_time})

    return render_template("index.html",messages = messages,history=history)


@app.route("/delete/chat/<int:chat_id>")

def delete(chat_id):
    delet_chat(chat_id)
    return redirect(url_for("index"))

@app.route("/clear")
def clear():
    clear_history()
    return redirect(url_for("index"))


if __name__ == "__main__" :
    app.run(host="0.0.0.0",port=5000,debug=False,use_reloader=False)