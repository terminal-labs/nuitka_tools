import json
import argparse
import subprocess
import configparser

__version__ = '0.0.1'

parser = argparse.ArgumentParser()

parser.add_argument('-v', '--version', action='version', version=__version__ )

parser.add_argument('cmd', choices=['getnetconf', 'setnetconf'],) 
parser.add_argument('-f', '--format',
                    default='text',
                    const='text',
                    nargs='?',
                    choices=['text', 'json'],
                    help='text or json (default: %(default)s)')

def _call(cmd):
	returned_value = subprocess.check_output(cmd, shell=True)
	returned_value = returned_value.decode('utf-8')
	returned_value = returned_value.strip()
	return returned_value

def _configparser_obj_to_dic():
	pass

def _dic_to_configparser_obj():
	pass
	
def _util_check():
	pass
	

def main(args):
	print(vars(args))
	
	netconf_obj = configparser.ConfigParser()
	netconf_obj.read('output.ini')
	
	dictionary = {}
	for section in netconf_obj.sections():
		dictionary[section] = {}
		for option in netconf_obj.options(section):
			dictionary[section][option] = netconf_obj.get(section, option)
	print(dictionary)
	
	
	data_dict = {
		'Section1': {
			'key1': 'value1',
			'key2': 'value2'
		},
		'Section2': {
			'key3': 'value3'
		}
	}
	config = configparser.ConfigParser()
	for section, values in data_dict.items():
		config[section] = values
	with open('output.ini', 'w') as configfile:
		config.write(configfile)


	print(_call("""ip route get 192.168.1.1"""))
	print(_call("""cat /etc/*-release"""))

if __name__ == '__main__':
    args = parser.parse_args()
    main(args)
