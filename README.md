<p align="center">
  <img src="https://github.com/FedericoJurio/wifiqredentials/blob/master/static/img/router.png?raw=true" alt="Logo" width="128" height="128">
</p>
<h3 align="center">WiFi QRedentials</h3>
<p align="center">Share your WiFi network with your guests via QR!</p>

* [About the Project](#about-the-project)
* [Getting Started](#getting-started)
  * [Prerequisites](#prerequisites)
  * [Installation](#installation)
* [FAQ](#faq)
* [TODO](#todo)
* [Demo](#demo)
* [License](#license)

## About the project
WiFi QRedentials is a web application made with Python and HTML5. My initial motivation was to take a look at [FastAPI](https://fastapi.tiangolo.com/) by implementing a simple feature other than the well known _Hello World_.

## Getting started
These instructions will get you a copy of the project up and running on your local machine for development and testing purposes.

### Prerequisites
1. Python 3.6 or greater
1. virtualenv or your preferred tool to create isolated Python environments

### Installation
1. Clone this repository `git@github.com:FedericoJurio/wifiqredentials.git`
1. Access to the project directory `cd wifiqredentials`
1. Create a virtual environment `virtualenv -p python3 venv`
1. Activate the virtual environment `source venv/bin/activate`
1. Install the requirements `pip install -r requirements.txt`
1. Run the web application `uvicorn main:app`

## FAQ
### How does this work?
ZXing proposed a [standardarized](https://github.com/zxing/zxing/wiki/Barcode-Contents#wi-fi-network-config-android-ios-11) way to connect to WiFi via QR Codes.

### Is ZXing's standard supported by all the phones?
This relies in the bar code scanner but most phones with Android 10/iOS 11 or greater should work.

### Should I use an specific app on my phone?
Android phones usually don't come with a bar code scanner, you can install [Barcode Scanner](https://play.google.com/store/apps/details?id=com.google.zxing.client.android) or [NeoReader](https://play.google.com/store/apps/details?id=de.gavitec.android). OTOH, The iOS Camera App has support for WiFi QR codes since iOS 11.

### Is it safe to put my secrets on the demo instance?
No, never is a good idea to introduce secrets on a site that you can't trust. The app running on Heroku is the same that is on this repository but you can't verify it. If your WiFi password is not unique and you are reusing it for other stuff I'd recommend you to:

1. Don't reuse passwords
1. Run the app locally

## TODO
There's room for improvements such as
* Adding unit tests
* Allowing the user to download the result as a friendly printable PDF
* Allowing the user to display the credentials as text as well in the result
* Adding a go back button in the result's page
* Making password field required for WPA/WPA2/WEP

## Demo
There's a live [demo](http://wifiqredentials.herokuapp.com/) hosted in Heroku.

## License
Distributed under the MIT License. See `LICENSE` for more information.