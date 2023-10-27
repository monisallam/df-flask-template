
1. clone this repository by running
`git clone https://github.com/monisallam/df-flask-template.git`
2. add your df-messenger script in templates/index.html from the df-messenger integration section in dialogflow. Replace everything inside of the body with you df-messenger script.

    ```html
    <body>
       <!-- Delete the paste element and put your messenger script here-->
   </body>

     
3. add the image you would like to use as the background for your "website" in the static/images directory that you cloned from this repository. Delete the image that is currently there and add your own instead. 

4. update your templates/index.html file to use the images from step 3. You can also change the color of the chat bubble.

    ```html
        <style>
                body {
                    background-image: url('{{ url_for('static', filename='images/<put image filename here>') }}');
                    background-repeat: no-repeat;
                    background-attachment: fixed;  
                    background-size: cover;
                }
                df-messenger{
                    --df-messenger-button-titlebar-color: blue;
                }
        </style>
5. install python3-venv, similar to these instructions https://cloud.google.com/python/docs/setup#linux, if you do not already have it installed
6. inside of the top level of the repository, create a virtual environment by running 
    `python3 -m venv env`
7. Activate the virtual environment by running 
    `source env/bin/activate`
8. install requirements by running 
    `pip install -r requirements.txt`
9. test locally by running 
    `gunicorn --bind :8080 main:app`
10. After you verify that the app is working as expected, deploy to cloud run
    `gcloud run deploy <service-name> --source .`

