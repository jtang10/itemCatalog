from flask import Flask, render_template, request, redirect, jsonify, url_for
from sqlalchemy import create_engine, desc
from sqlalchemy.orm import sessionmaker
from database_setup import Base, Category, Item

app = Flask(__name__)

engine = create_engine('postgresql:///itemcatalog')
Base.metadata.bind = engine

DBSession = sessionmaker(bind = engine)
session = DBSession()


@app.route('/category/<int:category_id>/items/JSON')
def categoryCatalogJSON(category_id):
    category = session.query(Category).filter_by(id = category_id).one()
    items = session.query(Item).filter_by(category_id = category_id).all()
    return jsonify(Catalog = [i.serialize for i in items])

@app.route('/category/<int:category_id>/items/<int:item_id>/JSON')
def ItemJSON(category_id, item_id):
    Item = session.query(Item).filter_by(id = item_id).one()
    return jsonify(Item = Item.serialize)

@app.route('/category/JSON')
def categoriesJSON():
    categories = session.query(Category).all()
    return jsonify(categories = [c.serialize for c in categories])


# Front page. Show all categories
@app.route('/')
@app.route('/category/')
def showCategories():
    categories = session.query(Category).all()
    latestItems = session.query(Item).order_by(desc(Item.modified)).limit(10).all()
    return render_template('categories.html', categories = categories, latestItems = latestItems)


# Add a new category
@app.route('/category/new/', methods = ['GET', 'POST'])
def newCategory():
    if request.method == 'POST':
        newCategory = Category(name = request.form['name'])
        session.add(newCategory)
        session.commit()
        return redirect(url_for('showCategories'))
    else:
        return render_template('newCategory.html')


# Edit a category
@app.route('/category/<int:category_id>/edit/', methods=['GET', 'POST'])
def editCategory(category_id):
    editedCategory = session.query(
        Category).filter_by(id = category_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedCategory.name = request.form['name']
            session.add(editedCategory)
            session.commit()
            return redirect(url_for('showCategories'))
    else:
        return render_template('editCategory.html',
                               category = editedCategory)


# Delete a category
@app.route('/category/<int:category_id>/delete/', methods=['GET', 'POST'])
def deleteCategory(category_id):
    categoryToDelete = session.query(
        Category).filter_by(id=category_id).one()
    if request.method == 'POST':
        session.delete(categoryToDelete)
        session.commit()
        return redirect(url_for('showCategories', category_id = category_id))
    else:
        return render_template('deleteCategory.html',
                               category = categoryToDelete)


# Show a category's all items
@app.route('/category/<int:category_id>/')
@app.route('/category/<int:category_id>/items/')
def showItems(category_id):
    category = session.query(Category).filter_by(id = category_id).one()
    items = session.query(Item).filter_by(category_id = category_id).all()
    return render_template('items.html', items = items, category = category)

# Show one item
@app.route('/category/<int:category_id>/items/<int:item_id>')
def showOneItem(category_id, item_id):
    item = session.query(Item).filter_by(id = item_id).one()
    return render_template('oneitem.html', item = item)

# Create a new item
@app.route('/category/<int:category_id>/items/new/',
           methods = ['GET', 'POST'])
def newItem(category_id):
    if request.method == 'POST':
        newItem = Item(name = request.form['name'],
                       description = request.form['description'],
                       category_id = category_id)
        session.add(newItem)
        session.commit()

        return redirect(url_for('showItems', category_id = category_id))
    else:
        return render_template('newItem.html', category_id = category_id)

    return render_template('newItem.html', category = category)


# Edit an item
@app.route('/category/<int:category_id>/items/<int:item_id>/edit',
           methods=['GET', 'POST'])
def editItem(category_id, item_id):
    editedItem = session.query(Item).filter_by(id = item_id).one()
    if request.method == 'POST':
        if request.form['name']:
            editedItem.name = request.form['name']
        if request.form['description']:
            editedItem.description = request.form['description']
            session.add(editedItem)
            session.commit()
        return redirect(url_for('showItems', category_id = category_id))
    else:

        return render_template('editItem.html',
                               category_id = category_id,
                               item_id = item_id,
                               item = editedItem)


# Delete an item
@app.route('/category/<int:category_id>/items/<int:item_id>/delete',
           methods=['GET', 'POST'])
def deleteItem(category_id, item_id):
    itemToDelete = session.query(Item).filter_by(id = item_id).one()
    if request.method == 'POST':
        session.delete(itemToDelete)
        session.commit()
        return redirect(url_for('showItems', category_id = category_id))
    else:
        return render_template('deleteItem.html', item = itemToDelete)


if __name__ == '__main__':
    app.debug = True
    app.run(host = '0.0.0.0', port = 5000)
