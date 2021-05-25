import click
import webbrowser
import requests
import json


@click.group()
def cli():
    pass

# function to find a short url
@click.command()
@click.option("-l", required=True, type=str, help="Link to find")
def find(l):
    if(l == ""):
        click.echo("You must specify a url.")
        exit()
    url = "https://link.untypical.co.uk/api/find"
    headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_11_5) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/50.0.2661.102 Safari/537.36'}
    data = {
        "url": l, # required
    }
    response = requests.get(url, params = data, headers = headers);
    urlData = json.loads(response.content.decode());
    try:
        click.echo(urlData['url'])
        webbrowser.open(urlData['url'])
    except: 
        click.echo(urlData['message'])

# function to generate a short url
@click.command()
@click.option("-l","--link", required=True, type=str, help="Link to shorten")
@click.option("-vr", required=False, default=0, type=int, help="Verify response from url is 200")
@click.option("-vl", required=False, default=0, type=int, help="Verify the regex of the link passed")
@click.option("-e", required=False, type=str, help="Expiry date for the short url")
def generate(link, vr, vl, e):
    if(link == ""):
        click.echo("You must specify a url.")
        exit()
    
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

cli.add_command(find)
cli.add_command(generate)