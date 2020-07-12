import requests,time,json,sys
def chance():
 try:
  if cookies1()!=''or set_address().set_address().cookies2()!='':
   cookies1==None
   cookies2==None
 except NameError:
  pass
 url='http://api.guerrillamail.com/ajax.php?f=get_email_address'
 resp=requests.get(url)
 cookies1=resp.cookies
 time.sleep(2)
 data=resp.json()
 emailgu=data['email_addr']
 print('Your new Address : '+emailgu)
class set_address:
 def __init__(self,address,lan):
  self.address=address
  self.lan=address
 def set_address(self):
  try:
   if chance().cookies1!='' or cookies2!='':
    cookies1==None
    cookies2==None
  except NameError:
   pass
  url1="http://api.guerrillamail.com/ajax.php?f=set_email_user&email_user="+self.address+"&lan="+self.lan
  resp1=requests.get(url1)
  cookies2=resp1.cookies
  time.sleep(2)
  data1=resp1.json()
  emailaddress=data1['email_addr']
  print('Your new Address : '+emailaddress)
class check_email:
 def __init__(self,seq):
  self.seq=seq
 def check_email(self):
  try:
   if chance().cookies1==''or set_address().set_address().cookies2=='':
    sys.exit('You Did Not Make Email ... First Create It')
   else:
    if cookies1!='':
     cookiemain=cookies1
    else:
     cookiemain=cookies2
  except NameError:
   pass
  url2="http://api.guerrillamail.com/ajax.php?f=check_email"+str(self.seq)
  resp2=requests.get(url2,cookies=cookiemain)
  time.sleep(2)
  data2=resp2.json()
  checkemail=data2['count']
  if checkemail == '0':
   print('Email Box Is Empty')
  else:
   print('You Have '+checkemail+' New Email')
class get_email_list:
 def __init__(self,offset,seq):
  self.offset=offset
  self.seq=seq
 def get_email_list(self):
  try:
   if chance().cookies1==''or set_address().set_address().cookies2=='':
    sys.exit('You Did Not Make Email ... First Create It')
   else:
    if cookies1!='':
     cookiemain=cookies1
    else:
     cookiemain=cookies2
  except NameError:
   pass
  url3='http://api.guerrillamail.com/ajax.php?f=check_email&offset='+str(self.offset)+'&seq='+str(self.seq)
  resp3=requests.get(url3,cookies=cookiesmain)
  data3=resp3.json()
  print(data3)


