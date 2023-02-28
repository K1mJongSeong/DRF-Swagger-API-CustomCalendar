DATABASES = { 
	'default': { 
    	'ENGINE': 'django.db.backends.mysql', 
        'NAME': 'm_calendar', 
        'USER': 'mcalendar', 
        'PASSWORD': 'ekffur3!@#', 
        'HOST': '121.254.171.155', 
        'PORT': '3306',
        'OPTIONS': {
            'init_command': "SET sql_mode='STRICT_TRANS_TABLES'"
        }
     } 
}
SECRET_KEY = 'django-insecure-hjj_l$jk8uj9*%qwov9%d%clh(dmc*$%v%t%a9$1gv_!r3xl40'