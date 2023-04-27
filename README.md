## How to Setup GeoDjango

To setup geodjango they are varios step you need to go through

- Step 1: <b>Installing Geospatial Libraries</b>
  
  On Debian/Ubuntu, you are advised to install the following packages which will install, 
  directly or by dependency, the required geospatial libraries:
    ```bash
    sudo apt-get install binutils libproj-dev gdal-bin
    ```

- Step 2: <b>Install GEOS API</b>
  
    GEOS stands for Geometry Engine - Open Source, and is a C++ library, ported from the Java Topology Suite.
    ```bash
    sudo apt-get install libgeos++
    ```
- Step 3: <b>Install PROJ.4</b>

    PROJ is a generic coordinate transformation software, that transforms geospatial coordinates from one coordinate reference system (CRS) to another. On Ubuntu the APT package manager is used:

    ```bash
    sudo apt install proj-bin
    ```
- Step 4: <b>Install GDAL API</b>

    GDAL stands for Geospatial Data Abstraction Library, and is a veritable “Swiss army knife” of GIS data functionality.

    ```bash
    sudo apt install gdal-bin
    ```

If you want to use sqlite3 database you will need to install `libsqlite3-mod-spatialite`
```bash
sudo apt install libsqlite3-mod-spatialite
``` 

## Create a Django Project
- Create a virtual environment
    ```bash
    python3 -m venv env
    ```
- activate the virtual environment
    ```bash
    source ./env/bin/activate
    ```
- Install GeoDjango Geodjango is included in the Django installation 
  ```bash
  pip install Django
  ```
- Create project
  ```bash
  django-admin startproject project_name
  ```
## In the `settings.py` file 
update the install apps to

```python
INSTALLED_APPS = [
    ...,
    "django.contrib.staticfiles",
    'django.contrib.gis',  # GeoDjango,
    ...
]
```

Update the databases to 

If you want to use SQLITE 3
```python
DATABASES = {
    'default': {
        "ENGINE": "django.contrib.gis.db.backends.spatialite",
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}
```

- NB: If you are using sqlite database you must run this command one's before you migrate to avoid this error `django.db.utils.OperationalError: error in trigger ISO_metadata_reference_row_id_value_insert: no such column: rowid`
  ```
  python ./manage.py shell -c "import django;django.db.connection.cursor().execute('SELECT InitSpatialMetaData(1);')";
  ```

If you want to use Postgress Database
install `pyscopg2`
```bash
pip install psycopg2-binary
```

```python
DATABASES = {
    'default': {        
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'mydatabase',
        'USER': 'mydatabaseuser',
        'PASSWORD': 'mypassword',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
```

Migrate the database
```bash
python ./manage.py shell -c "import django;django.db.connection.cursor().execute('SELECT InitSpatialMetaData(1);')";
python manage.py migrate
```

Create Superuser
```bash
python manage.py createsuperuser
```

Run Server
```bash
python manage.py runserver
```