import json
import requests
import os
import urllib2
from prettytable import PrettyTable

access_key = "YOUR_IPSTACK_API_ACCESS_KEY"

while True:
    print("""
                  [INVADER$ TOOLS]   [TRACK IP]                    
-----------------------------------------------------------------                       
******   *           *      ******  *    *  *****  *   *       *              
*    *   *          * *     *       *  *    *      *     *   *               
******   *         *   *    *       **      * ***  *       *                          
*    *   *        *******   *       *  *    *      *       *                       
******   ******  *       *  ******  *    *  *      *****   *                          
-----------------------------------------------------------------                        
                  [Created By Rwoxxi & aliēn]           
    """)

    ip_address = input("Bir IP Adresi giriniz: ")


    

    url = f"http://api.ipstack.com/{ip_address}?access_key={access_key}"
    response = requests.get(url)
    data = json.loads(response.text)

    table = PrettyTable()
    table.field_names = ["Attribute", "Value"]
    table.add_row(["IP-Address:", data["ip"]])
    table.add_row(["Sunucu:", data["org"]])
    table.add_row(["Şehir:", data["city"]])
    table.add_row(["Ülke:", data["country_name"]])
    table.add_row(["Bölge:", data["region_name"]])

    print("Sonuç")
    print(table)
    input("Enter tuşuna basın...")


//İkinci Kısım Editledim Burayı 46.cı satırdan sonrası ekleme hata verebilir bakmadım

url = "http://ip-api.com/json/"
load1 = urllib2.urlopen(url)
read1 = load1.read()
result1 = json.loads(read1)
os.system('clear')

while True:
    ip = raw_input("\033[1;36mEnter Your Target IP: \033[1;36m")

    if ip == 'exit':
        break
    else:

        
        #ip-api
        url = "http://ip-api.com/json/"
        load1 = urllib2.urlopen(url + ip)
        read1 = load1.read()
        result1 = json.loads(read1)

   if result1['status'] == 'success':
            # latitude
            lati = result['latitude']
            lat = "{:.4f}".format(lati)
            # longitude
            lon = result['longitude']
            long = "{:.4f}".format(lon)

            # more info
            more = json.dumps(result['location'])

            # printing information
            print ("\n\033[1;33mAll The Information Of IP Is Here \033[1;33m[" + ip + "] :\n")
            print ("\033[1;33mIP: \033[1;33m" + result['ip'])
            print ("\033[1;32mIP Type: \033[1;32m" + result['type'])
            print ("\033[1;34mContinent Name: \033[1;34m" + result['continent_name'])
            print ("\033[1;34mContinent Code: \033[1;34m" + result['continent_code'])
            print ("\033[1;33mCountry: \033[1;33m" + result['country_name'])
            print ("\033[1;33mCountry Code: \033[1;33m" + result1['countryCode'])
            print ("\033[1;32mRegion Name: \033[1;32m" + result['region_name'])
            print ("\033[1;32mRegion Code: \033[1;32m" + result['region_code'])
            print ("\033[1;36mCity: \033[1;36m" + result['city'])
            print ("\033[1;36mZip: \033[1;36m" + result['zip'])
            print ("\033[1;33mTimeZone: \033[1;33m" + result1['timezone'])
            print ("\033[1;33misp: \033[1;33m" + result1['isp'])
	    print ("Do you want to find the exact location with Google Maps?")
	    print ("Then search the Google Map using the Latitude or longitude number")
            print ("\033[1;36mLatitude: \033[1;36m" + lat)
            print ("\033[1;36mlongitude: \033[1;36m" + long)
            print ("\033[1;33mMore Information Of IP \033[1;33m:\n" + more)
            print ("\n\n")
        else:
            print ("\n\033[1;31mSorry, Please Type The IP[" + ip + "] Please try again\033[1;31m\n")

