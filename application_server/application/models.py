import application


class Product(application.db.Model):
    __tablename__ = 'product'

    id = application.db.Column(application.db.Integer, primary_key=True)
    name = application.db.Column(application.db.String(255), nullable=False)
    price = application.db.Column(application.db.Integer, nullable=False)
    url = application.db.Column(application.db.String(255), nullable=False)

    def __repr__(self):
        return '<Entry id={id} name={title!r} price={price}>'.format(
            id=self.id, title=self.name, price=self.price)


def init():
    application.db.create_all()
