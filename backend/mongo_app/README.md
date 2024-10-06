```markdown
# Forum API with Flask and MongoDB

This API provides a forum system where each forum corresponds to a collection in MongoDB. Users can create, edit, list, and delete forums and posts, with support for timestamp-ordered operations.

## Requirements

- Python 3.x
- Flask
- PyMongo
- MongoDB (can be run in a Docker container)

## Environment Setup

1. **Clone the repository:**
   ```bash
   git clone <repo_url>
   cd <repo_name>
   ```

2. **Install the dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

3. **Run MongoDB using Docker:**
   Ensure that MongoDB is running in a Docker container with the `27017` port exposed.
   ```bash
   docker run -d -p 27017:27017 --name mongo mongo
   ```

4. **Set MongoDB environment variables:**
   Check the `app/config.py` file to ensure that the MongoDB connection settings are correct.

5. **Run the Flask application:**
   ```bash
   flask run
   ```

## API Routes

### **Forums**

#### Create a Forum
**POST:** `/api/forum/<subject_code>`  
**Request:**
```json
{
  "User": "00.0.0000",
  "Type": "POST",
  "text": "FORUM <subject_code> CREATED",
  "time": 1234567890
}
```
**Response:**
```json
{
  "status": "success",
  "message": "Forum Created"
}
```

#### Delete a Forum
**DELETE:** `/api/forum/<subject_code>`  
**Request:** N/A  
**Response:**
```json
{
  "status": "success",
  "message": "Collection dropped successfully."
}
```

### **Posts**

#### Create a Post
**POST:** `/api/forum/<subject_code>/`  
**Request:**
```json
{
  "User": "00.0.0000",
  "Type": "POST",
  "text": "Post text",
  "time": 1234567890
}
```
**Response:**
```json
{
  "status": "success",
  "inserted_id": "60b1234567890abcdef12345",
  "doc": {
    "_id": "60b1234567890abcdef12345",
    "User": "00.0.0000",
    "Type": "POST",
    "text": "Post text",
    "time": 1234567890
  }
}
```

#### List Posts
**GET:** `/api/forum/<subject_code>/`  
**Note:** (Optional filters in the request body)  
**Response:**
```json
{
  "status": "success",
  "result": [
    {
      "_id": "60b1234567890abcdef12345",
      "User": "00.0.0000",
      "Type": "POST",
      "text": "Post text",
      "time": 1234567890
    }
  ]
}
```

#### Update a Post
**PUT:** `/api/forum/<subject_code>/?id=<post_id>`  
**Request:**
```json
{
  "text": "Updated post text",
  "time": 1234567891
}
```
**Response:**
```json
{
  "status": "success",
  "modified_count": 1
}
```

#### Delete Posts
**DELETE:** `/api/forum/<subject_code>/`  
**Request:**
```json
{
  "User": "00.0.0000"
}
```
**Response:**
```json
{
  "status": "success",
  "deleted_count": 1
}
```