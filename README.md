## JakAceh
JakAceh merupakan website yang dikerjakan sebagai tugas akhir pada mata kuliah Proyek Perangkat Lunak. JakAceh merupakan website yang dibuat untuk memudahkan para turis/pelancong melihat informasi seputar budaya di Aceh. JakAceh diharapkan menjadi sarana informasi yang baik, lengkap, serta informatif. 

## Technology we used in this website
- Django 4.0.3
- Bootstrap 5
- MongoDb 5.0.6

## Run
1. Clone Repository
```
git clone https://github.com/ridha-arlian/JakAceh.git
```
2. Install Django with pip
```
pip install django
```
3. Install Djongo Library with pip
```
pip install djongo
```
4. Install Mongo ver. 3.12.3 Library with pip
```
pip install pymongo==3.12.3
```
5. Migration the database
```
python manage.py makemigrations
```
```
python manage.py migrate
```
6. Run the Server
```
python manage.py runserver
```
