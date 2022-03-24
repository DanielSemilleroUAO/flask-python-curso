from webpersonal import db


class Project(db.Model):
    __tablename__ = 'projects'
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(100))
    description = db.Column(db.Text)

    def __init__(self, title, description):
        self.title = title
        self.description = description

    def __repr__(self):
        return f'Project: {self.title}'

# p1 = Project('Proyecto 01', 'Descripcion de proyecto 01')
# p2 = Project('Proyecto 02', 'Descripcion de proyecto 02')
# p3 = Project('Proyecto 03', 'Descripcion de proyecto 03')

# PROYECTS = [p1, p2, p3]
