import json
import requests
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
