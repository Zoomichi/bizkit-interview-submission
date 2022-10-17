from flask import Blueprint, request

from .data.search_data import USERS


bp = Blueprint("search", __name__, url_prefix="/search")


@bp.route("")
def search():
    return search_users(request.args.to_dict()), 200


def search_users(args):
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

    # Implement search here!
    if args == {}:
        return USERS
    
    result = []
    isAdded = {}
    for key, val in args.items():
        for user in USERS:
            if key == "id":
                if user[key] == val:
                    if user["id"] not in isAdded:
                        isAdded[user["id"]] = True
                        result.append(user)
                    elif isAdded[user["id"]] == True:
                        pass                        
            elif key == "name" or key == "occupation":
                if val.lower() in user[key].lower():
                    if user["id"] not in isAdded:
                        isAdded[user["id"]] = True
                        result.append(user)
                    elif isAdded[user["id"]] == True:
                        pass                        
            elif key == "age":
                if user[key] <= int(val)+1 and user[key] >= int(val)-1:
                    if user["id"] not in isAdded:
                        isAdded[user["id"]] = True
                        result.append(user)
                    elif isAdded[user["id"]] == True:
                        pass

    if result == []:
        return USERS
    else:
        return result