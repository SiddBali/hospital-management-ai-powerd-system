from flask import Flask, render_template

app = Flask(__name__, static_folder='src', static_url_path='/src')

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/doctors')
@app.route('/doctors/<speciality>')
def doctors(speciality=None):
    return render_template('doctors.html', speciality=speciality)

@app.route('/appointment/<doctor_id>')
def appointment(doctor_id):
    return render_template('appointment.html', doctor_id=doctor_id)

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

@app.route('/profile')
def profile():
    return render_template('profile.html')

@app.route('/my-appointments')
def my_appointments():
    return render_template('my_appointments.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/jobs')
def jobs():
    return render_template('jobs.html')

if __name__ == '__main__':
    app.run(debug=True)