from keras.models import load_model
from keras.preprocessing import image
from keras.backend import clear_session
from PIL import Image
import numpy as np
from django.templatetags.static import static
from io import BytesIO

size = (224,224)

hdf5_file_name = "caffe_concierge_django/"+static("model.h5")

caffe_list = ['도로시인호텔', '스탠다드커피바', '더달달', '빈브라더스', '수수커피', '세루리안커피', '빈스플', '컴포테이블',
       '에이블스퀘어', '카페마마스', '마먕갸또', 'getsomecoffeedownstairs', '떼시스', '클로리스티룸',
       '에스프레소퍼블릭', '카페스팟', '피아노리브레', '베이커스필드', '아우어커피', '가비터']

def byte_to_tensor(image_data):

    byte_data = None
    img = None

    byte_data = image_data.read()
    img = Image.open(BytesIO(byte_data))

    # convert PIL.Image.Image type to 3D tensor with shape (224, 224, 3)
    x = np.expand_dims(image.img_to_array(img.resize((224, 224))), 0)
    # convert 3D tensor to 4D tensor with shape (1, 224, 224, 3) and return 4D tensor

    return x

def image_to_caffe(img_data):
    clear_session()
    model = load_model(hdf5_file_name)

    img = byte_to_tensor(img_data)
    
    result = np.argmax(model.predict(img))
    caffe = caffe_list[-result]

    return caffe
