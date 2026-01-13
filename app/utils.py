from flask import request , make_response
import json


def get_recently_viewed():
    """
    To get the recently viewed product ids and convert them to python list.
    """
    cookies_values = request.cookies.get('recently_viewed')

    if cookies_values:
        try:
            product_id = json.loads(cookies_values)
            return product_id
        except:
            return[]

    return[]

#another helper function
def add_to_recently_viewed(response,product_id):
    """
    Docstring for add_to_recently_viewed
    remove duplicate,insert new, limit to 8 product ids
    
    :param response: A flask response obj
    :param product_id: new recently viewed product id.
    """
    current_recently_viewed = get_recently_viewed()

    #removing duplicated ids
    if product_id in current_recently_viewed:
        current_recently_viewed.remove(product_id)
    
    #inserting new ids
    current_recently_viewed.insert(0,product_id)

    #limiting to 8 product ids
    current_recently_viewed = current_recently_viewed[:8]

    #converting to json string
    cookies_values = json.dumps(current_recently_viewed)

    #set the cookies
    response.set_cookie(
        'recently_viewed',
        cookies_values,
        max_age = 30 * 24 * 30 * 30 # 30 days
    )

    return response