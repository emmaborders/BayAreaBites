from werkzeug.security import generate_password_hash, check_password_hash
from flask import *
from database import init_db, db_session
from models import *

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///mydatabase.db'
app.secret_key = 'secret'


@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['POST'])
def login():
    username = request.form['username']
    password = request.form['password']
    user = db_session.query(User).where(User.username == username).first()
    if user:
        session['user'] = user.id
        return redirect('/restaurants')
    else:
        return redirect('/')

@app.route('/signup', methods=['POST'])
def signup():
    username = request.form['username']
    password = request.form['password']
    
    user_exists = db_session.query(User).filter_by(username=username).first()
    if user_exists:
        return redirect('/')
    
    new_user = User(username=username, password=password)
    
    db_session.add(new_user)
    db_session.commit()
    
    return redirect('/restaurants')


@app.route('/favorites')
def favorites():
    res = db_session.query(Restaurant).all()
    print(res[0].address)
    user = db_session.query(User).where(User.id == session["user"]).first()
    return render_template('favorites.html', restaurants=res, favorites=user.favorties)


@app.route('/restaurants', methods=["GET", "POST"])
def restaurants():
    res = db_session.query(Restaurant).all()
    print(res[0].address)
    user = db_session.query(User).where(User.id == session["user"]).first()

    return render_template('restaurants.html', restaurants=res, favorites=user.favorties)


@app.route('/fav/<id>')
def fav(id):
    print(id)
    print(session["user"])

    existing_favorite = db_session.query(Favorite).filter_by(user_id=session["user"], restaurant_id=id).first()
    
    if existing_favorite:
        db_session.delete(existing_favorite)
        db_session.commit()
        return redirect('/restaurants')
    else:
        new_favorite = Favorite(user_id=session["user"], restaurant_id=id)
        db_session.add(new_favorite)
        db_session.commit()
        return redirect('/restaurants')

    

if __name__ == '__main__':
    init_db()
    app.run(debug=True)


