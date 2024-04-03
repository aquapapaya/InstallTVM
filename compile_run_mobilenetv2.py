######################################################################
# Set environment variables
# -------------------------

import tvm

target = "llvm"
target_host = "llvm"
ctx = tvm.cpu(0)

model_path = "./1.tflite"
input_name = "input"
data_type = "uint8" # model's input type

######################################################################
# Set input shape
# ---------------

batch_size = 1
num_class = 1001
image_dimention = 3
image_shape = (224, 224)
data_shape = (batch_size,) + image_shape + (image_dimention,)
out_shape = (batch_size, num_class)

######################################################################
# Load TFLite model
# -----------------

import os
tflite_model_file = os.path.join(model_path)
tflite_model_buf = open(tflite_model_file, "rb").read()

# Get TFLite model from buffer
try:
    import tflite
    tflite_model = tflite.Model.GetRootAsModel(tflite_model_buf, 0)
except AttributeError:
    import tflite.Model
    tflite_model = tflite.Model.Model.GetRootAsModel(tflite_model_buf, 0)

######################################################################
# Convert TFLite model into Relay IR
# ----------------------------------

import tvm.relay as relay
dtype_dict = {input_name: data_type}
shape_dict = {input_name: data_shape}

mod, params = relay.frontend.from_tflite(tflite_model,
                                         shape_dict=shape_dict,
                                         dtype_dict=dtype_dict)
print("Relay IR:\n", mod)

######################################################################
# Compile Relay module
# --------------------

with tvm.transform.PassContext(opt_level=3, config={"tir.disable_vectorize":True}):
    graph, lib, params = relay.build(mod, target=target, target_host=target_host, params=params)

######################################################################
# Get ImageNet lable
# ------------------

from tvm.contrib.download import download_testdata
# Load label file
label_file_url = "".join(
    [
        "https://raw.githubusercontent.com/",
        "tensorflow/tensorflow/master/tensorflow/lite/java/demo/",
        "app/src/main/assets/",
        "labels_mobilenet_quant_v1_224.txt",
    ]
)
label_file = "labels_mobilenet_quant_v1_224.txt"
label_path = download_testdata(label_file_url, label_file, module="data")

# List of 1001 classes
with open(label_path) as f:
    imagenet_labels = f.readlines()

######################################################################
# Get image of cat
# ----------------

img_file_url = "https://github.com/dmlc/mxnet.js/blob/main/data/cat.png?raw=true"
img_file = "cat.png"
img_path = download_testdata(img_file_url, img_file, module="data")

######################################################################
# Create TVM runtime and do inference
# -----------------------------------

# Apply data preprocessing
from PIL import Image
import numpy as np
img = Image.open(img_path).resize((224, 224))
image_data = np.asarray(img).astype(data_type)
image_data = np.expand_dims(image_data, axis=0)

# Create a runtime executor module
from tvm.contrib import graph_runtime
module = graph_runtime.create(graph, lib, ctx)

# Set input and parameters
module.set_input(input_name, tvm.nd.array(image_data))
module.set_input(**params)

# Run
import time
timeStart = time.time()
module.run()
timeEnd = time.time()
print("Inference time: %f" % (timeEnd - timeStart))

# Get Top-1 output
tvm_output = module.get_output(0).asnumpy()
top5 = tvm_output[0].argsort()[-5:][::-1]
print("Prediction: id " + str(top5[0]) + " name: " + imagenet_labels[top5[0]])

