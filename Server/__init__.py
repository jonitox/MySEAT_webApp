from flask import Flask
## static_folrder의 경로를 다시 지정해야합니다!
app = Flask(__name__,static_folder='${work_space}\Server\static')

import Server.main
