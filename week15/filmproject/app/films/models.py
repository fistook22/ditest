import datetime

from app import db

films_in_countries = db.Table('filmandcountry',
                              db.Column('film_id', db.Integer, db.ForeignKey('film.film_id')),
                              db.Column('country_id', db.Integer, db.ForeignKey('country.country_id'))
                              )

films_and_categories = db.Table('filmandcategory',
                                db.Column('film_id', db.Integer, db.ForeignKey('film.film_id')),
                                db.Column('category_id', db.Integer, db.ForeignKey('category.category_id'))
                                )

films_and_directors = db.Table('filmanddirector',
                               db.Column('film_id', db.Integer, db.ForeignKey('film.film_id')),
                               db.Column('director_id', db.Integer, db.ForeignKey('director.director_id'))
                               )


class Country(db.Model):
    country_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))
    film_made_in = db.Column(db.Integer, db.ForeignKey('film.film_id'))


class Category(db.Model):
    country_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    name = db.Column(db.String(64))


class Film(db.Model):
    film_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    title = db.column(db.String(64))
    release_date = db.Column(db.Date(64), default=datetime.date.today())
    created_in_countries = db.Column(db.relationship('Country', backref='film', lazy='dynamic'))
    available_in_countries = db.relationship("Country", secondary=films_in_countries)
    category = db.relationship("Category", secondary=films_and_categories)
    director = db.relationship("Director", secondary=films_and_directors)


class Director(db.Model):
    director_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))


class User(db.Model):
    username = db.Column(db.String(64))
    password1 = db.Password()
    password2 = db.Password()
