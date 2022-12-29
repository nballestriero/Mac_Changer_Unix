import subprocess
import optparse
import re


def change_mac(interface, mac):
    print("[+] Changing MAC address for interface: " + interface + " to " + mac)
    # subprocess.run(["ifconfig", interface])
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", mac])
    subprocess.run(["ifconfig", interface, "up"])

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")
    (options, arguments) = parser.parse_args()
    if not options.interface:
        parser.error("[-] Please specify an interface, use --help for more info")
    elif not options.new_mac:
        parser.error("[-] Please specify a new mac, use --help for more info")
    return options

def get_current_mac(interface):
    ifconfig_result = subprocess.check_output(["ifconfig", interface])
    mac_found = re.search(r"\w\w:\w\w:\w\w:\w\w:\w\w:\w\w", str(ifconfig_result))
    if mac_found:
        return mac_found.group(0)
    else:
        print("[-] could not read MAC address.")

def main():
    # Es. codice non sicuro. Usa come input per l'interfaccia eth0;ls;
    # interface = input("interface > ")
    # MAC = input("MAC> ")
    # subprocess.run("ifconfig " + interface, shell=True)

    options = get_arguments()
    current_mac = get_current_mac(options.interface)
    print("Current MAC = " + str(current_mac))
    change_mac(options.interface, options.new_mac)
    current_mac = get_current_mac(options.interface)
    if current_mac == options.new_mac:
        print("[+] MAC address was successfully changed to " + current_mac)
    else:
        print("[-] MAC address did not get changed")


if __name__ == "__main__":
    main()
