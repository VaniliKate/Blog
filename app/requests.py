import urllib, json
def configure_request(app):
    global quote_api 
    quote_api = app.config['QUOTE_API']

def quote_of_the_day():
    quote_url = quote_api.format('qod')
    
    with urllib.request.urlopen(quote_url) as quotes_data:
        quotes = json.loads(quotes_data.read())
        
    return(quotes['contents']['quotes'][0]['quote'])