from flask import jsonify, request, url_for, abort
from app import db
from app.models import User
from app.api import bp
from app.api.auth import token_auth
from app.api.errors import bad_request



@bp.route('/rechnen', methods=['POST'])
@token_auth.login_required
def rechnen():

    error = None
    result = None
    operation = request.args['operation']
    
    if "+" in operation:
            operator = operation.split("+")
            result = int(operator[0]) + int(operator[1])
    if "-" in operation:
            operator = operation.split("-")
            result = int(operator[0]) - int(operator[1])
    if "/" in operation:
            operator = operation.split("/")
            result = int(operator[0]) / int(operator[1])
    if "*" in operation:
            operator = operation.split("*")
            result = int(operator[0]) * int(operator[1])
    else:
            result = "Nix"
        
    response = {"Rechnung": operation, "Resultat": result}
    return response, 200
        
 
    