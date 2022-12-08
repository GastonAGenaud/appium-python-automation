# Mobile testing 
## Python, Behave &amp; Appium (Instagram Example)

This is example how to run appium on local machine to set up Instagram application for Android.
Example is based on BDD Test Scenario (Successful Login).

#### How to run:
1. Go to project root folder "MobileTestingWithAppium"
2. Add credential from instagram account to config file (/features/credentials.py)
3. Update desired capabilities for Android (/features/environment.py)
4. Execute command: "behave"

#### Result:
https://www.youtube.com/watch?v=nb2MnwL9Cps

#### Environment:
- macOS Mojave 
- Python 3.7.2 
- appium 1.16.0
- device Android 6.0 x86

#### Useful links:
- https://www.swtestacademy.com/how-to-install-appium-on-mac/
- https://automated-testing.info/t/mobilnaya-avtomatizacziya-s-appium-opyt-napisaniya-pervogo-testa/17221
- https://www.youtube.com/watch?v=jnKd6PRhmDY



### Automating lights by people detection through classifier

Check out <a href="https://medium.com/softway-blog/automating-lights-with-computer-vision-nodejs-fb9b614b75b2"><b>Automating lights with Computer Vision & NodeJS</b></a>.

![user-presence](https://user-images.githubusercontent.com/34403479/70385871-8d62e680-19b7-11ea-855c-3b2febfdbd72.png)

<a name="how-to-install"></a>

# How to install

``` bash
npm install --save opencv4nodejs
```

Native node modules are built via node-gyp, which already comes with npm by default. However, node-gyp requires you to have python installed. If you are running into node-gyp specific issues have a look at known issues with [node-gyp](https://github.com/nodejs/node-gyp) first.

**Important note:** node-gyp won't handle whitespaces properly, thus make sure, that the path to your project directory does **not contain any whitespaces**. Installing opencv4nodejs under "C:\Program Files\some_dir" or similar will not work and will fail with: "fatal error C1083: Cannot open include file: 'opencv2/core.hpp'"!**

On Windows you will furthermore need Windows Build Tools to compile OpenCV and opencv4nodejs. If you don't have Visual Studio or Windows Build Tools installed, you can easily install the VS2015 build tools:

``` bash
npm install --global windows-build-tools
```

## Installing OpenCV Manually

Setting up OpenCV on your own will require you to set an environment variable to prevent the auto build script to run:

``` bash
# linux and osx:
export OPENCV4NODEJS_DISABLE_AUTOBUILD=1
# on windows:
set OPENCV4NODEJS_DISABLE_AUTOBUILD=1
```

### Windows

You can install any of the OpenCV 3 or OpenCV 4 <a href="https://github.com/opencv/opencv/releases/"><b>releases</b></a> manually or via the [Chocolatey](https://chocolatey.org/) package manager:

``` bash
# to install OpenCV 4.1.0
choco install OpenCV -y -version 4.1.0
```

Note, this will come without contrib modules. To install OpenCV under windows with contrib modules you have to build the library from source or you can use the auto build script.

Before installing opencv4nodejs with an own installation of OpenCV you need to expose the following environment variables:
- *OPENCV_INCLUDE_DIR* pointing to the directory with the subfolder *opencv2* containing the header files
- *OPENCV_LIB_DIR* pointing to the lib directory containing the OpenCV .lib files

Also you will need to add the OpenCV binaries to your system path:
- add an environment variable *OPENCV_BIN_DIR* pointing to the binary directory containing the OpenCV .dll files
- append `;%OPENCV_BIN_DIR%;` to your system path variable

Note: Restart your current console session after making changes to your environment.

### MacOSX

Under OSX we can simply install OpenCV via brew:

``` bash
brew update
brew install opencv@4
brew link --force opencv@4
```

### Linux

Under Linux we have to build OpenCV from source manually or using the auto build script.

## Installing OpenCV via Auto Build Script

The auto build script comes in form of the [opencv-build](https://github.com/justadudewhohacks/npm-opencv-build) npm package, which will run by default when installing opencv4nodejs. The script requires you to have git and a recent version of cmake installed.

### Auto Build Flags

You can customize the autobuild flags using *OPENCV4NODEJS_AUTOBUILD_FLAGS=<flags>*.
Flags must be space-separated.

This is an advanced customization and you should have knowledge regarding the OpenCV compilation flags. Flags added by default are listed [here](https://github.com/justadudewhohacks/npm-opencv-build/blob/master/src/constants.ts#L44-L82).

### Installing a Specific Version of OpenCV

You can specify the Version of OpenCV you want to install via the script by setting an environment variable:
`export OPENCV4NODEJS_AUTOBUILD_OPENCV_VERSION=4.1.0`

### Installing only a Subset of OpenCV modules

If you only want to build a subset of the OpenCV modules you can pass the *-DBUILD_LIST* cmake flag via the *OPENCV4NODEJS_AUTOBUILD_FLAGS* environment variable. For example `export OPENCV4NODEJS_AUTOBUILD_FLAGS=-DBUILD_LIST=dnn` will build only modules required for `dnn` and reduces the size and compilation time of the OpenCV package.

## Configuring Environments via package.json

It's possible to specify build environment variables by inserting them into the `package.json` as follows:

```json
{
  "name": "my-project",
  "version": "0.0.0",
  "dependencies": {
    "opencv4nodejs": "^X.X.X"
  },
  "opencv4nodejs": {
    "disableAutoBuild": 1,
    "opencvIncludeDir": "C:\\tools\\opencv\\build\\include",
    "opencvLibDir": "C:\\tools\\opencv\\build\\x64\\vc14\\lib",
    "opencvBinDir": "C:\\tools\\opencv\\build\\x64\\vc14\\bin"
  }
}
```

The following environment variables can be passed:

- autoBuildBuildCuda
- autoBuildFlags
- autoBuildOpencvVersion
- autoBuildWithoutContrib
- disableAutoBuild
- opencvIncludeDir
- opencvLibDir
- opencvBinDir

<a name="usage-with-docker"></a>

# Usage with Docker

### [opencv-express](https://github.com/justadudewhohacks/opencv-express) - example for opencv4nodejs with express.js and docker

Or simply pull from [justadudewhohacks/opencv-nodejs](https://hub.docker.com/r/justadudewhohacks/opencv-nodejs/) for opencv-3.2 + contrib-3.2 with opencv4nodejs globally installed:

``` docker
FROM justadudewhohacks/opencv-nodejs
```

**Note**: The aforementioned Docker image already has ```opencv4nodejs``` installed globally. In order to prevent build errors during an ```npm install```, your ```package.json``` should not include ```opencv4nodejs```, and instead should include/require the global package either by requiring it by absolute path or setting the ```NODE_PATH``` environment variable to ```/usr/lib/node_modules``` in your Dockerfile and requiring the package as you normally would.

Different OpenCV 3.x base images can be found here: https://hub.docker.com/r/justadudewhohacks/.

<a name="usage-with-electron"></a>

# Usage with Electron

### [opencv-electron](https://github.com/justadudewhohacks/opencv-electron) - example for opencv4nodejs with electron

Add the following script to your package.json:
``` python
"electron-rebuild": "electron-rebuild -w opencv4nodejs"
```

Run the script:
``` bash
$ npm run electron-rebuild
```
