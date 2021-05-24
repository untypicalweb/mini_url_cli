import click
import os
from miniurl.service import generate as g
import requests
import json
import webbrowser

@click.group()
def cli():
    pass

@click.command()
@click.option("-l","--link", default="", type=str, help="Link to shorten")
@click.option("-vr", required=False, default=0, type=int, help="Verify response from url is 200")
@click.option("-vl", required=False, default=0, type=int, help="Verify the regex of the link passed")
@click.option("-e", required=False, type=str, help="Expiry date for the short url")
# function to generate a short url
def url(link, vr, vl, e):
    url = "https://link.untypical.co.uk/api/generate"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    data = {
        "url": link, # required
        "expiry": e, # optional
        "verify_url": vl, # optional
        "verify_response": vr # optional 
    }
    response = requests.post(url, data = data, headers = headers);
    urlData = json.loads(response.content.decode());
    try:
        click.echo(urlData['data']['short_url'])
    except: 
        click.echo(urlData['message'])

cli.add_command(url)
