import sys
import Alfred
from webcolors import normalize_hex, rgb_to_hex
from printer import push_colors

handler = Alfred.Handler(args=sys.argv)

try:
    query = handler.query

    query = query.replace(' ', '')
    query = query.replace('(', '')
    query = query.replace(')', '')

    rgb_raw = query.split(',')

    rgb = (int(rgb_raw[0]), int(rgb_raw[1]), int(rgb_raw[2]))

    hex_val = rgb_to_hex(rgb)

    push_colors(handler, hex_val.upper(), rgb)
except:
    handler.add_new_item(title="...")

handler.push()
