from textnode import TextType, TextNode


def split_nodes_delimiter(old_nodes, delimiter, text_type):
    output = []
    for node in old_nodes:
        match node.text_type:
            case node.text_type.TEXT:
                s = node.text.split(delimiter)
                if len(s) % 2 == 0:
                    raise Exception(
                        f"Invalid Markdown sintax, did you close the delimiter")
                for index, item in enumerate(s):
                    if item == "":
                        continue
                    if index % 2 == 0:
                        output.append(TextNode(item, TextType.TEXT))
                    else:
                        output.append(TextNode(item, text_type))

            case _:
                output.append(node)
    return output
