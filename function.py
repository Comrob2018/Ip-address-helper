import ipaddress

'''
This script takes user input for Ip v4 address and subnet mask. 
The provided input then returns information for the class, available hosts in subnet, 
subnet id, and CIDR notation.
It also checks the ip address and subnet mask for validity.
'''

def ipv4addr(ip):
    '''
    This Function takes user ip address input and determines what class network the ip address is, 
    and gives the user inforamtion about the network class and private address range for the 
    address provided.
    '''
    classA= ' is a Class A IP v4 address. Class A private address range is 10.0.0.0 to 10.255.255.255.'
    classB= ' is a Class B IP v4 address. Class B private address range is 172.16.0.0 to 172.31.255.255. Additionally, there is the APIPA address range which is 169.254.0.1 through 169.254.255.254.'
    classC= ' is a Class C IP v4 address. Class C private address range is 192.168.0.0 to 192.168.255.255.'
    classD= ' is a Class D IP v4 address. These addresses are used for multicast traffic and not available for hosts.'
    classE= ' is a Class E IP v4 address.These addresses are reserved for future use and are not available for private or public use.'
    
    iplst = ip.split('.')
    for x in iplst:
        realip = '.'.join(iplst)
        while True:
            try:
                ipaddress.ip_address(realip)
                break
            except ValueError:
                return 'This is not a valid IP v4 address.'
               
    for x in iplst:
        if int(x) in range(0,255):
            if len(x) < 4:
                if int(x) in range(0, 128):
                    return ip + classA 
                elif int(x) in range(128, 192):
                    return ip +  classB 
                elif int(x) in range(192, 224):
                    return ip +  classC 
                elif int(x) in range(224, 240):
                    return ip + classD
                elif int(x) in range(240, 255):
                    return ip + classE
            else:
                return 'This is not a valid IP v4 address.'
            

def subnetting(subnet):
    #This function determines if the subnet mask is valid.
    subnetcheck = ['0','128','192','224','240','248','252','254','255']
    subnetlist = subnet.split('.')
    num=''
    for octet in subnetlist:
        x = bin(int(octet))
        num +=str(x[2::1])
    global cidr
    cidr= num.count('1')
    if subnetlist[0] == '255':
        if subnetlist[1] in subnetcheck:
            if subnetlist[2] in subnetcheck:
                if subnetlist[3] in subnetcheck:
                    return 'Your CIDR notation is /' + str(cidr) + '.'
                else:
                    return 'This is not a valid subnet mask.'
            else:
                return 'This is not a valid subnet mask.'
        else:
            return 'This is not a valid subnet mask.'
    else:
        return 'This is not a valid subnet mask.'


def network_id(ip, cidr):
    #This returns the subnet id when given the ip address and the cidr notation.
    x = ip + '/' + cidr
    global net_id
    net_id = ipaddress.ip_network(x, strict=False)
    return 'Your subnet id is ' + str(net_id) + '.'

def hostrange(ip, net_id):
    #This is to return the host ip address range for the ip address and network id provided.
    #It also outputs all available host addressess to a file. 
    global hostrng
    hostrng = []
    iplist = open('iplist.txt', "w")
    for ip in ipaddress.ip_network(net_id):
        hostrng.append(str(ip))
    iplist.write('Here are your available hosts: '+ str(hostrng[1:-1]))
    return 'There are '+ str(len(hostrng[1:-1])) +' host ip addresses available on this subnet. \nThe first useable host ip address is ' + hostrng[1] + '. \nThe last useable host ip address is ' + hostrng[-2] + '. \nYour broadcast IP address is ' + str(hostrng[-1]) + '.'

ip=raw_input('What is your IP v4 address? ')
subnet=raw_input('What is your subnet mask? ')
print(ipv4addr(ip))
print(subnetting(subnet))
print(network_id(ip, str(cidr)))
print(hostrange(ip, net_id))
