#the file to start our web application

from website import create__app

app = create__app()

if __name__ == '__main__':          #this condition means that only if we run this file, not if we import this file i.e. main.py, are we going to run the next line of code
    app.run(debug=True)             #in this line debug=true means that every time we make a change to the website, it will keep updating the website. should turn it of when running into production