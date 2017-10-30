# WikiRider
##
Do a Wikirun directly from your terminal ( assuming you use Linux or Mac )!<br />
[![Travis](https://img.shields.io/travis/sadboyzvone/wikirider.svg)]()
[![Known Vulnerabilities](https://snyk.io/test/github/sadboyzvone/wikirider/badge.svg)](https://snyk.io/test/github/sadboyzvone/wikirider)
[![Code Climate](https://img.shields.io/codeclimate/coverage/github/sadboyzvone/wikirider.svg)]()
## Install
Since I use Debian, I can only provide instructions for Debian-based distros.
```bash
# Clone the repo
git clone git@github.com:sadboyzvone/wikirider.git
# Install virtualenv
sudo pip install virtualenv
# Create a virtualenv
cd wikirider && virtualenv .
# Activate virtualenv
source bin/activate
# Install requirements
pip install -r requirements.txt
# Run
python wikirider.py
```
## FAQ:
* What is a Wikirun?
	* [This](http://www.urbandictionary.com/define.php?term=Wikirun)
* Does it work on XYZ OS?
	* If you have Python on it, it probably will
