import json
import requests
import os
from prettytable import PrettyTable

while True:
    os.system("cls" if os.name == "nt" else "clear")  

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

    url = "https://rwoxxi.org/" + input("Bir IP Adresi giriniz: ") 
    response = requests.get(url)
    data = json.loads(response.text)

    table = PrettyTable()
    table.field_names = ["Attribute", "Value"]
    table.add_row(["IP-Address:", data["ip"]])
    table.add_row(["Sunucu:", data["org"]])
    table.add_row(["Şehir:", data["city"]])
    table.add_row(["Ülke:", data["country"]])
    table.add_row(["Bölge:", data["region"]])

    print("Sonuç")
    print(table)
    input("press Enter...")
