# Copyright 2022 Google LLC
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#      http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

"""Flask Web Server"""

import os
import re

from consts import LOCATION
from consts import PROJECT_ID
from consts import VALID_LANGUAGES



from flask import Flask
from flask import render_template
from flask import request
from google.api_core.exceptions import ResourceExhausted
from werkzeug.exceptions import HTTPException

app = Flask(__name__)

FORM_OPTIONS = {
    "language_list": VALID_LANGUAGES,
    "default_language": VALID_LANGUAGES[0],
}



@app.route("/", methods=["GET"])
def index() -> str:
    """
    Web Server, Homepage for Contract
    """

    return render_template(
        "index.html"
    )






if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=int(os.environ.get("PORT", 8080)))