import ipaddress
def ipv4addr(ip):
    '''
    This Function takes user ip address input and determines what class network the ip address is. 
    And based on that information they are given a list of available hosts, private address range and default subnet mask for the address provided.
    '''
    classA= ' is a Class A IP v4 address. The Class A network first octet range is from 0 to 127. Class A private address range is 10.0.0.0 to 10.255.255.255.'
    classB= ' is a Class B IP v4 address. The Class B network first octet range is from 128 to 191. Class B private address range is 172.16.0.0 to 172.31.255.255. Additionally, there is the APIPA address range which is 169.254.0.1 through 169.254.255.254. This is for windows systems that are configured for DHCP without a server. These networks usually only have a few hosts on them. No more than 25 to 30.'
    classC= ' is a Class C IP v4 address. The Class C network first octet range is from 192 to 223. Class C private address range is 192.168.0.0 to 192.168.255.255.'
    classD= ' is a Class D IP v4 address. These addresses are used for multicast traffic and not available for hosts. Class D networks first octet range is from 224 to 239.'
    classE= ' is a Class E IP v4 address. These addresses are reserved for future use and are not available for private or public use.  Class E networks first octet range is from 240 to 255.'
    subnetA = ' Default subnet mask is 255.0.0.0. Available subnet masks for this address are from 255.0.0.0 to 255.255.255.255(This is for a point to point connection).'
    subnetB = ' Default subnet mask is 255.255.0.0. Available subnet masks for this address are from 255.255.0.0 to 255.255.255.255(This is for a point to point connection).'
    subnetC = ' Default subnet mask is 255.255.255.0. Available subnet masks for this address are from 255.255.255.0 to 255.255.255.255(This is for a point to point connection).'
    subnetD = ' Default subnet mask for Class D networks is 255.255.255.255.'
    subnetE = ' Default subnet mask for Class E networks is 255.255.255.255.'
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
        if int(x) in range(0,256):
            if len(x) < 4:
                if int(x) in range(0, 128):
                    return ip + classA + subnetA 
                elif int(x) in range(128, 192):
                    return ip +  classB + subnetB
                elif int(x) in range(192, 224):
                    return ip +  classC + subnetC
                elif int(x) in range(224, 240):
                    return ip + classD + subnetD
                elif int(x) in range(240, 256):
                    return ip + classE + subnetE
            else:
                return 'This is not a valid IP v4 address.'
      
def subnetting(subnet):
    #This determines if a given subnetmask is valid.
    subnetlist = subnet.split('.')
    num=''
    for octet in subnetlist:
        x = bin(int(octet))
        num +=str(x[2::1])
    global cidr 
    cidr= num.count('1')

    if subnetlist[0] =='255':
        if subnetlist[1] == '0' or subnetlist[1] =='128' or subnetlist[1]=='192' or subnetlist[1]=='224' or subnetlist[1] == '240' or subnetlist[1] =='248' or subnetlist[1]=='252' or subnetlist[1] =='254' or subnetlist[1] =='255':
            if subnetlist[2] == '0' or subnetlist[2] =='128' or subnetlist[2]=='192' or subnetlist[2]=='224' or subnetlist[2] == '240' or subnetlist[2] =='248' or subnetlist[2]=='252' or subnetlist[2] =='254' or subnetlist[2] =='255':
                if subnetlist[3] == '0' or subnetlist[3] =='128' or subnetlist[3]=='192' or subnetlist[3]=='224' or subnetlist[3] == '240' or subnetlist[3] =='248' or subnetlist[3]=='252' or subnetlist[3] =='254' or subnetlist[3] =='255':
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
    global hostrng
    hostrng = []
    testfile = open('testfile.txt', "w")
    for ip in ipaddress.ip_network(net_id):
        hostrng.append(str(ip))
    iplist.write('Here are your available hosts: '+ str(hostrng[1:-1]))
    return 'You have '+ str(len(hostrng[1:-1])) +' host ip addresses available on this subnet. \nThe first useable host ip address is ' + hostrng[1] + '. \nThe last useable host ip address is ' + hostrng[-2] + '. \nYour broadcast IP address is ' + str(hostrng[-1]) + '.'

ip=input('What is your IP v4 address? ')
subnet=input('What is your subnet mask? ')
print(ipv4addr(ip))
print(subnetting(subnet)) 
print(network_id(ip, str(cidr)))
print(hostrange(ip, net_id))  
