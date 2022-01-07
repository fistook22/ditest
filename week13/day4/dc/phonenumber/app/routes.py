from faker import Faker
from flask import render_template
from app.forms import AddForm
from app import app, db
from app.models import Person, PhoneNumber


@app.route('/')
def index():
    persons = Person.query.all()
    return render_template('index.html', person='person')


@app.route('/add_fake_person', methods=['GET', 'POST'])
def add_fake_person():
    faker = Faker()
    name = faker.first_name()
    address = faker.address()
    email = faker.email()
    phone_number_1 = faker.phone_number()
    phone_number_2 = faker.phone_number()

    person = Person(name=name, email=email, address=address)
    phone_number_1 = PhoneNumber(number=phone_number_1, person=person)
    phone_number_2 = PhoneNumber(number=phone_number_2, person=person)

    db.session.add(person)
    db.session.add(phone_number_1)
    db.session.add(phone_number_2)

    db.session.commit()

    @app.route('/get_person/<id>', methods=['GET', 'POST'])
    def get_person(person_id):
        person.query.filter_by(person_id=person_id).first()

        return f"{person.name}<br>>{person.email}<br>>{person.address}"

    @app.route('/delete_person/<int:id>', methods=['GET', 'POST'])
    def delete_person(id):
        p = Person.query.filter_by(person_id=id).first()
        db.session.delete(p)
        db.session.commit()

        return f"the person with id {id} deleted successfully"
