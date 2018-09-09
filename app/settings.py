SERVER_NAME = None
SECRET_KEY = 'asaad2ewewe0ds.sds'
DEBUG = True

DOMAIN = {
    'companies': {
        # We choose to override global cache-control directives for this resource.
        'cache_control': 'max-age=10,must-revalidate',
        'cache_expires': 10,
        # 'title' tag used in item links. Defaults to the resource title minus
        # the final, plural 's' (works fine in most cases but not for 'name')
        'item_title': 'name',

        # by default the standard item entry point is defined as
        # '/companies/<ObjectId>'. We leave it untouched, and we also enable an
        # additional read-only entry point. This way consumers can also perform
        # GET requests at '/company/<company_name>'.
        'additional_lookup': {
            'url': 'regex("[\w]+")',
            'field': 'company_name'
        },
        # most global settings can be overridden at resource level
        'resource_methods': ['GET', 'POST'],
        'schema': {
            'company_name': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 200,
            },
            'company_url': {
                'type': 'string',
                'minlength': 1,
                'maxlength': 200,
            },
            'industry':{
                'type': 'string'
            },
            'ticker_symbol': {
                'type': 'string'
            },
            'company_address': {
                'type': 'dict',
                'schema': {
                    'street1': {
                        'type' : 'string'
                    },
                    'street2': {
                        'type' : 'string'
                    },
                    'city': {
                        'type' : 'string'
                    },
                    'province': {
                        'type' : 'string'
                    }
                },  
            },
            'company_email': {
                'type': 'string'
            },
            'company_website': {
                'type': 'string'
            },
            'company_phone_number': {
                'type': 'string'
            },
            'revenue': {
                'type': 'string'
            },
            'financial_summary': {
                'type': 'dict',
                'schema': {
                    'capital_currency': {
                        'type': 'string'
                    },
                    'market_capital': {
                        'type': 'string'
                    },
                    'par_value': {
                        'type': 'string'
                    },
                    'equity': {
                        'type': 'string'
                    },
                    'equity': {
                        'type': 'string'
                    },
                    'listing_volume': {
                        'type': 'string'
                    },
                    'initial_list_price': {
                        'type': 'string'
                    }
                }
            },
            'company_description': {
                'type': 'string'
            },
            'auditing_company': {
                'type': 'dict',
                'schema': {
                    'company_name': {
                        'type': 'string'
                    },
                    'company_address': {
                        'type': 'string'
                    },
                    'company_contact': {
                        'type': 'string'
                    },
                    'company_website': {
                        'type': 'string'
                    },
                    'company_email': {
                        'type': 'string'
                    }
                }
            },
            'business_registration': {
                'type' : 'dict',
                'schema': {
                    'established_licence': {
                        'type': 'string',
                    },
                    'business_licance': {
                        'type': 'string'
                    }
                }
            }
        }
    }
}

#Mongo setup
MONGO_HOST = 'mongo'
MONGO_PORT = 27017
MONGO_DBNAME   = 'qomm'
IF_MATCH  = False

#Enable reads (GET), inserts (POST) and delete (DELETE) for resource collection
#If you omit this line,  the API will default to ['GET'] and provide
#Read Only access to the endpoint
RESOURCE_METHODS = ['GET', 'POST']

#Enable reads (GET), edit (PATCH) or (PUT) and delete for item resource
#(default to read only-items access)
ITEM_METHODS = ['GET', 'PATCH', 'DELETE', 'PUT']

#Enable standard client cache directive for all resource exposed by the
#API. And Always override these global setting letter
CACHE_CONTROL = 'max-age=20'
CACHE_EXPIRED = 20