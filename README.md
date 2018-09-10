# flask_scrappy
this is base on scrappy that used for vietnam stock market aggregator 

# Engine service
Docker image with uWSGI and Nginx for Flask web applications in Python 3.6, Python 3.5 and Python 2.7 running in a single container. Optionally using Alpine Linux

#General Instruction
please install docker for full running in local machine

<pre>
$ docker version
    Client:
     Version:	17.12.0-ce
     API version:	1.35
     Go version:	go1.9.2
     Git commit:	c97c6d6
     Built:	Wed Dec 27 20:03:51 2017
     OS/Arch:	darwin/amd64

    Server:
     Engine:
      Version:	17.12.0-ce
      API version:	1.35 (minimum version 1.12)
      Go version:	go1.9.2
      Git commit:	c97c6d6
      Built:	Wed Dec 27 20:12:29 2017
      OS/Arch:	linux/amd64
      Experimental:	true
$ docker-compose version
docker-compose version 1.18.0, build 8dd22a9
docker-py version: 2.6.1
CPython version: 2.7.12
OpenSSL version: OpenSSL 1.0.2j  26 Sep 2016
</pre>

#Simple Architecture 

<pre>
+------------------------------- docker container ----------------------------+
+-------------+       +------------+         +--------------+     +-----------+
|             |       |            |         |              |     |           |
|    nginx    +-------+  gunicorn  +---------+      eve     +-----+   mongo   |
|             |       |            |         |              |     |           |
+-------------+       +------------+         +--------------+     +-----------+
+-----------------------------------------------------------------------------+

</pre>

# Quick start
Pull build and up
<pre>
$ git clone  https://github.com/teguh87/flask_scrappy.git
$ cd flask_scrappy
$ docker-compose build
$ docker-compose up -d
</pre>

#stop the service

<pre>
$ docker-compose stop
</pre>


# Endpoint definition
The next thing is a definition of the client endpoint you need restful client such as postmen etc. base url is <pre>http://localhost</pre> It is done in 
<b> Fetch companies </b> <pre> /companies </pre> result must be :

