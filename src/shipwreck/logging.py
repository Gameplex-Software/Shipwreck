# ----------------------------------------------------------------------------
# ShipHelm Copyright 2020-2023 by Gameplex Software and contributors
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
# ----------------------------------------------------------------------------

import datetime

class logging:
    def __init__(self):
        logging.log(logline="ShipWreck logging and error detection active! \n \n # ---------------------------------------------------------------------------- \n # ShipHelm Copyright 2020-2023 by Gameplex Software and contributors \n # \n # Licensed under the Apache License, Version 2.0 (the 'License'); \n # you may not use this file except in compliance with the License. \n # You may obtain a copy of the License at \n # \n # http://www.apache.org/licenses/LICENSE-2.0 \n # \n # Unless required by applicable law or agreed to in writing, software \n # distributed under the License is distributed on an 'AS IS' BASIS, \n # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. \n # See the License for the specific language governing permissions and \n # limitations under the License. \n # ----------------------------------------------------------------------------\n",type="n")
        logging.log(logline="\n   _________.__     .__         __      __                         __      \n  /   _____/|  |__  |__|______ /  \    /  \_______   ____   ____  |  | __  \n  \_____  \ |  |  \ |  |\____ \\   \/\/   /\_  __ \_/ __ \_/ ___\ |  |/ /  \n  /        \|   Y  \|  ||  |_> >\        /  |  | \/\  ___/\  \___ |    <   \n /_______  /|___|  /|__||   __/  \__/\  /   |__|    \___  >\___  >|__|_ \  \n         \/      \/     |__|          \/                \/     \/      \/  \n                                                                          ",type="n")
        print("ShipWreck logging and error detection active! \n \n # ---------------------------------------------------------------------------- \n # ShipHelm Copyright 2020-2023 by Gameplex Software and contributors \n # \n # Licensed under the Apache License, Version 2.0 (the 'License'); \n # you may not use this file except in compliance with the License. \n # You may obtain a copy of the License at \n # \n # http://www.apache.org/licenses/LICENSE-2.0 \n # \n # Unless required by applicable law or agreed to in writing, software \n # distributed under the License is distributed on an 'AS IS' BASIS, \n # WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. \n # See the License for the specific language governing permissions and \n # limitations under the License. \n # ----------------------------------------------------------------------------\n")
        print("\n   _________.__     .__         __      __                         __      \n  /   _____/|  |__  |__|______ /  \    /  \_______   ____   ____  |  | __  \n  \_____  \ |  |  \ |  |\____ \\   \/\/   /\_  __ \_/ __ \_/ ___\ |  |/ /  \n  /        \|   Y  \|  ||  |_> >\        /  |  | \/\  ___/\  \___ |    <   \n /_______  /|___|  /|__||   __/  \__/\  /   |__|    \___  >\___  >|__|_ \  \n         \/      \/     |__|          \/                \/     \/      \/  \n                                                                          ")


    def log(self, logline, type):
        with open('latest.log', 'a') as file:
            logging = logline + "[" + datetime.strftime("%Y-%m-%d %H:%M:%S") + " "
            if type == "w":
                logline = "WARN]: " + logline + "\n"
            elif type == "d":
                logline = "DEBUG]: " + logline + "\n"
            elif type == "e":
                logline = "ERROR]: Oh mo! looks like you hit a ShipWreck, here is what we know: \n ---------[Begin Error]--------- \n" + logline + "\n ----------[End Error]---------- \n"
            elif type == "n":
                logline = logline
            else:
                logline = "INFO]: " + logline + "\n"
            print(logline)
            file.write(logline)

    def clearlog(self):
        with open('latest.log') as file:
            logline = ""
            file.write(logline)

