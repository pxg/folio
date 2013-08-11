## Instructions

To build the static site:
 - First run the django site `python mange.py runserver`
 - `cd scripts`
 - ./build_static.sh

The static site files will now be in 'publish/127.0.0.1:8000'. You can test they are ok:
 - `cd publish/127.0.0.1:8000`
 - `python -m SimpleHTTPServer 8888`

 Now push them to s3 with Boto:



TODO:
 - boto script to publish to s3
 - publish button (calls unified script)

 - fix title styling
 - order content
 - add more content
 - edit general text in site (key/value or flat pages)

################################################################################

 - alt text on images
 - Lightbox bigger images
 - host CMS on server
 - sitemap.xml

REFACTOR:
 - remove need to collect static?
 - review if we require wget alternatives (https://github.com/timetric/django-staticgenerator, https://github.com/koenbok/Cactus, https://pypi.python.org/pypi/staticgenerator)
