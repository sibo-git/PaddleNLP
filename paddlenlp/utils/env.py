# Copyright (c) 2020  PaddlePaddle Authors. All Rights Reserved.
#
# Licensed under the Apache License, Version 2.0 (the "License"
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
"""
This module is used to store environmental variables in PaddleNLP.
PPNLP_HOME              -->  the root directory for storing PaddleNLP related data. Default to ~/.paddlenlp. Users can change the
├                            default value through the PPNLP_HOME environment variable.
├─ MODEL_HOME              -->  Store model files.
└─ DATA_HOME         -->  Store automatically downloaded datasets.
"""
import os


def _get_user_home():
    return os.path.expanduser("~")


def _get_ppnlp_home():
    if "PPNLP_HOME" in os.environ:
        home_path = os.environ["PPNLP_HOME"]
        if os.path.exists(home_path):
            if os.path.isdir(home_path):
                return home_path
            else:
                raise RuntimeError("The environment variable PPNLP_HOME {} is not a directory.".format(home_path))
        else:
            return home_path
    return os.path.join(_get_user_home(), ".paddlenlp")


def _get_sub_home(directory, parent_home=_get_ppnlp_home()):
    home = os.path.join(parent_home, directory)
    if not os.path.exists(home):
        os.makedirs(home, exist_ok=True)
    return home


USER_HOME = _get_user_home()
PPNLP_HOME = _get_ppnlp_home()
MODEL_HOME = _get_sub_home("models")
HF_CACHE_HOME = os.environ.get("HUGGINGFACE_HUB_CACHE", MODEL_HOME)
DATA_HOME = _get_sub_home("datasets")
PACKAGE_HOME = _get_sub_home("packages")
DOWNLOAD_SERVER = "http://paddlepaddle.org.cn/paddlehub"
FAILED_STATUS = -1
SUCCESS_STATUS = 0

LEGACY_CONFIG_NAME = "model_config.json"
CONFIG_NAME = "config.json"
PYTORCH_WEIGHT_FILE_NAME = "pytorch_model.bin"
PADDLE_WEIGHT_FILE_NAME = "model_state.pdparams"

# for conversion
ENABLE_TORCH_CHECKPOINT = os.getenv("ENABLE_TORCH_CHECKPOINT", True)
