#Access Log Parser


This is a simple yet cool little project to parse an apache log and output an html file containing all of the entries in a formatted table. 

#Implementation
It uses some regular expressions and the [python-geoip]( http://pythonhosted.org/python-geoip/) API. 


hosted on [here](
http://runnable.com/VIc_XEkD1G12SKz0/apache-parsing-python-addteq-for-file-input
)

Nothing Crazy complex happening here but it's useful to look at for simple things like reading lines out of files in python, lots of substrings etc.

##Usage

All that has to happen on this front is to install the requirements, which is essentially the python geoip. Other than that just type 

```python
python script.py access_log > output.html
```
Or alternatively you could simply type, ```make```. 


Have fun! 

