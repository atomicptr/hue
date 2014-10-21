from webcolors import hex_to_name

def push_colors(handler, hex_query, rgb):
    handler.add_new_item(title=hex_query, subtitle="Hex")

    try:
        name = hex_to_name(hex_query, spec='css3')
        handler.add_new_item(title="color: %s;" % name, subtitle="CSS3")
    except ValueError:
        pass

    handler.add_new_item(title="rgb(%s, %s, %s)" % rgb, subtitle="RGB")