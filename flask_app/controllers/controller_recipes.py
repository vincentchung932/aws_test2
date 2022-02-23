from flask import  render_template, request, redirect, session, flash
from flask_app.models.models_users import Users
from flask_app.models.models_recipes import Recipes

from flask_app import app

@app.route('/recipes/new')
def create_recipe():
    if 'id' not in session:
        return redirect('/')
    
    return render_template('recipe_new.html')


@app.route('/recipes/creating', methods=['post'])
def creating_recipe():
    print(request.form)
    data = {
        **request.form,
        'user_id' : session['id']
    }
    Recipes.add(data)
    return redirect('/dashboard')



@app.route('/recipes/<int:id>')
def view_recipe(id):
    if 'id' not in session:
        return redirect('/')
    recipe = Recipes.get_one({'id':id})
    user = Users.get_one( {'id':session['id']} )

    return render_template('recipe_show.html',recipe=recipe,user = user)


@app.route('/recipes/delete//<int:id>')
def delete_recipe(id):
    Recipes.delete({'id':id})
    return redirect('/dashboard')

@app.route('/recipes/edit/<int:id>')
def edit_recipe(id):
    if 'id' not in session:
        return redirect('/')   
    recipe = Recipes.get_one({'id':id})
    return render_template('recipe_edit.html',recipe=recipe)

@app.route('/recipes/editing/<int:id>',methods=['post'])
def editing_recipe(id):
    data = {
        **request.form,
        'id' : id
    }
    Recipes.update(data)
    return redirect('/dashboard')