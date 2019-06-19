# hitchARide
Simple webapp for pairing drivers with riders (right now for hiking purposes).
Check it out at: http://hitcharide.pythonanywhere.com/

## How to run locally: 
Note: this works on Unix based systems with Python 3 already installed. I have not tested it on Windows. If you do get it working on a Window's device, let me know how and we'll update this document. 

In a new directory:
`$ pip install virtualenv`  
  
`$ virtualenv --python=python3.6 myenv`  
`$ source myenv/bin/activate`  
  
`$ pip3 install flask`  
`$ pip3 install flask-cors`  
`$ pip3 install passlib`  
  
Now you should be able to clone/fork this repo into this directory. To create a local database (after you have the project files in the directory):  
`$ sqlite3 database.db < schema.sql`  
  
To run the project:  
`python3 app.py`  
  
To View the project, visit: http://127.0.0.1:5000/ in a web browser.  
  
## Want to help out? 
Awesome, thanks! Please submit your ideas as an issue or pull requests with updated code. 
