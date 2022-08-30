from main.database import db

ACCESS = {
    'guest': 0,
    'user': 1,
    'admin': 2
}


class UserModel(db.Model):
    __tablename__ = 'users'

    id = db.Column(db.Integer, autoincrement=True, primary_key=True)
    username = db.Column(db.String(80), nullable=False)
    email = db.Column(db.String(120), index=True, unique=True, nullable=False)
    password = db.Column(db.String(128), nullable=False)
    access = db.Column(db.Integer)

    # dans le skeleton pas de constructeur, bizarre ?
    def __init__(self, username, password, email, access=ACCESS['guest']):
        self.username = username
        # TODO: ici il faudrait appliquer un hash sur le password
        self.password = password
        self.email = email
        self.access = access

    def __repr__(self):
        return '<User {}>'.format(self.username)

    def to_json(self):
        return {
            'id': self.id,
            'username': self.username,
            'mail': self.email,
            'password': '*********',
            'access': self.access
        }

    @classmethod
    def find_all(cls):
        return cls.query.all()

    @classmethod
    def find_by_id(cls, _id):
        return cls.query.filter_by(id=_id).first()

    @classmethod
    def find_by_username(cls, username):
        return cls.query.filter_by(username=username).first()

    @classmethod
    def find_by_email(cls, email):
        return cls.query.filter_by(email=email).first()

    def is_admin(self):
        if self.access == ACCESS['admin']:
            return True
        return False

    def is_guest(self):
        if self.access == ACCESS['guest']:
            return True
        return False
