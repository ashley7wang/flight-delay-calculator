""" Specifies routing for the application"""
from flask import render_template, request, jsonify, redirect, url_for
from flask_wtf import FlaskForm
from wtforms import StringField,SubmitField
from wtforms.validators import DataRequired

from app import app
from app import database as db_helper

@app.route('/')
def main():
    form = SearchForm()
    return render_template("index.html", form=form)

@app.route('/search', methods=["POST"])
def search():
    form = SearchForm()
    if form.validate_on_submit():
        searched = form.searched.data
        rec = db_helper.searchdb(searched)
        return render_template("search.html", form=form, searched = searched, rec = rec)
    pass

@app.route('/add_review', methods=["GET", "POST"])
def add_review():
    form = AddReview()
    if form.validate_on_submit():
        airline = form.airline.data
        review = form.review.data
        id = db_helper.add_reviewdb(review, airline)  # Add the review to the database
        return render_template("add-review.html", form=form, airline=airline, review=review, id=id)  # Redirect to the main page after adding a review
    return render_template("add-review.html", form=form)

@app.route('/delete_review', methods=["GET", "POST"])
def delete_review():
    form = DeleteReview()
    if form.validate_on_submit():
        review_num = form.review_num.data
        db_helper.delete_reviewdb(review_num)  # Delete the review from the database
        return render_template("delete-review.html", form=form, review_num=review_num)  # Redirect to the main page after deleting a review
    return render_template("delete-review.html", form=form)


@app.route('/update_review', methods=["GET", "POST"])
def update_review():
    form = UpdateReview()
    if form.validate_on_submit():
        review_num = form.review_num.data
        review = form.review.data
        db_helper.update_reviewdb(review_num, review)  # Update the review in the database
        return render_template("update-review.html", form=form, review_num=review_num, text=review)  # Redirect to the main page after updating a review
    return render_template("update-review.html", form=form)



@app.route('/delay_calculator', methods=["GET", "POST"])
def delay_calculator():
    form = DelayCalculator()
    if form.validate_on_submit():
        origin = form.origin.data
        destination = form.destination.data
        best_airline, avg_delay = db_helper.get_best_airline_with_least_delay(origin, destination)
        
        return render_template("delay-calculator.html", form=form, origin=origin, destination=destination, best_airline=best_airline, avg_delay=avg_delay)
    return render_template("delay-calculator.html", form=form)





class SearchForm(FlaskForm):
    searched = StringField("Searched", validators=[DataRequired()])
    submit = SubmitField("Submit")


class AddReview(FlaskForm):
    airline = StringField("Airline", validators=[DataRequired()])
    review = StringField("Review", validators=[DataRequired()])
    submit = SubmitField("Submit")

class RecommendationForm(FlaskForm):
    origin = StringField("Origin Airport", validators=[DataRequired()])
    destination = StringField("Destination Airport", validators=[DataRequired()])
    submit = SubmitField("Submit")

class DeleteReview(FlaskForm):
    review_num = StringField("Review #", validators=[DataRequired()])
    submit = SubmitField("Submit")

class UpdateReview(FlaskForm):
    review_num = StringField("Review #", validators=[DataRequired()])
    review = StringField("Review", validators=[DataRequired()])
    submit = SubmitField("Submit")

class DelayCalculator(FlaskForm):
    origin = StringField("Origin", validators=[DataRequired()])
    destination = StringField("Destination", validators=[DataRequired()])
    submit = SubmitField("Submit")
