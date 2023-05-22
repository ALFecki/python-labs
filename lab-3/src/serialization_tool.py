import argparse
from serialization_tool.serialization_factory import SerializationFactory
from constants import JSON, XML

arg_parser = argparse.ArgumentParser('JSON to XML or vice versa')
arg_parser.add_argument('first', type=str, help='File from which we want to convert')
arg_parser.add_argument('second', type=str, help='File for which we will convert')

args = arg_parser.parse_args()

deser = None
ser = None

if JSON in args.first:
    deser = SerializationFactory.get_serializer(JSON)
elif XML in args.first:
    deser = SerializationFactory.get_serializer(XML)

if JSON in args.second:
    ser = SerializationFactory.get_serializer(JSON)
elif XML in args.second:
    ser = SerializationFactory.get_serializer(XML)

if ser == None or deser == None:
    print('Parsing error: Error type')
    exit()


result = deser.load(args.first)
result = ser.dump(result, args.second)

print('Converting files success')
