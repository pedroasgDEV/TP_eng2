from flask import Blueprint, request, jsonify
from app.utils.collections.people import PeopleCollection
from app.utils.connectDB import MongoDB

users_bp = Blueprint('users_bp', __name__)

# Configurar a conexão com o MongoDB
mongo = MongoDB()
mongo.connectDB()
db = mongo.get_database()
col = PeopleCollection(db)

@users_bp.route('/<int:qnt>', methods=['GET'])
def get_random_users(qnt):
    result = col.select_many_random(qnt)
    return jsonify(result), 200

@users_bp.route('/id:<id>', methods=['GET'])
def get_one_user(id):
    result = col.select_one(id)
    return jsonify(result), 200

@users_bp.route('/', methods=['POST'])
def create_item():
    data = request.get_json()
    result = col.insert_document(data)
    return jsonify({'_id': str(result.inserted_id)}), 201

@users_bp.route('/<item_id>', methods=['PUT'])
def update_item(item_id):
    data = request.get_json()
    result = col.edit_registry(item_id, data)
    if result.modified_count:
        return jsonify({'message': 'Item updated'}), 200
    return jsonify({'error': 'Item not found'}), 404

@users_bp.route('/<item_id>', methods=['DELETE'])
def delete_item(item_id):
    result = col.delete_registry(item_id)
    if result.deleted_count:
        return jsonify({'message': 'Item deleted'}), 200
    return jsonify({'error': 'Item not found'}), 404
