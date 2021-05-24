# mini_url_cli
CLI for shortening urls

Installation
1. Download this repository
2. Change directory into the repo
3. Type the following command "pip install ."

### Generate a new short URL

Parameters 
* -l (string) url to shorten
* -vl (bool) optional, validate link with regex
* -vr (bool) optional, validate response is 200 from link
* -e (string) optional, expiry date for short url

`miniurl generate url -l "https://www.google.com" -vr 1 -vl 1 -e 2021-06-01`

### Find long url

Parameters
* -l (string) short url to find

`miniurl find url -l "https://short.link/abc123"`

