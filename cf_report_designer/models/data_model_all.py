# -*- coding: utf-8 -*-
# 康虎软件工作室
# http://www.khcloud.net
# QQ: 360026606
# wechat: 360026606
#--------------------------
#
import os
import sys
import logging
import string
try :
 import simplejson as json
except ImportError :
 import json
 if 64 - 64: i11iIiiIii
from lxml import etree
try :
 import xml . etree . cElementTree as ET
except ImportError :
 import xml . etree . ElementTree as ET
from xml . dom import minidom
if 65 - 65: O0 / iIii1I11I1II1 % OoooooooOO - i1IIi
from odoo . exceptions import AccessError , UserError , ValidationError
from odoo import models , fields , api , _
from Crypto . Cipher import AES
if 73 - 73: II111iiii
IiII1IiiIiI1 = logging . getLogger ( __name__ )
if 40 - 40: oo * OoO0O00
if 2 - 2: ooOO00oOo % oOo0O0Ooo * Ooo00oOo00o . oOoO0oo0OOOo + iiiiIi11i
import os
import sys
import hashlib
import string
import random
import base64
from binascii import b2a_hex , a2b_hex
if 24 - 24: II11iiII / OoOO0ooOOoo0O + o0000oOoOoO0o * i1I1ii1II1iII % oooO0oo0oOOOO
from Crypto import Random
from Crypto . Cipher import AES
if 53 - 53: o0oo0o / Oo + o0oo0o / oooO0oo0oOOOO * OoooooooOO + i1I1ii1II1iII
OOo0oO0oooOoO = ( 'C' )
ooO00oOoo = ( 'FS' )
O0OOo = ( 'O' )
II1Iiii1111i = ( 'F' )
i1IIi11111i = ( 'T' )
o000o0o00o0Oo = ( 'S' )
if 80 - 80: OoooooooOO . oo
OOO0O = ( 't' )
oo0ooO0oOOOOo = ( 'u' )
oO000OoOoo00o = ( 'd' )
iiiI11 = ( 'i' )
OOooO = ( 'o72' )
OOoO00o = ( '0' )
II111iiiiII = ( '1' )
if 63 - 63: oOo0O0Ooo % i1IIi
o0oOo0Ooo0O = b"1234567890123456"
if 81 - 81: oOoO0oo0OOOo * oooO0oo0oOOOO * OoOO0ooOOoo0O - i1I1ii1II1iII - Ooo00oOo00o
def OooO0OO ( ) :
 return '' . join ( OOo0oO0oooOoO + ooO00oOoo + O0OOo + II1Iiii1111i + i1IIi11111i + o000o0o00o0Oo + OOO0O + oo0ooO0oOOOOo + oO000OoOoo00o + iiiI11 + OOooO + OOoO00o + II111iiiiII )
 if 28 - 28: II111iiii
 if 28 - 28: iIii1I11I1II1 - i1IIi
OO = len ( OooO0OO ( ) )
oO0O = lambda OOoO000O0OO : OOoO000O0OO + ( OO - len ( OOoO000O0OO ) % OO ) * chr ( OO - len ( OOoO000O0OO ) % OO )
iiI1IiI = lambda OOoO000O0OO : OOoO000O0OO [ 0 : - ord ( OOoO000O0OO [ - 1 ] ) ]
if 13 - 13: OoO0O00 . i11iIiiIii - iIii1I11I1II1 - oOo0O0Ooo
class ii1I ( object ) :
 def __init__ ( self , key = False , mode = AES . MODE_CBC ) :
  if 76 - 76: O0 / Ooo00oOo00o . oo * o0000oOoOoO0o - II11iiII
  if 76 - 76: i11iIiiIii / iIii1I11I1II1 . oOoO0oo0OOOo % II11iiII / OoooooooOO % iiiiIi11i
  if 75 - 75: i1I1ii1II1iII
  if 97 - 97: i11iIiiIii
  if 32 - 32: OoO0O00 * O0 % iiiiIi11i % o0000oOoOoO0o . oooO0oo0oOOOO
  if 61 - 61: Oo
  if 79 - 79: OoO0O00 + oo - i1I1ii1II1iII
  if 83 - 83: Oo
  if 64 - 64: ooOO00oOo % Oo % i1I1ii1II1iII / oOo0O0Ooo - ooOO00oOo
  if 74 - 74: i1I1ii1II1iII * O0
  if 89 - 89: iiiiIi11i + OoO0O00
  if 3 - 3: i1IIi / oo % OoOO0ooOOoo0O * i11iIiiIii / O0 * OoOO0ooOOoo0O
  if 49 - 49: iiiiIi11i % o0000oOoOoO0o + i1IIi . oo % oOoO0oo0OOOo
  if 48 - 48: OoOO0ooOOoo0O + OoOO0ooOOoo0O / II111iiii / iIii1I11I1II1
  self . key = key or OooO0OO ( )
  self . mode = mode
  self . key = self . key . encode ( 'utf-8' )
  if 20 - 20: Ooo00oOo00o
 @ staticmethod
 def get_machine_code ( ) :
  import uuid
  if 77 - 77: oOo0O0Ooo / OoOO0ooOOoo0O
  return str ( uuid . UUID ( int = uuid . getnode ( ) ) )
  if 98 - 98: iIii1I11I1II1 / i1IIi / i11iIiiIii / Ooo00oOo00o
 @ staticmethod
 def rand_aes_key ( size = 16 , by_base64 = True , chars = string . ascii_uppercase + string . digits ) :
  I1i1I1II = '' . join ( random . choice ( chars ) for _ in range ( size ) )
  if 45 - 45: o0oo0o . oOo0O0Ooo
  if 83 - 83: iiiiIi11i . iIii1I11I1II1 . oOoO0oo0OOOo
  if 31 - 31: o0000oOoOoO0o . o0000oOoOoO0o - Ooo00oOo00o / ooOO00oOo + Oo * oo
  if 63 - 63: o0oo0o % i1IIi / OoooooooOO - OoooooooOO
  if 8 - 8: oOo0O0Ooo
  if 60 - 60: OoOO0ooOOoo0O / OoOO0ooOOoo0O
  return base64 . b64encode ( I1i1I1II ) if by_base64 else I1i1I1II
  if 46 - 46: o0000oOoOoO0o * II11iiII - ooOO00oOo * iiiiIi11i - o0oo0o
  if 83 - 83: OoooooooOO
 def encrypt ( self , text ) :
  text = oO0O ( text ) . encode ( 'utf-8' )
  Iii111II = AES . new ( self . key , self . mode , o0oOo0Ooo0O )
  self . ciphertext = Iii111II . encrypt ( text )
  if 9 - 9: ooOO00oOo
  return base64 . b64encode ( self . ciphertext )
  if 33 - 33: Oo . i1I1ii1II1iII
  if 58 - 58: II11iiII * i11iIiiIii / oOo0O0Ooo % o0oo0o - oOoO0oo0OOOo / iiiiIi11i
 def decrypt ( self , text ) :
  ii11i1 = base64 . b64decode ( text )
  Iii111II = AES . new ( self . key , self . mode , o0oOo0Ooo0O )
  if 29 - 29: oOoO0oo0OOOo % oo + Oo / Ooo00oOo00o + II11iiII * Ooo00oOo00o
  if 42 - 42: o0000oOoOoO0o + iiiiIi11i
  o0O0o0Oo = bytes . decode ( Iii111II . decrypt ( ii11i1 ) )
  return iiI1IiI ( o0O0o0Oo )
  if 16 - 16: O0 - o0oo0o * iIii1I11I1II1 + i1I1ii1II1iII
  if 50 - 50: II111iiii - Oo * oOoO0oo0OOOo / o0oo0o + Ooo00oOo00o
