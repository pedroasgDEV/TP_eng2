from flask import Blueprint, request, jsonify
from app.utils.connectDB import MongoDB
from app.utils.forums import Forums
from app.config import mongodb_config
import time

forum_bp = Blueprint('forum_bp', __name__)

mongo = MongoDB(mongodb_config["HOST"], mongodb_config["PORT"], mongodb_config["DATABASE"])

# Create Forum
@forum_bp.route('/<subject_code>', methods=['POST'])
def create_forum(subject_code):
    forum = Forums(mongo, subject_code)
    
    doc = {
        "User": "00.0.0000",
        "Type": "POST",
        "text": f"FORUM {subject_code} CREATED",
        "time": time.time()
    }
    
    result = forum.insert(doc)
    
    if result["status"] == "success":
        return jsonify({ "status": "success", "message": "Forum Created"}), 201
    else:
        return jsonify({ "status": "error", "message": "Forum not Created"}), 400

# Delete Forum
@forum_bp.route('/<subject_code>', methods=['DELETE'])
def delete_forum(subject_code):
    forum = Forums(mongo, subject_code)
    
    result = forum.delete_collection()
    
    if result["status"] == "success":
        return jsonify(result), 200
    else:
        return jsonify(result), 400

# Create Post
@forum_bp.route('/<subject_code>/', methods=['POST'])
def create_post(subject_code):
    forum = Forums(mongo, subject_code)
    
    data = request.get_json()
    data["time"] = time.time()
    result = forum.insert(data)
    
    if result["status"] == "success":
        data["_id"] = result["_id"]
        result["doc"] = data
        return jsonify(result), 201
    else:
        return jsonify(result), 400

# Select Post
@forum_bp.route('/<subject_code>/', methods=['GET'])
def select_posts(subject_code):
    forum = Forums(mongo, subject_code)
    
    data = request.get_json()
    pipeline = [
        {"$match": data},
        {"$sort": {"time": -1}}
    ]
    result = forum.select(pipeline)
    
    if result["status"] == "success":
        return jsonify(result), 200
    else:
        return jsonify(result), 404

# Update Post
@forum_bp.route('/<subject_code>/', methods=['PUT'])
def update_post(subject_code):
    forum = Forums(mongo, subject_code)
    
    id = request.args.get("id")
    
    if not id: return jsonify({'message': 'Missing Args'}), 400
    
    data = request.get_json()
    data["time"] = time.time()
    result = forum.update(id, data)
    
    if result["status"] == "success":
        return jsonify(result), 200
    else:
        return jsonify(result), 404
    
# Delete Post
@forum_bp.route('/<subject_code>/', methods=['DELETE'])
def delete_posts(subject_code):
    forum = Forums(mongo, subject_code)
    
    data = request.get_json()
    result = forum.delete(data)
    
    if result["status"] == "success":
        return jsonify(result), 200
    else:
        return jsonify(result), 404