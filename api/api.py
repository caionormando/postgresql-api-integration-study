import os
import flask
from flask import request, jsonify
from flask_sqlalchemy import SQLAlchemy

app = flask.Flask(__name__)


app.config.from_object(os.environ['APP_SETTINGS'])
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['JSON_AS_ASCII'] = False
db = SQLAlchemy(app)
# app.config["DEBUG"] = False

from candidate.candidate import Candidate


class APIServer:

    @app.route('/', methods=['GET'])
    def home():
        return "<h1>Code challenge</h1><p>by Caio Normando</p>"

    @app.route('/addcandidate')
    def add_candidate():
        name = request.args.get('name')
        job = request.args.get('job')
        location = request.args.get('location')
        level = request.args.get('level')

        try:
            candidate = Candidate(
                name=name,
                job=job,
                location=location,
                level=level
            )
            db.session.add(candidate)
            db.session.commit()
            return "Candidate added. book id={}".format(candidate.id)
        except Exception as e:
            return str(e)

    @app.route("/getallcandidates")
    def get_all():
        try:
            candidates = Candidate.query.all()
            return jsonify([e.serialize() for e in candidates])
        except Exception as e:
            return str(e)

    @app.route("/getcandidate/<id_>")
    def get_by_id(id_):
        try:
            candidate = Candidate.query.filter_by(id=id_).first()
            return jsonify(candidate.serialize())
        except Exception as e:
            return str(e)

    app.run()
