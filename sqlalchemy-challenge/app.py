import sqlalchemy
from flask import Flask, jsonify
from sqlalchemy import create_engine, func, inspect
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base

engine = create_engine("sqlite:///Resources/hawaii.sqlite")
Base = automap_base()
Base.prepare(engine, reflect = True)

measurement = Base.classes.measurement
station = Base.classes.station



app = Flask(__name__)

@app.route("/")
def welcome():
	return(
		f"Available Routes: <br/>"
		f"/api/v1.0/precipitation <br/>"
		f"/api/v1.0/stations <br/>"
		f"/api/v1.0/tobs <br/>"
		f"/api/v1.0/<start> <br/>"
		f"/api/v1.0/<start>/<end> <br/>")






if __name__ == "__main__":
	app.run(debug = True)