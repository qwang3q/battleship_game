# Create VM from AWS EC2
- Create a VM following this guide:
   ```https://aws.amazon.com/getting-started/tutorials/launch-a-virtual-machine/```

# Set up network rule
Add InBound Rule in Security groups: "Custom TCP Rule - Port 8000"

# connect to server
- ssh -i .ssh/MyKeyPair.pem ec2-user@{IP_Address}

# Clone repo on Amazon Linux instance
- sudo yum upgrade
- sudo yum install git
- git clone https://github.com/qwang3q/tweetme.git


# Set up virtualenv
- virtualenv tweetme

# install Django 1.11.15
- pip install Django==1.11.15
- pip install djangorestframework
- pip install django-crispy-forms

# run Django server
- python manage.py migrate
- python manage.py runserver

# Set up uwsgi
- sudo yum install gcc gcc-c++ autoconf automake
- pip install uwsgi

# Allow host
- under "tweetme/settings", edit 
   - "base.py"
   - "local.py"
   - "production.py"
- by adding this line:
```ALLOWED_HOSTS = [u'ec2-54-214-186-191.us-west-2.compute.amazonaws.com']```

# Run server:
 uwsgi --http :8000 --module tweetme.wsgi

# Install nginx
sudo yum install nginx

