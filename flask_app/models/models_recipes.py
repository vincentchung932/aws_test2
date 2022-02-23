from flask_app.config.mysqlconnection import connectToMySQL
# model the class after the friend table from our database
import re
from flask import flash

Database = 'recipes_db'
class Recipes:
    def __init__( self , data ):
        self.id = data['id']
        self.name = data['name']
        self.description = data['description']
        self.instructions = data['instructions']
        self.date_made = data['date_made']
        self.time = data['time']
        self.created_at = data['created_at']
        self.updated_at = data['updated_at']
        self.recipes=[]
    
    
    
    @classmethod
    def add(cls,data):
        query = "INSERT INTO recipes (name,description,instructions,date_made,time,user_id) VALUES ( %(name)s,%(description)s,%(instructions)s,%(date_made)s,%(time)s,%(user_id)s);"    
        return connectToMySQL(Database).query_db(query,data)
    
    @classmethod
    def delete(cls,data):
        query = "DELETE FROM recipes WHERE id=%(id)s;"    
        return connectToMySQL(Database).query_db(query,data)
    
    @classmethod
    def get_one(cls,data):
        query = "SELECT * FROM recipes WHERE id = %(id)s;"
        results = connectToMySQL(Database).query_db(query,data)
        if results:
            return cls(results[0])
        else:
            return []
        
    @classmethod
    def update(cls,data):
        query = "UPDATE recipes SET name=%(name)s,description=%(description)s, instructions=%(instructions)s,date_made=%(date_made)s,time=%(time)s WHERE id = %(id)s;"    
        return connectToMySQL(Database).query_db(query,data)