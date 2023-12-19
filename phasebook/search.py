from flask import Blueprint, request

from .data.search_data import USERS

bp = Blueprint("search", __name__, url_prefix="/search")

@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200

def search_users(args):
    results = USERS  #stores the entire user list

    id_param = args.get("id") #used to call the value of the parameters present in the url
    name = args.get("name")
    age = args.get("age")
    occupation = args.get("occupation")

    results = USERS

    if id_param is not None:
        results = [user for user in results if user["id"] == id_param] #checks if the parameter has the same value in the USERS constant 

    if name is not None:
        name = name.lower()
        results += [user for user in USERS if name in user["name"].lower()] #checks if the parameter has the same value in the USERS constant and change the parameter input into lower-case letters

    if age is not None: #checks if the parameter has the same value in the USERS constant
        age = int(age)
        results += [user for user in USERS if age - 1 <= user["age"] <= age + 1]

    if occupation is not None:
        occupation = occupation.lower()
        results += [user for user in USERS if occupation in user["occupation"].lower()] #checks if the parameter has the same value in the USERS constant and change the parameter input into lower-case letters

    unique_results = list({user["id"]: user for user in results}.values()) #remove duplicates based on user ID

    return unique_results


    """Search users database

    Parameters:
        args: a dictionary containing the following search parameters:
            id: string
            name: string
            age: string
            occupation: string

    Returns:
        a list of users that match the search parameters
    """