from Crypto import Random
from Crypto . Hash import SHA
from Crypto . Cipher import PKCS1_v1_5 as Cipher_pkcs1_v1_5
from Crypto . Signature import PKCS1_v1_5 as Signature_pkcs1_v1_5
from Crypto . PublicKey import RSA
if 88 - 88: o0000oOoOoO0o / o0oo0o + i1I1ii1II1iII - II111iiii / Oo - oOo0O0Ooo
class IIIIii ( ) :
 if 70 - 70: o0000oOoOoO0o / OoOO0ooOOoo0O . i1I1ii1II1iII % OoO0O00
 if 67 - 67: oOo0O0Ooo * Ooo00oOo00o . oooO0oo0oOOOO - ooOO00oOo * Ooo00oOo00o
 if 46 - 46: II11iiII + oOo0O0Ooo . oo * iiiiIi11i % oooO0oo0oOOOO
 if 86 - 86: oo + o0000oOoOoO0o % i11iIiiIii * iiiiIi11i . Oo * OoOO0ooOOoo0O
 if 44 - 44: iiiiIi11i
 if 88 - 88: o0oo0o % o0000oOoOoO0o . II111iiii
 if 38 - 38: Ooo00oOo00o
 if 57 - 57: O0 / iiiiIi11i * o0oo0o / oOo0O0Ooo . II111iiii
 if 26 - 26: i1I1ii1II1iII
 if 91 - 91: ooOO00oOo . oOoO0oo0OOOo + ooOO00oOo - i1I1ii1II1iII / OoooooooOO
 if 39 - 39: oOoO0oo0OOOo / Oo - II111iiii
 if 98 - 98: oOoO0oo0OOOo / OoOO0ooOOoo0O % iiiiIi11i . oOo0O0Ooo
 if 91 - 91: iiiiIi11i % OoO0O00
 if 64 - 64: OoOO0ooOOoo0O % i1I1ii1II1iII - o0oo0o - iiiiIi11i
 if 31 - 31: OoOO0ooOOoo0O - II111iiii . OoOO0ooOOoo0O
 def __init__ ( self , pri_key = 'pri.pem' , pub_key = 'pub.pem' , key_path = os . path . abspath ( os . path . dirname ( __file__ ) ) ) :
  self . KEY_PRIVATE = pri_key
  self . KEY_PUBLIC = pub_key
  self . KEY_PATH = key_path
  if 18 - 18: Ooo00oOo00o
 def gen_key_pair ( self ) :
  if 98 - 98: i1I1ii1II1iII * i1I1ii1II1iII / i1I1ii1II1iII + OoOO0ooOOoo0O
  ii111111I1iII = Random . new ( ) . read
  if 68 - 68: i1I1ii1II1iII - iIii1I11I1II1 * i11iIiiIii / oOoO0oo0OOOo * o0oo0o
  i1iIi1iIi1i = RSA . generate ( 1024 , ii111111I1iII )
  if 46 - 46: o0oo0o % OoOO0ooOOoo0O + ooOO00oOo . oOo0O0Ooo . ooOO00oOo
  if 96 - 96: OoO0O00
  Ii1I1IIii1II = i1iIi1iIi1i . exportKey ( )
  if 65 - 65: o0000oOoOoO0o . iIii1I11I1II1 / O0 - o0000oOoOoO0o
  with open ( self . KEY_PATH + "/" + self . KEY_PRIVATE , 'w' ) as iii1i1iiiiIi :
   iii1i1iiiiIi . write ( Ii1I1IIii1II )
   if 2 - 2: oo / O0 / Ooo00oOo00o % oOo0O0Ooo % o0000oOoOoO0o
  o0o00OO0 = i1iIi1iIi1i . publickey ( ) . exportKey ( )
  with open ( self . KEY_PATH + "/" + self . KEY_PUBLIC , 'w' ) as iii1i1iiiiIi :
   iii1i1iiiiIi . write ( o0o00OO0 )
   if 7 - 7: II11iiII + o0oo0o + O0
 def decrypt_str ( self , encrypt_text ) :
  if 9 - 9: II111iiii . Ooo00oOo00o - Oo / Ooo00oOo00o
  I11 = self . KEY_PATH + "/" + self . KEY_PUBLIC
  if not os . path . isfile ( I11 ) :
   raise Exception ( "Decrypt key not exist or invalid!" )
   if 66 - 66: i1IIi % i1IIi + oOo0O0Ooo + O0 + ooOO00oOo
  ii111111I1iII = Random . new ( ) . read
  with open ( self . KEY_PATH + "/" + self . KEY_PRIVATE ) as iii1i1iiiiIi :
   o0o = iii1i1iiiiIi . read ( )
   o00 = RSA . importKey ( o0o )
   OooOO000 = Cipher_pkcs1_v1_5 . new ( o00 )
   o0O0o0Oo = OooOO000 . decrypt ( base64 . b64decode ( encrypt_text ) , ii111111I1iII )
   return o0O0o0Oo
   if 97 - 97: oOoO0oo0OOOo + II11iiII / iIii1I11I1II1 / i1I1ii1II1iII
 def encrypt_str ( self , message ) :
  I11 = self . KEY_PATH + "/" + self . KEY_PUBLIC
  if not os . path . isfile ( I11 ) :
   raise Exception ( "Encrypt key not exist or invalid!" )
   if 37 - 37: i1I1ii1II1iII - Oo * iiiiIi11i % i11iIiiIii - o0oo0o
  with open ( I11 ) as iii1i1iiiiIi :
   o0o = iii1i1iiiiIi . read ( )
   o00 = RSA . importKey ( o0o )
   OooOO000 = Cipher_pkcs1_v1_5 . new ( o00 )
   o0oO = base64 . b64encode ( OooOO000 . encrypt ( message ) )
   return o0oO
   if 1 - 1: ooOO00oOo - iiiiIi11i . OoOO0ooOOoo0O . ooOO00oOo / OoO0O00 + OoOO0ooOOoo0O
   if 78 - 78: O0 . iiiiIi11i . II111iiii % II11iiII
   if 49 - 49: o0000oOoOoO0o / ooOO00oOo . II111iiii
   if 68 - 68: i11iIiiIii % oOoO0oo0OOOo + i11iIiiIii
   if 31 - 31: II111iiii . oo
   if 1 - 1: OoO0O00 / Ooo00oOo00o % i1I1ii1II1iII * oooO0oo0oOOOO . i11iIiiIii
   if 2 - 2: oOoO0oo0OOOo * OoOO0ooOOoo0O - iIii1I11I1II1 + oo . iiiiIi11i % i1I1ii1II1iII
   if 92 - 92: i1I1ii1II1iII
   if 25 - 25: OoO0O00 - oo / OoooooooOO / Ooo00oOo00o
   if 12 - 12: oo * i1I1ii1II1iII % i1IIi % iIii1I11I1II1
   if 20 - 20: II11iiII % o0000oOoOoO0o / o0000oOoOoO0o + o0000oOoOoO0o
   if 45 - 45: iiiiIi11i - oooO0oo0oOOOO - OoooooooOO - ooOO00oOo . II111iiii / O0
oo0o00O = "report_"
o00O0OoO = "report_"
i1I = "report_"
if 72 - 72: i1IIi / ooOO00oOo + OoooooooOO - OoO0O00
if 29 - 29: oOoO0oo0OOOo + iiiiIi11i % O0
class I1I11 ( models . Model ) :
 _name = 'cf.cfprint.license'
 _description = u'许可证信息'
 if 34 - 34: oo . II11iiII * oOoO0oo0OOOo + o0oo0o
 mcode = fields . Char ( string = u'机器码' , default = lambda i11111IIIII : ii1I . get_machine_code ( ) , help = u'服务器机器码' )
 license = fields . Binary ( string = u'许可证' , help = u'授权许可证文件，下载后改名为cfprint.lic放到客户端cfprint目录下。' )
 note = fields . Char ( string = u'备注' )
 if 19 - 19: oOo0O0Ooo * i1IIi
 @ api . model
 def create ( self , vals ) :
  vals [ 'mcode' ] = ii111iI1iIi1 = ii1I . get_machine_code ( ) or ''
  return super ( I1I11 , self ) . create ( vals )
  if 78 - 78: ooOO00oOo . II11iiII + ooOO00oOo / OoOO0ooOOoo0O / ooOO00oOo
 @ api . multi
 def write ( self , vals ) :
  vals [ 'mcode' ] = ii111iI1iIi1 = ii1I . get_machine_code ( ) or ''
  return super ( I1I11 , self ) . write ( vals )
  if 54 - 54: oOo0O0Ooo % i1I1ii1II1iII
class IIiII111iiI1I ( models . Model ) :
 _inherit = 'ir.model'
 if 11 - 11: II111iiii * II111iiii % iIii1I11I1II1 * o0oo0o + oOo0O0Ooo / oo
 def name_get ( self ) :
  return [ ( ii1Ii11I . id , '%s(%s)' % ( ii1Ii11I . name , ii1Ii11I . model ) ) for ii1Ii11I in self ]
  if 80 - 80: II111iiii
