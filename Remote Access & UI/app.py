from flask import Flask, render_template, request
import sqlite3

app = Flask(__name__)

# conn = sqlite3.connect('/home/pi/sensing.db')
# cursor = conn.cursor()

@app.route('/')
def index():
	return render_template('index.html')

@app.route('/templates/pilog.html')
def pilog():
	return render_template('pilog.html')

@app.route('/data/recentSensorData.txt')
def sensorData():
	return render_template('data/recentSensorData.txt')

@app.route('/data/images.txt')
def paths():
	return render_template('data/images.txt')

@app.route( '/home/pi/images/ME_1.png')
def img1():
	return render_template('/home/pi/images/ME_1.png')

@app.route( '/home/pi/images/ME_4.jpg')
def img2():
	return render_template('/home/pi/images/ME_4.jpg')

@app.route( '/home/pi/images/ME_2.png')
def img3():
	return render_template('/home/pi/images/ME_2.png')

@app.route( '/home/pi/images/ME_3.jpeg')
def img4():
	return render_template('/home/pi/images/ME_3.jpeg')

@app.route('/templates/data/pilog.txt')
def log():
	return render_template('data/pilog.txt')

@app.route('/templates/help.html')
def help():
	return render_template('help.html')



@app.route('/climatedata')
def retrieve_climate_data():
		conn = sqlite3.connect('/home/pi/sensing.db')
		cursor = conn.cursor()

		# id=request.args.get('id')
		id=2
		date=request.args.get('date')
		date='2023-05-18'
		time=request.args.get('time')
		if id == 1:
			# Retrieve last three climate measurements from the database
			cursor.execute("SELECT * FROM climate ORDER BY id DESC LIMIT 3")
		elif id == 2 and date:
			# Retrieve climate measurements from the specified date
			cursor.execute("SELECT * FROM climate WHERE date = ? ", (date,))
		elif id == 3 and time:
			# Retrieve climate measurements from the specified time range
			cursor.execute("SELECT * FROM climate WHERE time <= ? ", (time,))

		# Fetch all the rows
		rows = cursor.fetchall()

		#Close the database connection
		conn.close()

		
		with open('/home/pi/webapp/templates/data/recentSensorData.txt','w') as file:
			for row in rows:
				file.write('|'.join(str(item) for item in row)+'<br>')
		
		return render_template('index.html')

@app.route('/images')
def retrieve_images():
		conn = sqlite3.connect('/home/pi/images.db')
		cursor = conn.cursor()

		id=request.args.get('id')
		id=1
		date=request.args.get('date')
		time=request.args.get('time')
		if id == 1:
			# Retrieve last three images from the database
			cursor.execute("SELECT path FROM images ORDER BY id DESC LIMIT 3")
		elif id == 2 and date:
			# Retrieve climate measurements from the specified date
			cursor.execute("SELECT * FROM climate WHERE date = ? ", (date,))
		elif id == 3 and time:
			# Retrieve climate measurements from the specified time range
			cursor.execute("SELECT * FROM climate WHERE time <= ? ", (time,))

		# Fetch all the rows
		rows = cursor.fetchall()

		#Close the database connection
		conn.close()

		paths=[]


		with open('/home/pi/webapp/templates/data/images.txt','w') as file:
			for row in rows:
				file.write('|'.join(str(item) for item in row)+'<br>')
			
			
		with open('/home/pi/webapp/templates/data/images.txt') as file:
			paths = [line.rstrip() for line in file]
		
		
		path1=paths[0]
		path2=paths[1]
		path3=paths[2]

		return render_template('index.html',path1=path1,path2=path2,path3=path3)

if __name__ == '__main__':
	app.run(debug=True, host='0.0.0.0')