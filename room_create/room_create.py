import os
import subprocess
import tempfile
import shutil
from flask import Flask
from flask import send_file, request, abort

app = Flask(__name__)


@app.route('/plan', methods=['GET', 'POST'])
def gen_plan():
    if request.values.get('data'):
        data = request.values['data']
        with open("room_data.json", "w") as f:
            f.write(data)
        blender = subprocess.Popen(["blender", "--background", "--python", "blender_script.py"])
        blender.wait()
        temp_file_obj = tempfile.NamedTemporaryFile(mode='w+b', suffix='3ds')
        try:
            room = open('/tmp/room.3ds', 'rb')
        except OSError:
            return abort(500)
        shutil.copyfileobj(room, temp_file_obj)
        room.close()
        os.remove('/tmp/room.3ds')
        temp_file_obj.seek(0, 0)
        return send_file(temp_file_obj, as_attachment=True, attachment_filename='room.3ds')
    else:
        return abort(400)


if __name__ == '__main__':
    app.run()