class O0O ( models . Model ) :
 _name = 'cf.report.define'
 _description = u'报表定义'
 if 1 - 1: II111iiii
 name = fields . Char ( string = u'报表ID' , copy = True , help = u"用一确定报表的唯一ID，只允许英文、数字和下划线。" )
 comment = fields . Char ( string = u'报表中文名称' , copy = True )
 model_id = fields . Many2one ( 'ir.model' , string = u'数据表(model)' , required = True , copy = True , help = u"报表对应的数据表(model)" )
 template_id = fields . Many2one ( 'cf.template' , string = u'报表模板' , copy = True , help = u"该报表使用的打印模板。\n模板如果尚未设计，可以先创建一个模板定义，待生成数据并设计报表模板后再上传到模板库。" )
 company_id = fields . Many2one ( 'res.company' , string = u'所属公司' , default = lambda OOooooO0Oo : OOooooO0Oo . env [ 'res.company' ] . _company_default_get ( '' ) )
 open_print = fields . Boolean ( string = u"是否弹出打印" , default = False )
 use_client_templ = fields . Boolean ( string = u"使用客户端模板" , default = False , help = u"" )
 client_templ_name = fields . Char ( string = u"客户端模板文件名" , help = u"如果设置了使用客户端模板，则在此录入客户端模板路径和文件名" )
 field_ids = fields . One2many ( "cf.report.define.field" , "report_id" , string = u"字段" , help = u"要在报表模板中使用的字段信息" )
 state = fields . Selection ( [ ( 'draft' , u'草稿' ) , ( 'defined' , u'完成报表定义' ) ] , string = u"状态" , default = "draft" )
 note = fields . Text ( string = u"备注" )
 if 91 - 91: Ooo00oOo00o . iIii1I11I1II1 / iiiiIi11i + i1IIi
 _sql_constraints = [
 ( 'uniq_name' , 'unique(name)' , _ ( u'报表名称必须唯一!' ) ) ,
 ]
 if 42 - 42: Oo . Ooo00oOo00o . Oo - oOoO0oo0OOOo
 @ api . model
 def create ( self , vals ) :
  if not vals . get ( "template_id" , False ) :
   i1ii1I1I1 = vals . get ( "name" , False )
   oO = vals . get ( "comment" , False )
   if not i1ii1I1I1 :
    raise ValidationError ( _ ( u"请先指定报表ID！" ) )
   oO0O0o0Oooo = "cf_templ_%s" % ( o00O0OoO , i1ii1I1I1 . replace ( '.' , '_' ) )
   I1Ii1iI1 = self . env [ "cf.template" ] . search ( [ ( 'templ_id' , '=' , oO0O0o0Oooo ) ] , limit = 1 )
   if not I1Ii1iI1 :
    I1Ii1iI1 = self . env [ "cf.template" ] . create ( {
 "templ_id" : oO0O0o0Oooo ,
 "name" : ( oO or oO0O0o0Oooo ) + "打印模板" ,
 "description" : ( oO or oO0O0o0Oooo ) + "打印模板" ,
 } )
   vals [ "template_id" ] = I1Ii1iI1 . id
   if 87 - 87: OoO0O00 . oooO0oo0oOOOO
  return super ( O0O , self ) . create ( vals )
  if 75 - 75: Oo + oOo0O0Ooo + Ooo00oOo00o * OoOO0ooOOoo0O % iiiiIi11i . i1I1ii1II1iII
 @ api . multi
 def unlink ( self ) :
  for oOI1Ii1I1 in self :
   oOI1Ii1I1 . _remove_report ( )
  return super ( O0O , self ) . unlink ( )
  if 28 - 28: O0 * OoO0O00 - II11iiII % iIii1I11I1II1 * o0000oOoOoO0o - i11iIiiIii
 def _get_report_id ( self ) :
  self . ensure_one ( )
  return "%s%s" % ( i1I , self . name )
  if 7 - 7: OoO0O00 + iiiiIi11i - o0oo0o % o0000oOoOoO0o + oOoO0oo0OOOo
 def _get_report_name ( self , with_module = True ) :
  self . ensure_one ( )
  if with_module :
   return "cf_report_designer.%s%s" % ( o00O0OoO , self . name . replace ( '.' , '_' ) )
  else :
   return "%s%s" % ( o00O0OoO , self . name . replace ( '.' , '_' ) )
   if 53 - 53: i1IIi - OoOO0ooOOoo0O . oOo0O0Ooo
 def _get_report_file ( self , with_module = True ) :
  self . ensure_one ( )
  if with_module :
   return "cf_report_designer.%s%s" % ( oo0o00O , self . name . replace ( '.' , '_' ) )
  else :
   return "%s%s" % ( oo0o00O , self . name . replace ( '.' , '_' ) )
   if 39 - 39: II111iiii / Oo + o0oo0o / oOo0O0Ooo
 @ api . one
 def _remove_report ( self ) :
  I1Ii11i = self . _get_report_id ( )
  i1111I1I = self . _get_report_name ( )
  i1i = self . _get_report_file ( )
  if 56 - 56: oOoO0oo0OOOo % O0 - oo
  if 100 - 100: o0000oOoOoO0o - O0 % iiiiIi11i * II11iiII + oo
  self . env [ "ir.model.data" ] . sudo ( ) . search ( [ ( 'name' , '=' , I1Ii11i ) ] ) . unlink ( )
  if 88 - 88: OoooooooOO - ooOO00oOo * O0 * OoooooooOO . OoooooooOO
  I111iI = self . env [ 'ir.actions.report' ] . sudo ( ) . search ( [ ( 'report_name' , '=' , i1111I1I ) ] )
  for oOI1Ii1I1 in I111iI :
   oOI1Ii1I1 . unlink_action ( )
   oOI1Ii1I1 . unlink ( )
   if 56 - 56: oo
   if 54 - 54: o0oo0o / II11iiII . iiiiIi11i % i1I1ii1II1iII
  self . env [ 'ir.ui.view' ] . search ( [ ( 'key' , '=' , i1111I1I ) ] ) . unlink ( )
  if 57 - 57: i11iIiiIii . oOoO0oo0OOOo - o0000oOoOoO0o - iiiiIi11i + oOo0O0Ooo
  if 63 - 63: oOo0O0Ooo * i1I1ii1II1iII
  if 69 - 69: O0 . ooOO00oOo
  if 49 - 49: oo - OoOO0ooOOoo0O
  if 74 - 74: iIii1I11I1II1 * oOoO0oo0OOOo + oOo0O0Ooo / i1IIi / II111iiii . OoO0O00
  if 62 - 62: OoooooooOO * oo
  if 58 - 58: oOo0O0Ooo % Ooo00oOo00o
  if 50 - 50: o0oo0o . Ooo00oOo00o
  if 97 - 97: O0 + oOo0O0Ooo
 def action_retrieve_fields ( self ) :
  if 89 - 89: Ooo00oOo00o + ooOO00oOo * OoOO0ooOOoo0O * o0000oOoOoO0o
  self . env [ "cf.report.define.field" ] . search ( [ ( 'report_id' , '=' , self . id ) ] ) . unlink ( )
  if 37 - 37: OoooooooOO - O0 - Ooo00oOo00o
  if 77 - 77: II11iiII * iIii1I11I1II1
  if 98 - 98: oo % o0000oOoOoO0o * OoooooooOO
  for OoiIIiIi1 in self . model_id . field_id :
   if 74 - 74: i1I1ii1II1iII + Ooo00oOo00o
   oO00O000oO0 = self . env [ 'cf.report.define.field' ] . create ( {
 "report_id" : self . id ,
 "model_id" : OoiIIiIi1 . model_id . id ,
 "field_id" : OoiIIiIi1 . id ,

   } )
   if 79 - 79: OoOO0ooOOoo0O - OoooooooOO - iiiiIi11i - iIii1I11I1II1 * II11iiII
 def action_remove_fields ( self ) :
  self . env [ "cf.report.define.field" ] . search ( [ ( 'report_id' , '=' , self . id ) ] ) . unlink ( )
  if 4 - 4: i11iIiiIii . OoooooooOO / ooOO00oOo % o0oo0o % OoOO0ooOOoo0O * O0
  if 14 - 14: II11iiII / Ooo00oOo00o
 def _make_report_defind ( self ) :
  I1Ii11i = self . _get_report_id ( )
  if 32 - 32: oo * OoO0O00
  i1111I1I = self . _get_report_name ( )
  i1i = self . _get_report_file ( )
  if 78 - 78: II11iiII - OoooooooOO - oOoO0oo0OOOo / Oo / II111iiii
  if 29 - 29: oo % oo
  Oo0O0 = self . env [ 'ir.actions.report' ]
  Ooo0OOoOoO0 = Oo0O0 . create ( {
 "name" : self . comment or self . name ,
 "type" : "ir.actions.report" ,
 "binding_type" : "report" ,
 "model" : self . model_id . model ,
 "report_type" : "qweb-html" ,
 "report_name" : i1111I1I ,
 "report_file" : i1i ,
  "multi" : False ,
 "print_report_name" : self . comment or self . name ,
  "attachment_use" : False ,
 "cf_report_define_id" : self . id ,
 } )
  if Ooo0OOoOoO0 :
   self . env [ "ir.model.data" ] . create ( {
 "name" : "action_%s" % ( I1Ii11i ) ,
 "model" : "ir.actions.report" ,
 "module" : "cf_report_designer" ,
 "noupdate" : False ,
 "res_id" : Ooo0OOoOoO0 . id
 } )
   if 70 - 70: iiiiIi11i
   Ooo0OOoOoO0 . create_action ( )
   if 59 - 59: Ooo00oOo00o % iiiiIi11i
 def _make_templ ( self ) :
  if 6 - 6: iIii1I11I1II1 % i11iIiiIii % oOoO0oo0OOOo
  if 93 - 93: oooO0oo0oOOOO * OoooooooOO + Oo
  IiII111i1i11 = "%s%s" % ( o00O0OoO , self . name . replace ( '.' , '_' ) )
  I1Ii11i = self . _get_report_id ( )
  i1111I1I = self . _get_report_name ( )
  i1i = self . _get_report_file ( )
  if 40 - 40: Oo * oooO0oo0oOOOO * i11iIiiIii
  oo0OO00OoooOo = self . _get_report_name ( False )
  if 19 - 19: oOoO0oo0OOOo % OoooooooOO % oooO0oo0oOOOO * Ooo00oOo00o % O0
  ooo = """<?xml version="1.0"?>
<t t-name="%s">
  <t t-call="cfprint.html_container">
    <t t-raw="show_message"/>
  </t>
<script type="text/javascript">
  <t t-raw="cfprint_json"/>
</script>
</t>
""" % ( oo0OO00OoooOo )
  if 27 - 27: Oo % oo
  o0oooOO00 = self . env [ 'ir.ui.view' ]
  if 32 - 32: o0oo0o
  try :
   Iii1 = o0oooOO00 . create ( {
 "name" : I1Ii11i ,
 "key" : i1111I1I ,
 "priority" : 16 ,
 "type" : "qweb" ,
 "arch_db" : ooo ,
 "mode" : "primary" ,
 "active" : True ,

   } )
   if Iii1 :
    self . env [ "ir.model.data" ] . create ( {
 "name" : oo0OO00OoooOo ,
 "model" : "ir.ui.view" ,
 "module" : "cf_report_designer" ,
 "noupdate" : False ,
 "res_id" : Iii1 . id
 } )
    if 61 - 61: oOo0O0Ooo - II11iiII - i1IIi
  except Exception as IiI1iIiIIIii :
   IiII1IiiIiI1 . error ( "Create report template[%s] failed." % ( i1111I1I ) )
   raise IiI1iIiIIIii
   if 53 - 53: i1IIi
 def action_generate ( self ) :
  if 59 - 59: Ooo00oOo00o
  if 81 - 81: oOo0O0Ooo - oOo0O0Ooo . i1I1ii1II1iII
  if 73 - 73: OoOO0ooOOoo0O % i11iIiiIii - oo
  self . _remove_report ( )
  if 7 - 7: O0 * i11iIiiIii * o0000oOoOoO0o + Oo % ooOO00oOo - Oo
  if 39 - 39: OoO0O00 * II11iiII % II11iiII - OoooooooOO + Ooo00oOo00o - OoOO0ooOOoo0O
  self . _make_report_defind ( )
  if 23 - 23: i11iIiiIii
  if 30 - 30: Ooo00oOo00o - i1IIi % II111iiii + OoOO0ooOOoo0O * iIii1I11I1II1
  self . _make_templ ( )
  if 81 - 81: oooO0oo0oOOOO % i1IIi . iIii1I11I1II1
  self . write ( { "state" : "defined" } )
  if 4 - 4: i11iIiiIii % ooOO00oOo % i1IIi / oooO0oo0oOOOO
 def action_design ( self ) :
  if 6 - 6: i1I1ii1II1iII / oo % II11iiII - oo
  if 31 - 31: II11iiII
  if 23 - 23: o0oo0o . oooO0oo0oOOOO
  OO0000o = self . env [ self . model_id . model ] . search ( [ ] , limit = 5 )
  i1I1i1 = [ i11111IIIII . id for i11111IIIII in OO0000o ]
  if 81 - 81: Oo - iIii1I11I1II1 - i1IIi / o0oo0o - O0 * OoOO0ooOOoo0O
  if 20 - 20: iiiiIi11i % oooO0oo0oOOOO
  I1Ii11i = "cf_report_designer.%s%s" % ( i1I , self . name )
  if 19 - 19: oOoO0oo0OOOo % oooO0oo0oOOOO + Oo / o0oo0o . Oo
  i1111I1I = "cf_report_designer.%s%s" % ( o00O0OoO , self . name )
  IiIi1I1 = { "is_design" : True ,
 "docs" : OO0000o ,
 "docids" : i1I1i1
 }
  if 39 - 39: II111iiii + oOo0O0Ooo - Oo . oOo0O0Ooo
  return ( self . env [ 'ir.actions.report' ] . search ( [ ( 'report_name' , '=' , i1111I1I ) ] , limit = 1 )
 . with_context ( { 'is_design' : True } )
 . report_action ( i1I1i1 , data = IiIi1I1 ) )
  if 84 - 84: ooOO00oOo + i1IIi - II111iiii . oOoO0oo0OOOo * OoooooooOO + oo
  if 38 - 38: II11iiII + II111iiii % Oo % oOo0O0Ooo - o0000oOoOoO0o / OoooooooOO
