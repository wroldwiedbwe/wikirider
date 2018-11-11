WikiRider

Komut istemcisinden direkt bir Wikirun yapabilirsin (Linux veya MacOS kullandigini varsayiyorum).

Kurulum
Debian kullandigim icin, sadece Debian temelli sürümler icin kurulum adimlarini yazdim.

#Repoyu kopyala
git clone git@github.com:sadboyzvone/wikirider.git
#Sanal ortami kur
sudo pip install virtualenv
#Bir adet sanal ortam yarat
cd wikirider && virtualenv .
#Sanal ortami aktive et
source bin/activate
#Gerekli icerigi kur
pip install -r requirements.txt
#Calistir
python main.py

SIKCA SORULAN SORULAR
==> Wikirun nedir?
	https://www.urbandictionary.com/define.php?term=Wikirun
==> Bu, XYZ OS üzerinde calisir mı?
	Eger OS üzerinde python kuruluysa, büyük olasilikla calisacaktir.
