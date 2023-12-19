import time
from flask import Blueprint

from .data.match_data import MATCHES


bp = Blueprint("match", __name__, url_prefix="/match")


@bp.route("<int:match_id>")
def match(match_id):
    if match_id < 0 or match_id >= len(MATCHES):
        return "Invalid match id", 404

    start = time.time()
    msg = "Match found" if (is_match(*MATCHES[match_id])) else "No match"
    end = time.time()

    return {"message": msg, "elapsedTime": end - start}, 200
 
    
def is_match(fave_numbers_1, fave_numbers_2):
    set1 = set(fave_numbers_1) #use to store multiple items in single variable
    set2 = set(fave_numbers_2) #use to store multiple items in single variable
    result = set2.issubset(set1) #returns true if all items in set2 is present in set1
    return result