class oOOoo0000O0o0 ( models . Model ) :
 _name = 'cf.report.define.field'
 _description = u'报表字段'
 _order = 'report_id, id'
 if 1 - 1: iiiiIi11i + iiiiIi11i % oOo0O0Ooo + i11iIiiIii
 report_id = fields . Many2one ( "cf.report.define" , string = u"报表定义" , required = True , ondelete = 'cascade' , help = u"字段所在的报表定义" )
 model_id = fields . Many2one ( 'ir.model' , string = u"数据表(模型)" , required = True , ondelete = 'cascade' , help = u"字段所在的model" )
 model_name = fields . Char ( related = "model_id.name" , string = u"模型名称" )
 field_id = fields . Many2one ( "ir.model.fields" , string = u"字段" , required = True , ondelete = 'cascade' )
 name = fields . Char ( related = "field_id.name" , string = u'字段名称' )
 field_description = fields . Char ( related = "field_id.field_description" , string = u'字段说明' )
 ttype = fields . Selection ( related = "field_id.ttype" , string = u'字段类型' )
 related_field_id = fields . Many2one ( "cf.report.define.field" , string = u"关联字段" , help = u"与关联表关联的字段(related_external_field_ids)" , oldname = "parent_field_id" )
 related_external_field_ids = fields . One2many ( "cf.report.define.field" , "related_field_id" , string = u"关联数据表字段" , help = u"与当前表相关联的表字段" , oldname = "sub_field_ids" )
 note = fields . Text ( string = u"备注" )
 if 56 - 56: Ooo00oOo00o
 related_field_model_id = fields . Many2one ( 'ir.model' , compute = "_compute_relation_model" , string = u"关联数据表（模型）" , help = u"关联字段所在的model。当前字段为One2many，Many2many，Many2one时有值。" )
 related_field_model_name = fields . Char ( related = "related_field_model_id.name" , string = u"关联数据表名称" , help = u"关联字段所在的model名称" )
 if 28 - 28: i1I1ii1II1iII . i1I1ii1II1iII % iIii1I11I1II1 * iIii1I11I1II1 . Ooo00oOo00o / i1I1ii1II1iII
 _sql_constraints = [
 ( 'uniq_repoer_model_field' , 'unique(report_id, model_id, field_id)' , u'报表 + 表 + 字段必须唯一!' ) ,
 ]
 if 27 - 27: ooOO00oOo + Oo - i1IIi
 @ api . model
 def create ( self , vals ) :
  if 69 - 69: oooO0oo0oOOOO - O0 % oOoO0oo0OOOo + i11iIiiIii . oOo0O0Ooo / ooOO00oOo
  if not vals . get ( "model_id" , False ) :
   oO00O000oO0 = self . env [ "ir.model.fields" ] . browse ( vals . get ( "field_id" , 0 ) )
   if oO00O000oO0 :
    vals [ "model_id" ] = oO00O000oO0 . model_id . id
    if 79 - 79: O0 * i11iIiiIii - oooO0oo0oOOOO / oooO0oo0oOOOO
    if 48 - 48: O0
  self . search ( [ ( 'report_id' , '=' , vals . get ( "report_id" , 0 ) ) , ( 'model_id' , '=' , vals . get ( "model_id" , 0 ) ) , ( 'field_id' , '=' , vals . get ( "field_id" , 0 ) ) ] ) . unlink ( )
  if 93 - 93: i11iIiiIii - oo * oOoO0oo0OOOo * OoOO0ooOOoo0O % O0 + OoooooooOO
  return super ( oOOoo0000O0o0 , self ) . create ( vals )
  if 25 - 25: oooO0oo0oOOOO + o0000oOoOoO0o / Oo . Ooo00oOo00o % O0 * ooOO00oOo
  if 84 - 84: Oo % o0000oOoOoO0o + i11iIiiIii
 def _compute_relation_model ( self ) :
  for oO00O000oO0 in self :
   II1I1Ii = self . env [ 'ir.model' ] . _get ( oO00O000oO0 . field_id . relation )
   oO00O000oO0 . related_field_model_id = II1I1Ii . id if II1I1Ii else None
   if 62 - 62: O0 % OoOO0ooOOoo0O . OoOO0ooOOoo0O - iIii1I11I1II1 / i11iIiiIii
 def action_retrieve_fields ( self ) :
  if self . field_id and ( self . field_id . ttype == 'one2many' or self . field_id . ttype == 'many2many' or self . field_id . ttype == 'many2one' ) :
   if 31 - 31: iIii1I11I1II1 / ooOO00oOo / oOoO0oo0OOOo
   if self . env . get ( self . field_id . relation , '_EMPTY' ) == '_EMPTY' :
    raise AccessError ( _ ( u"未找到关联字段对应的表（%s），无法获取关联表字段！" % ( self . field_id . relation ) ) )
    if 41 - 41: OoO0O00
    if 10 - 10: OoO0O00 / OoO0O00 / o0oo0o . o0oo0o
   OOoo = self . env [ 'ir.model' ] . _get ( self . field_id . relation )
   if 50 - 50: ooOO00oOo
   if 43 - 43: II111iiii . iiiiIi11i / oOoO0oo0OOOo
   self . action_remove_fields ( )
   if 20 - 20: oo
   if 95 - 95: i1I1ii1II1iII - oo
   for OoiIIiIi1 in OOoo . field_id :
    oO00O000oO0 = self . env [ 'cf.report.define.field' ] . create ( {
 "related_field_id" : self . id ,
 "report_id" : self . report_id . id ,
 "model_id" : OoiIIiIi1 . model_id . id ,
 "field_id" : OoiIIiIi1 . id ,
 } )
    if 34 - 34: Oo * oo . i1IIi * Oo / Oo
 def action_remove_fields ( self ) :
  if self . field_id and ( self . field_id . ttype == 'one2many' or self . field_id . ttype == 'many2many' or self . field_id . ttype == 'many2one' ) :
   if 30 - 30: oOoO0oo0OOOo + OoO0O00 / OoO0O00 % oOoO0oo0OOOo . oOoO0oo0OOOo
   OOoo = self . env [ 'ir.model' ] . _get ( self . field_id . relation )
   if 55 - 55: Oo - OoOO0ooOOoo0O + II111iiii + i1I1ii1II1iII % o0000oOoOoO0o
   if 41 - 41: i1IIi - OoOO0ooOOoo0O - o0000oOoOoO0o
   self . env [ "cf.report.define.field" ] . search ( [ ( 'report_id' , '=' , self . report_id . id ) , ( 'model_id' , '=' , OOoo . id ) , ( 'related_field_id' , '=' , self . id ) ] ) . unlink ( )
   if 8 - 8: ooOO00oOo + o0oo0o - Ooo00oOo00o % OoO0O00 % Ooo00oOo00o * iiiiIi11i
 def action_view_sub_fields ( self ) :
  self . ensure_one ( )
  if 9 - 9: OoO0O00 - i11iIiiIii - II11iiII * o0000oOoOoO0o + Oo
  iIIII = self . env . ref ( 'cf_report_designer.cf_report_define_field_form' ) . id
  return { 'type' : 'ir.actions.act_window' ,
 'res_model' : 'cf.report.define.field' ,
 'view_mode' : 'form' ,
 'views' : [ ( iIIII , 'form' ) ] ,
 'res_id' : self . id ,
 'target' : 'new' ,
 'limit' : 1000 ,
 'name' : u'关联表字段' ,
 'flags' : { 'form' : { 'action_buttons' : False } }
 }
  if 45 - 45: oOoO0oo0OOOo % oo - i11iIiiIii
  if 11 - 11: iIii1I11I1II1 * iIii1I11I1II1 * oo
  if 46 - 46: oOo0O0Ooo + ooOO00oOo
  if 70 - 70: i1I1ii1II1iII / iIii1I11I1II1
  if 85 - 85: OoooooooOO % i1IIi * OoooooooOO / oOoO0oo0OOOo
  if 96 - 96: OoooooooOO + iiiiIi11i
  if 44 - 44: iiiiIi11i
