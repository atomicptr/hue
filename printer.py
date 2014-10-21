from webcolors import hex_to_name

def push_colors(handler, hex_query, rgb):
    handler.add_new_item(title=hex_query, subtitle="Hex", arg=hex_query)

    try:
        name = hex_to_name(hex_query, spec='css3')

        css3_color = "color: %s;" % name

        handler.add_new_item(title=css3_color, subtitle="CSS3", arg=css3_color)
    except ValueError:
        pass

    rgb_str = "rgb(%s, %s, %s)" % rgb

    handler.add_new_item(title=rgb_str, subtitle="RGB", arg=rgb_str)