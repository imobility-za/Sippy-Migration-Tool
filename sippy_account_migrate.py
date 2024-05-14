#!/usr/bin/python

'''QAD (Quick and Dirty) Tool to migrate sippy accounts between Resellers and even other partitions'''

import logging
import argparse
import configparser

''' Read config file'''
config = configparser.ConfigParser()
config.read('sippy_account_migrate.conf')

''' Parse Arguments '''
parser = argparse.ArgumentParser(description='Sippy account migration tool for iMobility')
parser.add_argument('-ss', '--source_site', type=str,required=True, help='Site where account to be migrated is situated')
parser.add_argument('-ds', '--destination_site', type=str,default=None, help='Site where account is to be migrated to')
parser.add_argument('-sa', '--source_account', type=str,required=True, help='Source i_account')
parser.add_argument('-sc', '--source_customer', type=str,required=True, help='Source i_customer')
parser.add_argument('-dc', '--destination_customer', type=str,required=True, help='Destination i_customer')
parser.add_argument('-b', '--balance',action='store_true', help='Migrate balance to new account')
args = parser.parse_args()

if args.destination_site is None:
     args.destination_site = args.source_site


'''Setup logging'''
fmt = '%(asctime)-15s %(levelname)s  %(message)s'
logging.basicConfig(level=logging.INFO,format=fmt,filename='sippy_account_migrate.log')
logging.info("migrate tool started with following args: %s", args)




