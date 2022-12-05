import os
import features.environment


def getEnvironment():
    if features.environment.Environment is not None:
        Environment = features.environment.Environment
        return Environment
    else:
        return "Staging"


class Configuration:
    Environment = "Staging"

    basedir = os.path.abspath(os.path.join(__file__, "../.."))
    DateFormat = '%d/%m/%Y'
    HourFormat = "%H%M%S"

    devices_resources = basedir + u"/resources/devices/"

    if Environment == 'Staging':
        app = basedir + u'/resources/binaries/app-release-4_1_2.apk'
        device = "pixel_xl"
        port = 4723
        local = f"http://localhost/wd/hub"

    if Environment == 'Select':
        app = basedir + u'/resources/binaries/select-app-release-4_1_2.apk'
        device = "pixel_xl"
        port = 5001
        local = f"http://localhost/wd/hub"
