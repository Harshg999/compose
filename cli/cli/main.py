# -- coding: utf-8 --
# Licensed to Cloudera, Inc. under one
# or more contributor license agreements.  See the NOTICE file
# distributed with this work for additional information
# regarding copyright ownership.  Cloudera, Inc. licenses this file
# to you under the Apache License, Version 2.0 (the
# "License"); you may not use this file except in compliance
# with the License.  You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

import typer

app = typer.Typer()


@app.callback()
def callback():
    """
    Query your Data
    """


@app.command()
def login():
    import json

    import requests

    session = requests.Session()

    data = {
        "username": "demo",
        "password": "demo",
    }

    response = session.post("https://demo.gethue.com/api/token/auth", data=data)
    print(
        "Auth: %s %s"
        % ("success" if response.status_code == 200 else "error", response.status_code)
    )

    token = json.loads(response.content)["access"]
    print("Token: %s" % token)

    response = requests.post(
        "https://demo.gethue.com/api/query/autocomplete",
        headers={
            "Authorization": "Bearer %s" % token,
            "Content-Type": "application/x-www-form-urlencoded",
        },
        data={"snippet": json.dumps({"type": "mysql"})},
    )
    print(response.status_code)
    print(response.text)


@app.command()
def query():
    """
    Execute some SQL statements
    """
    typer.echo("Execute SQL")


@app.command()
def storage():
    """
    Access data files
    """
    typer.echo("List, upload, download data files")
