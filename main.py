import subprocess
import optparse


def change_mac(interface, mac):
    print("[+] Changing MAC address for interface: " + interface + " to" + mac)
    # subprocess.run(["ifconfig", interface])
    subprocess.run(["ifconfig", interface, "down"])
    subprocess.run(["ifconfig", interface, "hw", "ether", mac])
    subprocess.run(["ifconfig", interface, "up"])

def get_arguments():
    parser = optparse.OptionParser()
    parser.add_option("-i", "--interface", dest="interface", help="Interface to change its MAC Address")
    parser.add_option("-m", "--mac", dest="new_mac", help="New MAC address")

    return parser.parse_args()

def main():
    # Es. codice non sicuro. Usa come input per l'interfaccia eth0;ls;
    # interface = input("interface > ")
    # MAC = input("MAC> ")
    # subprocess.run("ifconfig " + interface, shell=True)

    (options, arguments) = get_arguments()
    change_mac(options.interface, options.new_mac)


if __name__ == "__main__":
    main()