<pre>
"_items": [
        {
            "_id": "5b95b7d6bbbfe362d0bea709",
            "company_website": "www.aquatexbentre.com",
            "company_description": "Processing and exporting aquatic products; breeding aquatic products; importing materials and commodities; trading; operating restaurants; providing services; and other business scopes decided by the Board of Directors and in line with the laws",
            "revenue": "81,000,000,000",
            "company_url": "http://stock.vietnammarkets.com/food-processing/ABT/",
            "industry": "Food processing",
            "business_registration": {
                "established_licence": "Established License: 3423/QD-UB  12-01-2003  Ben Tre Province People's Committee",
                "business_licance": "Business License: 553000010  12-25-2003   Department of Planning and Investment of Ben Tre Province"
            },
            "company_phone_number": "+84 8475860265/+84 8475860346",
            "financial_summary": {
                "listing_volume": "3,300,000",
                "par_value": "10,000",
                "equity": "0",
                "capital_currency": "VND",
                "market_capital": "81,000,000,000",
                "initial_list_price": "90,000"
            },
            "auditing_company": {
                "company_website": "http://www.aisc.com.vn ",
                "company_contact": "Tel: (84.8) 9 305 163 (10 lines) - Fax: (84.8) 9 304 28",
                "company_email": " aisc@aisc.com.vn",
                "company_address": "Address: 142 Nguyen Thi Minh Khai Street - District 3",
                "company_name": "Auditing and Informatic Services Company"
            },
            "company_name": "BEN TRE AQUAPRODUCT IMPORT AND EXPORT JSC",
            "company_address": {
                "province": " Ben Tre Province",
                "street1": "Village 9",
                "street2": " Tan Thach Commune",
                "city": " Chau Thanh District"
            },
            "ticker_symbol": "ABT",
            "company_email": "aquatex@hcm.vnn.vn",
            "_created": "Thu, 01 Jan 1970 00:00:00 GMT",
            "_updated": "Thu, 01 Jan 1970 00:00:00 GMT",
            "_links": {
                "self": {
                    "title": "name",
                    "href": "companies/5b95b7d6bbbfe362d0bea709"
                }
            }
        },
        .......
 </pre>

Try to fetch by company_name soo, you can query by using this query string : <pre>/companies/?where={"company_name": "BEN TRE AQUAPRODUCT IMPORT AND EXPORT JSC"}</pre> so the result should be:

<pre>
    "_items": [
        {
            "_id": "5b95b7d6bbbfe362d0bea709",
            "company_website": "www.aquatexbentre.com",
            "company_description": "Processing and exporting aquatic products; breeding aquatic products; importing materials and commodities; trading; operating restaurants; providing services; and other business scopes decided by the Board of Directors and in line with the laws",
            "revenue": "81,000,000,000",
            "company_url": "http://stock.vietnammarkets.com/food-processing/ABT/",
            "industry": "Food processing",
            "business_registration": {
                "established_licence": "Established License: 3423/QD-UB  12-01-2003  Ben Tre Province People's Committee",
                "business_licance": "Business License: 553000010  12-25-2003   Department of Planning and Investment of Ben Tre Province"
            },
            "company_phone_number": "+84 8475860265/+84 8475860346",
            "financial_summary": {
                "listing_volume": "3,300,000",
                "par_value": "10,000",
                "equity": "0",
                "capital_currency": "VND",
                "market_capital": "81,000,000,000",
                "initial_list_price": "90,000"
            },
            "auditing_company": {
                "company_website": "http://www.aisc.com.vn ",
                "company_contact": "Tel: (84.8) 9 305 163 (10 lines) - Fax: (84.8) 9 304 28",
                "company_email": " aisc@aisc.com.vn",
                "company_address": "Address: 142 Nguyen Thi Minh Khai Street - District 3",
                "company_name": "Auditing and Informatic Services Company"
            },
            "company_name": "BEN TRE AQUAPRODUCT IMPORT AND EXPORT JSC",
            "company_address": {
                "province": " Ben Tre Province",
                "street1": "Village 9",
                "street2": " Tan Thach Commune",
                "city": " Chau Thanh District"
            },
            "ticker_symbol": "ABT",
            "company_email": "aquatex@hcm.vnn.vn",
            "_created": "Thu, 01 Jan 1970 00:00:00 GMT",
            "_updated": "Thu, 01 Jan 1970 00:00:00 GMT",
            "_links": {
                "self": {
                    "title": "name",
                    "href": "companies/5b95b7d6bbbfe362d0bea709"
                }
            }
        }
    ],
    ...
</pre>


Try to fetch by industry soo, you can query by using this query string :
<pre>/companies/?where={"industry": "Food processing"}</pre> so the result should be:

<pre>
     "_items": [
        {
            "_id": "5b95b7d6bbbfe362d0bea709",
            "company_website": "www.aquatexbentre.com",
            "company_description": "Processing and exporting aquatic products; breeding aquatic products; importing materials and commodities; trading; operating restaurants; providing services; and other business scopes decided by the Board of Directors and in line with the laws",
            "revenue": "81,000,000,000",
            "company_url": "http://stock.vietnammarkets.com/food-processing/ABT/",
            "industry": "Food processing",
            "business_registration": {
                "established_licence": "Established License: 3423/QD-UB  12-01-2003  Ben Tre Province People's Committee",
                "business_licance": "Business License: 553000010  12-25-2003   Department of Planning and Investment of Ben Tre Province"
            },
            "company_phone_number": "+84 8475860265/+84 8475860346",
            "financial_summary": {
                "listing_volume": "3,300,000",
                "par_value": "10,000",
                "equity": "0",
                "capital_currency": "VND",
                "market_capital": "81,000,000,000",
                "initial_list_price": "90,000"
            },
            "auditing_company": {
                "company_website": "http://www.aisc.com.vn ",
                "company_contact": "Tel: (84.8) 9 305 163 (10 lines) - Fax: (84.8) 9 304 28",
                "company_email": " aisc@aisc.com.vn",
                "company_address": "Address: 142 Nguyen Thi Minh Khai Street - District 3",
                "company_name": "Auditing and Informatic Services Company"
            },
            "company_name": "BEN TRE AQUAPRODUCT IMPORT AND EXPORT JSC",
            "company_address": {
                "province": " Ben Tre Province",
                "street1": "Village 9",
                "street2": " Tan Thach Commune",
                "city": " Chau Thanh District"
            },
            "ticker_symbol": "ABT",
            "company_email": "aquatex@hcm.vnn.vn",
            "_created": "Thu, 01 Jan 1970 00:00:00 GMT",
            "_updated": "Thu, 01 Jan 1970 00:00:00 GMT",
            "_links": {
                "self": {
                    "title": "name",
                    "href": "companies/5b95b7d6bbbfe362d0bea709"
                }
            }
        },
        ...
</pre>

Try to fetch by grether then  soo, you can query by using this query string :
<pre>/companies/?where={"revenue': {'$gt": "83,000,000,000"}}</pre> so the result should be:

<pre>
     "_items": [
        {
            "_id": "5b95b7d6bbbfe362d0bea713",
            "company_website": "www.ximangbimson.com.vn",
            "company_description": "Manufacturing, trading, exporting and importing cement, clinker and other construction materials",
            "revenue": "900,000,000,000",
            "company_url": "http://stock.vietnammarkets.com/construction-materials/BCC/",
            "industry": "Construction materials",
            "business_registration": {
                "established_licence": "Established License: 366/BXD-TCLD  08-12-1993  Ministry of Construction",
                "business_licance": "Business License: 20603000429  05-01-2006   Planning and Investment Department of Thanh Hoa Province"
            },
            "company_phone_number": "+84 8437824242/+84 8437824046",
            "financial_summary": {
                "listing_volume": "90,000,000",
                "par_value": "10,000",
                "equity": "0",
                "capital_currency": "VND",
                "market_capital": "900,000,000,000",
                "initial_list_price": "0"
            },
            "auditing_company": {
                "company_website": "http:",
                "company_contact": "Tel: (84-4) 826 8681 - Fax: (84-4) 825 3973",
                "company_email": "",
                "company_address": "Address: 01 Le Phung Hieu Street - Hanoi",
                "company_name": "Accounting and Auditing Financial Consultancy Service Company (AASC)"
            },
            "company_name": "BIM SON CEMENT JOINT STOCK COMPANY",
            "company_address": {
                "province": "",
                "street1": "Ba Dinh Ward",
                "street2": " Bim Son Town",
                "city": " Thanh Hoa Privince"
            },
            "ticker_symbol": "BCC",
            "company_email": "ttximangbimson@hn.vnn.vn",
            "_created": "Thu, 01 Jan 1970 00:00:00 GMT",
            "_updated": "Thu, 01 Jan 1970 00:00:00 GMT",
            "_links": {
                "self": {
                    "title": "name",
                    "href": "companies/5b95b7d6bbbfe362d0bea713"
                }
            }
        },
</pre>
