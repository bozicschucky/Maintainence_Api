from flask_restful import Resource, reqparse
from flask_jwt import jwt_required
import sqlite3
from models.item import ItemModel

class Item(Resource):
    TABLE_NAME = 'items'

    parser = reqparse.RequestParser()
    parser.add_argument('id',
        type=int,
        required=True,
        help="This field cannot be left blank!"
    )

    @jwt_required()
    def get(self, name):
        # item = self.find_by_name(name)
        item = ItemModel.find_by_name(name)
        if item:
            return item.json()
        return {'message': 'Item not found'}, 404



    def post(self, name):
        if ItemModel.find_by_name(name):
            return {'message': "An item with name '{}' already exists.".format(name)}

        data = Item.parser.parse_args()

        item = ItemModel(name,data['id'])

        try:
            #ItemModel.insert(item)
            item.insert()
        except:
            return {"message": "An error occurred inserting the item."}

        return item


    @jwt_required()
    def put(self, name):
        data = Item.parser.parse_args()
        item = self.find_by_name(name)
        updated_item = ItemModel(name,data['id'])
        if item is None:
            try:
                updated_item.insert()
                # ItemModel.insert(updated_item)
            except:
                return {"message": "An error occurred inserting the item."}
        else:
            try:
                updated_item.update()
                # ItemModel.update(updated_item)
            except:
                # raise
                return {"message": "An error occurred updating the item."}
        return updated_item.json()

    @jwt_required()
    def delete(self, name):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "DELETE FROM {table} WHERE name=?".format(table=self.TABLE_NAME)
        cursor.execute(query, (name,))

        connection.commit()
        connection.close()

        return {'message': 'Item deleted'}




class Requests(Resource):
    TABLE_NAME = 'requests'

    def get(self):
        connection = sqlite3.connect('data.db')
        cursor = connection.cursor()

        query = "SELECT * FROM {table}".format(table=self.TABLE_NAME)
        result = cursor.execute(query)
        items = []
        for row in result:
            items.append({'request_name': row[0], 'id': row[1]})
        connection.close()

        return {'items': items}
