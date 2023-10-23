
1. clone this repository
2. add your df-messenger script in templates/index.html from the df-messenger integration section in dialogflow
3. add the image you would like to use as the background for your "website" in static/images. Delete the image that is currently there and add your own instead.
4. update your templates/index.html file to use the images from step 3.
5. install python3-venv, similar to these instructions https://cloud.google.com/python/docs/setup#linux
6. inside of the repository, create a virtual environment by running 
    `python3 -m venv env`
7. Activate the virtual environment by running 
    `source env/bin/activate`
8. install requirements by running pip install -r requirements.txt
9. test locally by running 
    `gunicorn --bind :8080 main:app`
10. After you verify that the app is working as expected, deploy to cloud run
    `gcloud run deploy <service-name> --source .`

