from flask import abort
from flask import jsonify
from flask import request
from flask_restplus import Resource

from api import socketio
from api.util.dto import MessageDto

api = MessageDto.api
_message = MessageDto.message


@api.route("/status")
class Message(Resource):
    @api.expect(_message, validate=True)
    def post(self):
        if not request.json:
            abort(400)

        print(request.json)
        d = request.json.get("message", None)
        print("receive data:{}".format(d))

        socketio.emit('status_response', {'data': d})
        return jsonify(
            {"response": "ok"}
        )
