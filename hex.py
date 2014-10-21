import sys
import Alfred
from webcolors import normalize_hex, hex_to_rgb, hex_to_name

handler = Alfred.Handler(args=sys.argv)

try:
    hex_query = normalize_hex("#%s" % sys.argv[1])

    rgb = hex_to_rgb(hex_query)

    handler.add_new_item(title=hex_query.upper(), subtitle="Hex")
    
    try:
        name = hex_to_name(hex_query, spec='css3')
        handler.add_new_item(title="color: %s;" % name, subtitle="CSS3")
    except ValueError:
        pass   
    
    handler.add_new_item(title="rgb(%s, %s, %s)" % rgb, subtitle="RGB")
except ValueError:
    handler.add_new_item(title="...")

handler.push()
