import webbrowser
import click
import os
import requests
import json

@click.group()
def cli():
    pass

@click.command()
@click.option("-l", required=True, type=str, default="", help="Link to find")
def url(l):
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

cli.add_command(url)
