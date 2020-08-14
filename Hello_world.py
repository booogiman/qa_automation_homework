import argparse

parser = argparse.ArgumentParser()


parser.add_argument('--schema',
                    help='schema',
                    type=str,
                    default='https',
                    choices=['http', 'https'])
parser.add_argument('--brows',
                    help='brows',
                    default='gh',
                    choices=['gh', 'ff', 'ie'])

parser.add_argument('--host',
                    help='host',
                    type=str,
                    default="localhost")

# Если параметр передан то Ture, иначе False
parser.add_argument('--path',
                    default='/',
                    type=str,
                    help='True or false param',
                    )
# required=False

def url_maker(schema, host, path,brows):
    return schema + "://" + host + path + brows

args = parser.parse_args()

print(url_maker(args.schema, args.host, args.path,args.brows))
print(type(args.brows))