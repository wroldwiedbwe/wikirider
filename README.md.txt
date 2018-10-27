WikiRider

Komut istemcisinden direkt bir Wikirun yapabilirsin (Linux veya MacOS kullandýðýný varsayýyorum).

Kurulum
Debian kullandýðým için, sadece Debian temelli sürümler için kurulum adýmlarýný yazdým.

#Repoyu kopyala
git clone git@github.com:sadboyzvone/wikirider.git
#Sanal ortamý kur
sudo pip install virtualenv
#Bir adet sanal ortam yarat
cd wikirider && virtualenv .
#Sanal ortamý aktive et
source bin/activate
#Gerekli içeriði kur
pip install -r requirements.txt
#Çalýþtýr
python main.py

SIKÇA SORULAN SORULAR
==> Wikirun nedir?
	https://www.urbandictionary.com/define.php?term=Wikirun
==> Bu, XYZ OS üzerinde çalýþýr mý?
	Eðer OS üzerinde python kuruluysa, büyük olasýlýkla çalýþacaktýr.