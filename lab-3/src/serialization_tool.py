import argparse
import configparser
from serialization_tool.serialization_factory import SerializationFactory
from constants import JSON, XML

arg_parser = argparse.ArgumentParser('JSON to XML or vice versa')
arg_parser.add_argument('--from_file', type=str, default=None, help='File from which we want to convert')
arg_parser.add_argument('--to_file', type=str, default=None, help='File for which we will convert')
arg_parser.add_argument('--config', type=str, default=None, help='Provide config file. In cfg need to DEFAULT properties \'FromFile\' and \'ToFile\'')

args = arg_parser.parse_args()

deser = None
ser = None


if args.config != None:
    config = configparser.ConfigParser()
    config.read(args.config)
    args.from_file = config['DEFAULT']['FromFile']
    args.to_file = config['DEFAULT']['ToFile']
elif args.from_file == None or args.to_file == None:
    print('Need more arguments')
    exit()


if JSON in args.from_file:
    deser = SerializationFactory.get_serializer(JSON)
elif XML in args.from_file:
    deser = SerializationFactory.get_serializer(XML)

if JSON in args.to_file:
    ser = SerializationFactory.get_serializer(JSON)
elif XML in args.to_file:
    ser = SerializationFactory.get_serializer(XML)

if ser == None or deser == None:
    print('Parsing error: Error type')
    exit()


result = deser.load(args.from_file)
result = ser.dump(result, args.to_file)

print('Converting files success')
