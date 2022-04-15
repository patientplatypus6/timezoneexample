# Example Time Zone Application

To run navigate to /front and double click index.html (you can also serve this using http-server from nginx or httpSimpleServer from python or whichever server you prefer).
For the backend, navigate to /back, run source .env/bin/activate and then ./run.sh

Note that I've handled the case where the time would cross over midnight or noon, but didn't handle the case of when the date changes (the 15th in one time zone and the 16th in another for example), or anything to do with daylight savings time. More information on time zone formatting can be found here (https://docs.python.org/3/library/datetime.html#strftime-and-strptime-behavior). 