from xml . dom import minidom
import uuid
if 20 - 20: OoOO0ooOOoo0O + o0000oOoOoO0o / O0 % iIii1I11I1II1
oOo0O = "<h5 style=\"margin-top: 3rem; text-align: center;\">%s</h4>"
if 64 - 64: oOoO0oo0OOOo - i1I1ii1II1iII + i1I1ii1II1iII - OoOO0ooOOoo0O
if 30 - 30: iIii1I11I1II1 . oo . II11iiII / Ooo00oOo00o
class iiI1I1 ( models . Model ) :
 if 56 - 56: oo . O0 + OoO0O00
 _inherit = 'ir.actions.report'
 if 1 - 1: i1I1ii1II1iII
 if 97 - 97: II11iiII + i1I1ii1II1iII + O0 + i11iIiiIii
 if 77 - 77: Ooo00oOo00o / OoooooooOO
 _description = 'Report Action'
 if 46 - 46: Ooo00oOo00o % iIii1I11I1II1 . i1I1ii1II1iII % i1I1ii1II1iII + i11iIiiIii
 cf_report_define_id = fields . Many2one ( "cf.report.define" , string = u"报表定义" , help = u"如果是康虎云报表，则保存对应的报表定义。" )
 if 72 - 72: iIii1I11I1II1 * o0000oOoOoO0o % Oo / ooOO00oOo
 def _make_cfprint_json ( self , values ) :
  if 35 - 35: Oo + i1IIi % oOoO0oo0OOOo % OoOO0ooOOoo0O + iiiiIi11i
  if 17 - 17: i1IIi
  def iiIi1i ( report_define , model , fields , docs , datas ) :
   if 27 - 27: II11iiII * Oo . o0oo0o % oooO0oo0oOOOO * oooO0oo0oOOOO . i1IIi
   if 72 - 72: II11iiII % oOoO0oo0OOOo + ooOO00oOo / iiiiIi11i + oooO0oo0oOOOO
   def I1I1i ( lst ) :
    I1IIIiIiIi = set ( )
    IIIII1 = [ ]
    for iIi1Ii1i1iI in lst :
     IIiI1 = tuple ( iIi1Ii1i1iI . items ( ) )
     if IIiI1 not in I1IIIiIiIi :
      I1IIIiIiIi . add ( IIiI1 )
      IIIII1 . append ( iIi1Ii1i1iI )
    return IIIII1
    if 17 - 17: II11iiII / II11iiII / OoOO0ooOOoo0O
   ii1 = { }
   if 1 - 1: Oo % iIii1I11I1II1 + OoO0O00 . iIii1I11I1II1 % oo
   o0o0oOoOO0O = model . model . replace ( "." , "_" )
   if 16 - 16: oooO0oo0oOOOO % iIii1I11I1II1 . o0000oOoOoO0o
   if 59 - 59: oo * II111iiii . O0
   for O000OoOO0 in docs :
    i1IiIII111i1 = { }
    if 57 - 57: o0000oOoOoO0o % o0000oOoOoO0o * i11iIiiIii
    for oO00O000oO0 in [ iIi1Ii1i1iI for iIi1Ii1i1iI in fields if iIi1Ii1i1iI . model_id . model == model . model ] :
     try :
      if oO00O000oO0 . ttype in [ 'char' ] :
       if oO00O000oO0 . name == "type_name" :
        if 7 - 7: O0 . o0000oOoOoO0o
        if 51 - 51: ooOO00oOo - O0 % iiiiIi11i - II111iiii
        pass
       i1IiIII111i1 [ oO00O000oO0 . name ] = O000OoOO0 [ oO00O000oO0 . name ] or ""
       if 31 - 31: i1I1ii1II1iII / OoO0O00 - i1I1ii1II1iII - II11iiII
       if oO00O000oO0 . ttype == 'char' and O000OoOO0 [ oO00O000oO0 . name ] and len ( O000OoOO0 [ oO00O000oO0 . name ] ) > ii1 . get ( oO00O000oO0 . name , 0 ) :
        ii1 [ oO00O000oO0 . name ] = len ( O000OoOO0 [ oO00O000oO0 . name ] )
        if 7 - 7: i1I1ii1II1iII % O0 . oOo0O0Ooo + oo - OoOO0ooOOoo0O
      elif oO00O000oO0 . ttype in [ 'boolean' ] :
       i1IiIII111i1 [ oO00O000oO0 . name ] = O000OoOO0 [ oO00O000oO0 . name ]
       if 75 - 75: OoOO0ooOOoo0O
      elif oO00O000oO0 . ttype in [ 'integer' , 'float' ] :
       i1IiIII111i1 [ oO00O000oO0 . name ] = O000OoOO0 [ oO00O000oO0 . name ] if O000OoOO0 [ oO00O000oO0 . name ] != None else ""
       if 71 - 71: Oo
      elif oO00O000oO0 . ttype == 'datetime' :
       i1IiIII111i1 [ oO00O000oO0 . name ] = O000OoOO0 [ oO00O000oO0 . name ] . strftime ( "%Y-%m-%d %H:%M:%S" ) if O000OoOO0 [ oO00O000oO0 . name ] else ""
       if 53 - 53: OoooooooOO % o0000oOoOoO0o . oooO0oo0oOOOO / i11iIiiIii % i1I1ii1II1iII
      elif oO00O000oO0 . ttype == 'binary' :
       iIiIIIIIii = O000OoOO0 [ oO00O000oO0 . name ] . strip ( ) . decode ( "UTF-8" ) . replace ( "\n" , "" ) if O000OoOO0 [ oO00O000oO0 . name ] else ""
       i1IiIII111i1 [ oO00O000oO0 . name ] = "base64/jpg:%s" % ( iIiIIIIIii )
       if 58 - 58: Ooo00oOo00o / oooO0oo0oOOOO . oOo0O0Ooo / OoooooooOO + o0oo0o
      elif oO00O000oO0 . ttype in [ "one2many" , "many2many" ] and len ( oO00O000oO0 . related_external_field_ids ) > 0 :
       O0OoO0ooOO0o = O000OoOO0 [ oO00O000oO0 . name ]
       OoOo0oOooOoOO = oO00O000oO0 . related_external_field_ids
       if 60 - 60: OoooooooOO % o0000oOoOoO0o * i1IIi
       iI11 = self . env [ 'ir.model' ] . _get ( oO00O000oO0 . field_id . relation )
       if O0OoO0ooOO0o and len ( O0OoO0ooOO0o ) > 0 and OoOo0oOooOoOO and len ( OoOo0oOooOoOO ) > 0 and iI11 :
        iiIi1i ( report_define , iI11 , OoOo0oOooOoOO , O0OoO0ooOO0o , datas )
        if 96 - 96: II11iiII
      elif oO00O000oO0 . ttype in [ 'many2one' ] :
       i1IiIII111i1 [ oO00O000oO0 . name ] = O000OoOO0 [ oO00O000oO0 . name ] . id or ""
       i1IiIII111i1 [ oO00O000oO0 . name + "_name" ] = O000OoOO0 [ oO00O000oO0 . name ] . name or ""
       if 85 - 85: Ooo00oOo00o . oOo0O0Ooo / Oo . O0 % o0oo0o
       if 90 - 90: OoO0O00 % O0 * iIii1I11I1II1 . i1I1ii1II1iII
       if len ( i1IiIII111i1 [ oO00O000oO0 . name + "_name" ] ) > ii1 . get ( oO00O000oO0 . name + "_name" , 0 ) :
        ii1 [ oO00O000oO0 . name + "_name" ] = len ( i1IiIII111i1 [ oO00O000oO0 . name + "_name" ] )
        if 8 - 8: Oo + II111iiii / i1I1ii1II1iII / OoOO0ooOOoo0O
       if len ( oO00O000oO0 . related_external_field_ids ) > 0 :
        O0OoO0ooOO0o = O000OoOO0 [ oO00O000oO0 . name ]
        OoOo0oOooOoOO = oO00O000oO0 . related_external_field_ids
        if 74 - 74: O0 / i1IIi
        iI11 = self . env [ 'ir.model' ] . _get ( oO00O000oO0 . field_id . relation )
        if O0OoO0ooOO0o and len ( O0OoO0ooOO0o ) > 0 and OoOo0oOooOoOO and len ( OoOo0oOooOoOO ) > 0 and iI11 :
         iiIi1i ( report_define , iI11 , OoOo0oOooOoOO , O0OoO0ooOO0o , datas )
         if 78 - 78: OoooooooOO . ooOO00oOo + Oo - i1IIi
     except Exception as ii1O0 :
      IiII1IiiIiI1 . error ( _ ( u"生成康虎云报表打印数据出错。model: %s, field: %s, Error: %s" ) % ( model . model , oO00O000oO0 . name , ii1O0 ) )
      if 33 - 33: i1IIi
    if i1IiIII111i1 :
     if not datas . get ( o0o0oOoOO0O , False ) :
      datas [ o0o0oOoOO0O ] = { "cols" : [ ] , "rows" : [ ] }
     datas [ o0o0oOoOO0O ] [ "rows" ] . append ( i1IiIII111i1 )
     if 36 - 36: II111iiii % i11iIiiIii * oOo0O0Ooo + OoOO0ooOOoo0O
     if 25 - 25: iIii1I11I1II1 % i1I1ii1II1iII . Oo
   for oO00O000oO0 in [ iIi1Ii1i1iI for iIi1Ii1i1iI in fields if iIi1Ii1i1iI . model_id . model == model . model ] :
    IIIIi1 = "str"
    if oO00O000oO0 . ttype in [ "integer" ] :
     IIIIi1 = "int"
    elif oO00O000oO0 . ttype in [ "float" ] :
     IIIIi1 = "float"
    elif oO00O000oO0 . ttype in [ "datetime" ] :
     IIIIi1 = "date"
    elif oO00O000oO0 . ttype in [ "boolean" ] :
     IIIIi1 = "boolean"
    elif oO00O000oO0 . ttype in [ "binary" ] :
     IIIIi1 = "blob"
    elif oO00O000oO0 . ttype in [ "many2one" ] :
     IIIIi1 = "int"
     if 3 - 3: o0oo0o
    i1iiIiI1Ii1i = 0
    if IIIIi1 == "str" :
     i1iiIiI1Ii1i = ii1 . get ( oO00O000oO0 . name , 20 )
     if 22 - 22: oooO0oo0oOOOO / i11iIiiIii
    if not datas . get ( o0o0oOoOO0O , False ) :
     datas [ o0o0oOoOO0O ] = { "cols" : [ ] , "rows" : [ ] }
    datas [ o0o0oOoOO0O ] [ "cols" ] . append ( { "type" : IIIIi1 , "size" : i1iiIiI1Ii1i , "name" : oO00O000oO0 . name , "required" : False , "comment" : oO00O000oO0 . field_description } )
    if oO00O000oO0 . ttype in [ "many2one" ] :
     datas [ o0o0oOoOO0O ] [ "cols" ] . append ( { "type" : "str" , "size" : ii1 . get ( oO00O000oO0 . name + "_name" , 20 ) , "name" : oO00O000oO0 . name + "_name" , "required" : False , "comment" : oO00O000oO0 . field_description } )
     if 62 - 62: ooOO00oOo / oOoO0oo0OOOo
   datas [ o0o0oOoOO0O ] [ "cols" ] = I1I1i ( datas [ o0o0oOoOO0O ] [ "cols" ] )
   return datas
   if 7 - 7: OoooooooOO . oooO0oo0oOOOO
   if 53 - 53: o0000oOoOoO0o % o0000oOoOoO0o * Ooo00oOo00o + oOo0O0Ooo
   if 92 - 92: OoooooooOO + i1IIi / o0000oOoOoO0o * O0
  O00oOo00o0o = values . get ( "report_define" )
  ii111iI1iIi1 = ii1I . get_machine_code ( ) or ''
  O00oO0 = {
 "template" : "" ,
 "ver" : 4 ,
 "Copies" : 1 ,
 "Duplex" : 0 ,
 "mcode" : ii111iI1iIi1 ,
 "Tables" : [ ]
 }
  if 70 - 70: OoOO0ooOOoo0O . oOoO0oo0OOOo * OoooooooOO - oooO0oo0oOOOO * oo + oOo0O0Ooo
  iIi1 = self . _context . get ( "is_design" , False )
  if iIi1 :
   O00oO0 [ "design" ] = True
   i11iiI1111 = oOo0O % ( _ ( u"""请在康虎云报表设计器设计报表。<br/>
            如果报表设计器未打开，请检查康虎云报表是否已启动！<br/><br/><br/>
            模板设计完成后，请在odoo菜单“康虎云报表”--&gt;“模板”菜单中，打开模板记录上传或更新模板！<br/><br/>
            <a href=\"cfprint://open\">启动康虎云报表</a>
            """ ) )
   values . update ( show_message = i11iiI1111 )
   if 97 - 97: OoO0O00 * oo . iIii1I11I1II1
  if O00oOo00o0o . use_client_templ and O00oOo00o0o . client_templ_name :
   O00oO0 [ "template" ] = O00oOo00o0o . client_templ_name
  else :
   if not O00oOo00o0o . template_id or not O00oOo00o0o . template_id . templ_id :
    values . update ( show_message = oOo0O % ( _ ( u"未指定要打印的报表模板，请先指定报表模板。" ) ) )
   I1Ii1111iIi = self . env [ 'cf.template' ] . search ( [ ( 'templ_id' , '=' , O00oOo00o0o . template_id . templ_id ) ] , limit = 1 ) . template
   if not I1Ii1111iIi or I1Ii1111iIi == "" :
    if not iIi1 :
     values . update ( show_message = oOo0O % ( _ ( u"指定的报表模板未定义或模板无内容，请先设计模板并更新到模板记录表。</h3>" ) ) )
    else :
     O00oO0 [ "template" ] = "cf_templ_%s" % ( O00oOo00o0o . name . replace ( '.' , '_' ) )
   else :
    O00oO0 [ "template" ] = "base64:" + I1Ii1111iIi . strip ( ) . decode ( "UTF-8" ) . replace ( "\n" , "" )
    if 31 - 31: OoOO0ooOOoo0O . o0oo0o * Oo + i11iIiiIii * iiiiIi11i
  IiIi1I1 = { }
  OO0000o = values . get ( "docs" )
  if not OO0000o or len ( OO0000o ) < 1 :
   OO0o = self . _context . get ( "active_ids" , [ ] )
   OO0000o = self . env [ O00oOo00o0o . model_id . model ] . browse ( OO0o )
   if 75 - 75: OoooooooOO * oooO0oo0oOOOO
  iiIi1i ( O00oOo00o0o , O00oOo00o0o . model_id , O00oOo00o0o . field_ids , OO0000o , IiIi1I1 )
  if 9 - 9: oooO0oo0oOOOO - II111iiii + O0 / iIii1I11I1II1 / i11iIiiIii
  if 39 - 39: oooO0oo0oOOOO * OoO0O00 + iIii1I11I1II1 - oooO0oo0oOOOO + II11iiII
  for o0 , ( iiiI1I1iIIIi1 , Iii ) in enumerate ( IiIi1I1 . items ( ) ) :
   I1iiiiI1iI = string . capwords ( iiiI1I1iIIIi1 ) . replace ( "." , "_" )
   iIiiiii1i = Iii [ "cols" ]
   iiIi1IIiI = Iii [ "rows" ]
   O00oO0 [ "Tables" ] . append ( {
 "Name" : I1iiiiI1iI ,
 "Cols" : iIiiiii1i ,
 "Data" : iiIi1IIiI ,
 } )
   if 23 - 23: o0000oOoOoO0o . II11iiII
  return O00oO0
  if 9 - 9: Oo - oOoO0oo0OOOo - i1I1ii1II1iII
 def _set_report_data ( self , values , report_data ) :
  if 82 - 82: oooO0oo0oOOOO - oooO0oo0oOOOO + oOo0O0Ooo
  if 8 - 8: Ooo00oOo00o % i1I1ii1II1iII * iiiiIi11i % o0000oOoOoO0o . Oo / Oo
  if 81 - 81: ooOO00oOo
  oO0o00oOOooO0 = [
 "var cfprint_addr = \"127.0.0.1\"" ,
 "var _delay_close = -1"
 ]
  IiII1IiiIiI1 . debug ( 'Dump report data to json...' )
  OOOoO000 = json . dumps ( report_data )
  if 57 - 57: II111iiii
  if 54 - 54: OoO0O00 + iiiiIi11i + i11iIiiIii
  IiII1IiiIiI1 . debug ( 'Encrypt report data...' )
  o0o = ii1I . rand_aes_key ( 16 , False )
  IiII1IiiIiI1 . debug ( "AES Key: %s" % ( o0o ) )
  i1i1ii111 = ii1I ( o0o , AES . MODE_CBC )
  IiI1i = i1i1ii111 . encrypt ( OOOoO000 )
  if 87 - 87: Oo
  if 45 - 45: ooOO00oOo / OoooooooOO - i1I1ii1II1iII / o0000oOoOoO0o % oooO0oo0oOOOO
  IiII1IiiIiI1 . debug ( 'Encrypt key...' )
  if 83 - 83: oo . iIii1I11I1II1 - oooO0oo0oOOOO * i11iIiiIii
  if 20 - 20: i1IIi * o0oo0o + II111iiii % Ooo00oOo00o % iiiiIi11i
  if 13 - 13: OoO0O00
  if 60 - 60: oOoO0oo0OOOo * oo
  i1i1ii111 = ii1I ( OooO0OO ( ) , AES . MODE_CBC )
  I1iIiI11I1 = i1i1ii111 . encrypt ( o0o )
  if 27 - 27: o0000oOoOoO0o . i11iIiiIii % o0oo0o
  OooOOOOoO00OoOO = {
 "token" : I1iIiI11I1 . decode ( "utf-8" ) ,
 "dea" : "aes" ,
  "tea" : "aes" ,
  "data" : IiI1i . decode ( "utf-8" )
 }
  if 85 - 85: iiiiIi11i - iIii1I11I1II1 / O0
  IiII1IiiIiI1 . debug ( 'Dump final_data...' )
  if 99 - 99: II111iiii * oooO0oo0oOOOO % iIii1I11I1II1 / o0000oOoOoO0o
  oO0o00oOOooO0 . append ( "var _data = %s" % ( json . dumps ( OooOOOOoO00OoOO ) ) )
  if 90 - 90: iiiiIi11i % II11iiII - II11iiII % II111iiii * ooOO00oOo
  oO0o00oOOooO0 . append ( """_reportData = JSON.stringify(_data);\nconsole.log(_reportData);""" )
  iIi1iI111I = ";\n" . join ( oO0o00oOOooO0 )
  IiII1IiiIiI1 . debug ( 'json_data: %s ...' % ( iIi1iI111I [ 0 : 300 ] ) )
  if 85 - 85: OoooooooOO * iIii1I11I1II1 . i1I1ii1II1iII / OoooooooOO % oo % O0
  values . update (
 cfprint_json = iIi1iI111I ,
 )
  if 36 - 36: o0000oOoOoO0o / II111iiii / oooO0oo0oOOOO / oooO0oo0oOOOO + oOoO0oo0OOOo
 @ api . multi
 def render ( self , template , values = None ) :
  if values is None :
   if 95 - 95: oooO0oo0oOOOO
   if 51 - 51: II111iiii + oooO0oo0oOOOO . i1IIi . oOoO0oo0OOOo + oOo0O0Ooo * oo
   if 72 - 72: iiiiIi11i + iiiiIi11i / II111iiii . OoooooooOO % o0000oOoOoO0o
   if 49 - 49: iiiiIi11i . ooOO00oOo - OoO0O00 * OoooooooOO . OoO0O00
   if 2 - 2: OoooooooOO % II11iiII
   if 63 - 63: oo % iIii1I11I1II1
   values = { }
   if 39 - 39: i1I1ii1II1iII / II111iiii / oOoO0oo0OOOo % oo
  IiII1IiiIiI1 . debug ( "Render report..." )
  Ooo0OOoOoO0 = self . _get_report_from_name ( template )
  if not Ooo0OOoOoO0 :
   raise AccessError ( _ ( u"未找到报表（%s）定义，可能是报表未定义或定义未生效，如果使用康虎云报表，请在报表定义中重新生成一下报表定义！" % ( template ) ) )
   if 89 - 89: o0oo0o + OoooooooOO + o0oo0o * i1IIi + iIii1I11I1II1 % OoOO0ooOOoo0O
  i11iiI1111 = oOo0O % ( _ ( u"正在打印，请稍候...<br/><br/>如果打印机未输出报表，请检查康虎云报表是否已启动！<br/><br/><a href=\"cfprint://open\">启动康虎云报表</a>" ) )
  if 59 - 59: II11iiII + i11iIiiIii
  IiII1IiiIiI1 . debug ( "Prepare docs..." )
  OO0000o = values . get ( "docs" , False )
  if not OO0000o or len ( OO0000o ) < 1 :
   OO0o = self . _context . get ( "active_ids" , [ ] )
   OO0000o = self . env [ Ooo0OOoOoO0 . model ] . browse ( OO0o )
   values . update ( docs = OO0000o )
  if not OO0000o or len ( OO0000o ) < 1 :
   i11iiI1111 = oOo0O % ( _ ( u"没有可以打印数据。" ) )
   if 88 - 88: i11iIiiIii - Oo
  IiII1IiiIiI1 . debug ( "Retrieve report define..." )
  if 67 - 67: II11iiII . OoO0O00 + oOo0O0Ooo - OoooooooOO
  OOOoO = Ooo0OOoOoO0 . xml_id . split ( "." )
  if len ( OOOoO ) > 1 :
   OOOoO = OOOoO [ 1 ] . replace ( i1I , "" )
  else :
   OOOoO = OOOoO [ 0 ] . replace ( i1I , "" )
   if 14 - 14: OoOO0ooOOoo0O . iIii1I11I1II1 . OoooooooOO . II111iiii / Ooo00oOo00o
  values . update (
 show_message = i11iiI1111
 )
  if 21 - 21: i11iIiiIii / i1IIi + oo * II11iiII . o0oo0o
  if 84 - 84: O0 . OoOO0ooOOoo0O - II111iiii . Oo / II111iiii
  iii1 = self . env [ "cf.report.define" ] . search ( [ ( 'name' , '=' , OOOoO ) ] , limit = 1 )
  if 32 - 32: o0000oOoOoO0o . oooO0oo0oOOOO . OoooooooOO - ooOO00oOo + iiiiIi11i
  IiII1IiiIiI1 . debug ( "Prepare to make json...[%s]" % ( OOOoO ) )
  if iii1 :
   IiII1IiiIiI1 . debug ( "Set report_define to values..." )
   values . update ( report_define = iii1 , )
   IiII1IiiIiI1 . debug ( "Begin to make report data ..." )
   ooO0oO00O0o = self . _make_cfprint_json ( values )
   IiII1IiiIiI1 . debug ( "Begin to convert report data to json..." )
   self . _set_report_data ( values , ooO0oO00O0o )
   IiII1IiiIiI1 . debug ( "Converted!!!" )
   if 70 - 70: o0oo0o
  i1IiIII111i1 = super ( iiI1I1 , self ) . render ( template , values )
  return i1IiIII111i1
  if 16 - 16: i1I1ii1II1iII - OoooooooOO % OoO0O00
 def action_upload_templ_win ( self ) :
  i11i1iIiii = self . _context . get ( "templ_id" , False )
  return {
 'name' : _ ( u'上传康虎云报表模板' ) ,
 'type' : 'ir.actions.act_window' ,
 'view_type' : 'form' ,
 'res_model' : 'cf.template' ,
 'res_id' : i11i1iIiii ,

  'context' : self . _context ,
 'target' : 'current' ,
 'nodestroy' : True
 }
  if 71 - 71: oOoO0oo0OOOo % Oo - oo % OoOO0ooOOoo0O - O0
 @ api . model
 def render_qweb_html ( self , docids , data = None ) :
  if 67 - 67: II11iiII + OoO0O00
  OoOo000oOo0oo = data . get ( "is_design" , False )
  oO0OoOO = _ ( u"设计" ) if OoOo000oOo0oo else _ ( u"打印" )
  if 11 - 11: i11iIiiIii - iiiiIi11i . iiiiIi11i
  iii1 = self . cf_report_define_id
  if iii1 :
   if not docids :
    docids = data . get ( "docids" , None )
    if 31 - 31: II11iiII / OoO0O00 * i1IIi . oOo0O0Ooo
   i11iiI1111 = oOo0O % ( _ ( u"正在打印，请稍候...<br/><br/>如果打印机未输出报表，请检查康虎云报表是否已启动！<br/><br/><a href=\"cfprint://open\">启动康虎云报表</a>" ) )
   if 57 - 57: II11iiII + iIii1I11I1II1 % i1IIi % oo
   OO0000o = data . get ( "docs" , False )
   if 83 - 83: Ooo00oOo00o / i11iIiiIii % iIii1I11I1II1 . OoOO0ooOOoo0O % iiiiIi11i . OoooooooOO
   if ( not OO0000o or not isinstance ( OO0000o , list ) or len ( OO0000o ) < 1 ) and docids and iii1 and iii1 . model_id and iii1 . model_id . model :
    OO0000o = self . env [ iii1 . model_id . model ] . browse ( docids )
    if 94 - 94: o0000oOoOoO0o + iIii1I11I1II1 % ooOO00oOo
   if not OO0000o or len ( OO0000o ) < 1 :
    i11iiI1111 = oOo0O % ( _ ( u"没有可以%s数据。" ) % ( oO0OoOO ) )
    if 93 - 93: o0000oOoOoO0o - II11iiII + iIii1I11I1II1 * Ooo00oOo00o + o0oo0o . i1I1ii1II1iII
   data . update ( docs = OO0000o , show_message = i11iiI1111 , )
   if 49 - 49: OoooooooOO * OoOO0ooOOoo0O - OoO0O00 . iiiiIi11i
   if iii1 :
    data . update ( report_define = iii1 , )
    ooO0oO00O0o = self . with_context ( is_design = OoOo000oOo0oo ) . _make_cfprint_json ( data )
    self . _set_report_data ( data , ooO0oO00O0o )
    if 89 - 89: Oo + o0000oOoOoO0o * Oo / Oo
  return super ( iiI1I1 , self ) . render_qweb_html ( docids , data )
  if 46 - 46: ooOO00oOo
  if 71 - 71: OoOO0ooOOoo0O / OoOO0ooOOoo0O * iiiiIi11i * iiiiIi11i / II111iiii
# dd678faae9ac167bc83abf78e5cb2f3f0688d3a3
