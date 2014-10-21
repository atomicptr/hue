import sys
import Alfred
from webcolors import normalize_hex, hex_to_rgb
from printer import push_colors

handler = Alfred.Handler(args=sys.argv)

try:
    hex_query = normalize_hex("#%s" % sys.argv[1])

    rgb = hex_to_rgb(hex_query)

    push_colors(handler, hex_query.upper(), rgb)
except:
    handler.add_new_item(title="...")

handler.push()
