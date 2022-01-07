from faker import Faker

from app import app, db
from app.models import Person, PhoneNumber
from app.forms import AddForm
from flask import redirect, render_template


# @app.route('/')
# def index():
# 	books = Book.query.all()
# 	return render_template('index.html', books=books)


# @app.route('/add', methods=['GET', 'POST'])
# def addbook():
# 	form = AddForm()
#
# 	if form.validate_on_submit():
# 		title = form.title.data
# 		author_name = form.author.data
# 		price = form.price.data
#
# 		get_all_authors_name_from_db = [aut.name.lower() for aut in Author.query.all()]
#
# 		if author_name.lower() not in get_all_authors_name_from_db:
# 			# creating new author
# 			author = Author(name=author_name)
# 			db.session.add(author)
# 		else:
# 			# get existing author from db
# 			author = Author.query.filter_by(name=author_name).first()
#
# 		newbook = Book(title=title, author=author, price=price)
# 		db.session.add(newbook)
# 		db.session.commit()
# 		return redirect('/')
# 	return render_template('addbook.html', form=form)


@app.route('/<id>')
def index(id):
	persons = Person.query.all()
	return render_template('index.html', person_id=id)


@app.route('/add_fake_person', methods=['GET', 'POST'])
def add_person():
	faker = Faker()
	name = faker.first_name()
	email = faker.email()
	address = faker.address()
	phone_number1 = faker.phone_number()
	phone_number2 = faker.phone_number()

	person = Person(name=name, email=email, address=address)
	phone_number_1 = PhoneNumber(number=phone_number1, person=person)
	phone_number_2 = PhoneNumber(number=phone_number2, person=person)

	db.session.add(person)
	db.session.add(phone_number_1)
	db.session.add(phone_number_2)

	db.session.commit()

	return f"new person {name} added to the db with phone numbers {phone_number1}, {phone_number_2}"


@app.route('/get_person/<int:id>')
def get_person(id):
	p = Person.query.filter_by(person_id=id).first()

	return f"{p.name}<br>{p.email}<br>{p.address}"


@app.route('/delete_person/<int:id>', methods=['GET', 'POST'])
def delete_person(id):
	p = Person.query.filter_by(person_id=id).first()
	db.session.delete(p)
	db.session.commit()

	return f"the person with id {id} deleted successfully"
