from sqlalchemy import func
from sqlalchemy.ext.automap import automap_base
from flask import (
    Flask,
    render_template,
    jsonify,
    request,
    redirect)
import pandas as pd
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import create_engine

app = Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///db/customer_reviews.sqlite"
engine = create_engine("sqlite:///db/customer_reviews.sqlite")
db = SQLAlchemy(app)
Base = automap_base()
Base.prepare(engine, reflect=True)
Reviews=Base.classes.reviews
Bigram=Base.classes.bigram

@app.route("/")
def home():
#     """Render Home Page."""
    return render_template("index.html")

@app.route("/table")
def table():
#    
    return render_template("table.html")

@app.route("/api")
def rating():
    results = db.session.query(Reviews.Rating, func.count(Reviews.Rating)).group_by(Reviews.Rating).all()
    
    Rating = [result[0] for result in results]
    Count= [result[1] for result in results]

    trace = {
      "x": Rating,
      "y": Count,
      "type": "bar"
    }

    return jsonify(trace)


@app.route("/api2")
def Province():
    queries = db.session.query(Reviews.Province, func.count(Reviews.Province)).group_by(Reviews.Province).all()
    
    Province = [query[0] for query in queries][:14]
    Values= [query[1] for query in queries][:14]

    plot_trace = {
      "values": Values,
      "labels": Province,
      "type": "pie"
    }

    return jsonify(plot_trace)

@app.route("/api3")
def grams():
    bigrams = db.session.query(Bigram.Bigram, Bigram.Freq).all()
    
    Bigrams = [bigram[0] for bigram in bigrams]
    Frequency= [bigram[1] for bigram in bigrams]

    trace = {
      "x": Bigrams,
      "y": Frequency,
      "type": "scatter"
    }

    return jsonify(trace)

@app.route("/api4")
def all_reviews():
    
   
    results = db.session.query(Reviews.Name, Reviews.Rating, Reviews.Date_Reviewed,Reviews.Review).all()

    all_reviews = []
    for Name, Rating, Date_Reviewed,Review in results:
        reviews_dict = {}
        reviews_dict["Name"] = Name
        reviews_dict["Rating"] = Rating
        reviews_dict["Date Reviewed"] = Date_Reviewed
        reviews_dict["Review"] = Review
        all_reviews.append(reviews_dict)

    return jsonify(all_reviews)





if __name__ == '__main__':
        app.run(debug=True)


