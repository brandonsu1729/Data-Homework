import sqlalchemy
from flask import Flask, jsonify
from sqlalchemy import create_engine, func, inspect
from sqlalchemy.orm import Session
from sqlalchemy.ext.automap import automap_base
import numpy as np
import datetime as dt
from dateutil.relativedelta import relativedelta

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
		f"/api/v1.0/start <br/>"
		f"/api/v1.0/start/end <br/>")

@app.route("/api/v1.0/precipitation")
def precip():
	session = Session(engine)
	results = session.query(measurement.date, measurement.prcp).all()
	session.close()
	dateprcp_dict = {}
	for date, prcp in results:
		dateprcp_dict.update({date: prcp})
	return jsonify(dateprcp_dict)

@app.route("/api/v1.0/stations")
def stations():
	session = Session(engine)
	results = session.query(station.name,measurement.station).\
				group_by(station.name).\
				filter(station.id == measurement.id).all()
	session.close()
	stations = []
	for name, statid in results:
		stations.append([name, statid])
	#stations = [station[0], station[1] for station in results]
	return jsonify(stations)

@app.route("/api/v1.0/tobs")
def temps():
	session = Session(engine)
	most_active = session.query(func.count(measurement.station), measurement.station).\
		group_by(measurement.station).\
		order_by(func.count(measurement.station).desc()).first()[1]
	latest_date = session.query(measurement.date).filter(measurement.station == most_active).order_by(measurement.date.desc()).first()[0]

	latest_datetime = dt.datetime.strptime(latest_date, '%Y-%m-%d').date()
	year_earlier = latest_datetime + relativedelta(months = -12)

	temps = session.query(measurement.date, measurement.tobs).\
		order_by(measurement.date).\
		filter(measurement.date < latest_date).\
		filter(measurement.date > year_earlier).\
		filter(measurement.station == most_active).all()
	session.close()
	return jsonify(temps)

@app.route("/api/v1.0/<start>")
def start(start):
	session = Session(engine)
	temp_stats = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).\
		filter(measurement.date >= start).all()
	session.close()
	return (f"After {start}, the minimum temperature was {temp_stats[0][0]}, maximum temp was {temp_stats[0][1]}, and the average was {round(temp_stats[0][2],2)}.")
	#return jsonify(temp_stats)

@app.route("/api/v1.0/<start>/<end>")
def startend(start, end):
	session = Session(engine)
	temp_stats = session.query(func.min(measurement.tobs), func.max(measurement.tobs), func.avg(measurement.tobs)).\
		filter(measurement.date >= start).\
		filter(measurement.date <= end).all()
	session.close()

	return (f"Between {start} and {end}, the minimum temperature was {temp_stats[0][0]}, maximum temp was {temp_stats[0][1]}, and the average was {round(temp_stats[0][2],2)}.")

if __name__ == "__main__":
	app.run(debug = True)