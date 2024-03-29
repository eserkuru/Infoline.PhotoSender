import requests;
import os;

function SendDataToServer(imagePath):
    image_filename = os.path.basename(image_path)
    multipart_form_data = {
        'image': (image_filename, open(image_path, 'rb')),
        'temperature': ('', str(temperature)),
    }
    response = requests.post('http://www.example.com/api/v1/sensor_data/',
                             files=multipart_form_data)
    print(response.status_code)
    