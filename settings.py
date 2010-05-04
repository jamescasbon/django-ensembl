DEBUG = True

DATABASES = {
    'default':  {
        'ENGINE': 'sqlite3',
        'NAME': 'testdb.sqlite'
    },
    'ensembl.core': {
        'ENGINE': 'mysql',
        'NAME': 'homo_sapiens_core_56_37a',
        'TEST_NAME': 'homo_sapiens_core_56_37a',
        'USER': 'anonymous',
        'HOST': 'ensembldb.ensembl.org',
        'PORT': '5306'
    },
    'ensembl.variation': {
        'ENGINE': 'mysql',
        'NAME': 'homo_sapiens_variation_56_37a',
        'USER': 'anonymous',
        'HOST': 'ensembldb.ensembl.org',
        'PORT': '5306'
    }
}

DATABASE_ROUTERS = ['ensembl.core.routers.CoreRouter', 'ensembl.variation.routers.VariationRouter']
INSTALLED_APPS = ['django_extensions', 'browser']
