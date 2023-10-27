import subprocess
import optparse     #TODO   BU KÜTÜPHANE tooollarda bulunan --help --version -command gibi yazgıları kullanmamızı sağlıyor 

def get_arguments():
    parser = optparse.OptionParser()
    #! OPTİON MENU OLUSTURUP DEĞİŞKENE ATMIŞ OLUYORUZ -H VE --HELP KOMUTU DEFAULT OLARAK MEVCUT


    #TODO  -H GİBİ OLUCAK YARDIM MENULERI EKLİYORUZ
    parser.add_option("-i","--interface",dest="interface",help="Interface şu şu işe yarar")
    parser.add_option("-m","--mac",dest="new_mac",help="New MAC adress") 
    (options,arguments) = parser.parse_args()

    if not options.interface:
        parser.error("[-] Please specify an interface,use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify an new mac,use --help for more info")
        #* eski usül excepition handling


    return options #Yazılan option veya  parser üstünden yazılan dahili seçenekleri etkin eder 

def change_mac(interface,new_mac):
    print("[+] Changing mac adress for "+interface+" to "+new_mac)
    subprocess.call("ifconfig "+interface+ " down",shell=True) 
            
        #todo ifconfig wlan0 down linux işletim sisteminde mac adresimizi kapatır

    subprocess.call("ifconfig "+interface+ " hw ether "+new_mac,shell=True)

        #todo Mac adresimizi değiştirme komutu bu sayılar istediğimiz gibi olabilir sadece 12 tane olması şart

    subprocess.call("ifconfig "+interface+ " up",shell=True) 

        #todo Tekrardan aktif ediyoruz


options = get_arguments()

change_mac(options.interface,options.new_mac)




#? EXAMPLE ==> python3 macAdressChanger.py -i eth0 -m 00:22:33:44:55:66