
from flask import Flask ,render_template
from flask import jsonify
from flask import request
import mysql.connector
from mysql.connector import errorcode

app = Flask(__name__)



MYSQL_SETTING = {
  'user':'root',
  'password':'root',
  'database':'Kaidee',
  'host':'localhost',
}


def queryDB(query):
  cnx = mysql.connector.connect(**MYSQL_SETTING)
  cursor = cnx.cursor()
  cursor.execute(query)
  result = []
  for some in cursor:
    result.append({some[0]:some[1]})
  cursor.close()
  cnx.close()
  return result

def insertDB(query):
  cnx = mysql.connector.connect(**MYSQL_SETTING)
  cursor = cnx.cursor()
  cursor.execute(query)
  result = []
  for some in cursor:
    result.append({some[0]:some[1]})
  cnx.commit() 
  cursor.close()
  cnx.close()
  return result  
# send userid return rid,buyer_uid,seller_uid,iid,sid,name for all room that used by that user 
# example localhost:5000/ChatRooms/123
@app.route('/ChatRooms/<uid>', methods=['GET'])
def getChatRooms(uid):
  query = ("SELECT * FROM ChatRooms NATURAL JOIN ServiceOffering NATURAL JOIN Services WHERE buyer_uid =\'" + uid + "\' OR seller_uid =\'" + uid + "\'")
  result = queryDB(query)
  return jsonify({'result' : result})

  
# send rid return rid,timestamp,title,message,form_url,image_url for all message in that rid 
# example localhost:5000/Messages/123
@app.route('/Messages/<rid>', methods=['GET'])
def get_Messages(rid):
  query = ("SELECT * FROM ChatMessages WHERE rid =\'" + rid + "\'")
  result = queryDB(query)
  return jsonify({'result' : result})

# will finish 
# LOL
@app.route('/Messages/', methods=['POST'])
def post_Messages():
  query = ("INSERT INTO ChatMessages")
  result = insertDB(query)
  return jsonify({'result' : result})  

# send uid return uid,first_name,last_name,phone,email,profile_pic
# example localhost:5000/Users/123
@app.route('/Users/<uid>', methods=['GET'])
def get_Users(uid):
  query = ("SELECT * FROM Users WHERE uid =\'" + uid + "\'")
  result = queryDB(query)
  return jsonify({'result' : result})

# will need to change to POST will make it by the end of the week
# will fix later don't know how to autogen fid 
@app.route('/Feedback/<buyer_uid>/<seller_uid>/<rating>/<comments>/<iid>', methods=['GET'])
def post_Feedback(buyer_uid,seller_uid,rating,comments):
  query = ("INSERT INTO Feedback")
  result = insertDB(query)
  return jsonify({'result' : result})

#need to get seller_uid and do another query for more seller information possible for frontend to call getUsers again
#will return  iid, name, description, price, cid, since, seller_uid, product_location
#might need another table to collect product location
@app.route('/Product/<iid>', methods=['GET'])
def get_Products(iid):
  query = ("SELECT * FROM ItemListing WHERE iid = \'"+ iid +"\'")
  result = queryDB(query)
  return jsonify({'result' : result})


#send iid return iid,img_id,url,name for all of images for that item
@app.route('/Images/<iid>', methods=['GET'])
def get_Images(iid):
  query = ("SELECT * FROM ProductImages WHERE iid = \'"+ iid +"\'")
  result = queryDB(query)
  return jsonify({'result' : result})

#need to discuss later
@app.route('/ProductForCategory/<cid>', methods=['GET'])
def get_product_category(cid):
  query = ("")
  result = queryDB(query)
  return jsonify({'result' : result})

#need to discuss later
@app.route('/RecommendedProducts/<uid>', methods=['GET'])
def get_Recommended(uid):
  query = ("")
  result = queryDB(query)
  return jsonify({'result' : result})

if __name__ == '__main__':
    app.run(debug=True)

