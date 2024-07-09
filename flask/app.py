import flask 
from models import *
from sqlalchemy import select
from flask import request
from flask import jsonify
from sqlalchemy.exc import IntegrityError
from flask_cors import CORS,cross_origin

app = flask.Flask(__name__)

app.config["SQLALCHEMY_DATABASE_URI"] = "postgresql://postgres:1234@localhost:5432/flaskdb"
CORS(app)

db.init_app(app)


@app.route("/")
def home():
    return "Hello, world"


@app.route("/product")
def list_products():
    product_list=db.select(Image).order_by(Image.image_id.desc())
    product=db.session.execute(product_list).scalars()
    result=[]
    for item in product:
        details={"product_id":item.product.product_id,
                  "product_name":item.product.product_name,
                  "price":item.product.price,
                  "rating":item.product.rating,
                  "category_id":item.product.category_id,
                  "category_name":item.product.category.category_name,
                  "image":item.image}
        result.append(details)
    return flask.jsonify(result)


@app.route("/products",methods=['POST'])
@cross_origin()
def add_products():
    
    data=request.get_json()

    print(data)
    product_name=data.get('productName')
    price=data.get('price')
    rating=data.get('rating')
    category_name=data.get('categoryName')
    image_url=data.get('image')
    # required_fields = ['product_name', 'price', 'rating', 'category_name', 'image']

    # for field in required_fields:
    #     if field not in data:
    #         return jsonify({'error': f'Missing required field: {field}'}), 400

    # product_name=data.get('product_name')
    # price=data.get('price')
    # rating=data.get('rating')
    # category_name=data.get('category_name')
    # image=data.get('image')
    category = db.session.query(Category).filter_by(category_name = category_name).first()
   
    if category == None :
        category= Category(category_name=category_name)
        db.session.add(category)
        db.session.commit()

    new_product=Product(product_name=product_name,price=price,rating=rating,category_id=category.id)
    db.session.add(new_product)
    db.session.commit()

    new_image=Image(image=image_url,p_id=new_product.product_id)
    db.session.add(new_image)
    db.session.commit()
    return jsonify({'message':"Product added successfully"})
    

@app.route("/category")
def list_category():
    category_list=db.select(Category).order_by(Category.id.desc())
    category = db.session.execute(category_list).scalars()
    result=[]
    for item in category:
        details = {"id":item.id,
                    "category_name":item.category_name
                    }
        result.append(details)
    return flask.jsonify(result)

@app.route("/categories",methods=['POST'])
def add_category():
    data=request.get_json
    id=data.get('id')
    cname=data.get('category_name')
    new_category=Category(id=id,category_name=cname)
    db.session.add(new_category)
    db.session.commit()
    return flask.jsonify("Created")


# @app.route("/image")
# def list_image():
#     return "hy"

with app.app_context():
    db.create_all()

if __name__ == "__main__":
  init_db()
  app.run(port=5000)