from flask import render_template, flash, Blueprint, url_for, redirect
from flaskwebsite.sarcasm_classifier.forms import TextInputForm
from flaskwebsite.sarcasm_classifier.function import load_model, predict


sarcasm_classifier = Blueprint("sarcasm_classifier", __name__)


@sarcasm_classifier.route("/sarcasm", methods=['GET', 'POST'])
def sarcasm():
    form = TextInputForm()
    if form.validate_on_submit():
        text = form.text.data
        learn = load_model()
        result = predict(text, learn)
        if result == 0:
            flash("This is not sarcastic", "success")
        elif result == 1:
            flash("This is sarcastic", "danger")
        else:
            flash("An error has occurred. Please try again")
        return redirect(url_for('sarcasm_classifier.sarcasm'))
    return render_template("sarcasm.html", title="Sarcasm Detection", form=form)

