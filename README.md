# poc-api

| Lang| Version |
| ----------- | ----------- |
| Python      | 3.10.4       |

## Starting environment
Windows users

```
$ py -m pip install --user virtualenv 
$ py -m venv env   
$ .\env\Scripts\activate  
```

Unix
```
$ python3 -m venv env
$ source env/bin/activate
```

## Installing dependencies & running
```
$ pip install -r requirements.txt

$ scrapy runspider scraper.py -o angeloni.jl 

$ python3 app.py
$ sudo chmod +x app.py 	# Optional
$ ./app.py 				# Optional

```
