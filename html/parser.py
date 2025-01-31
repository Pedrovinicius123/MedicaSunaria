import os

class Html:
    def __init__(self, structure:dict={}, language_template:str='"en"', charset:str='"UTF-8"', meta_name:str='"viewport"', content='"width=device-width, initial-scale=1.0"', title:str="DOCUMENT"):
        self.structure = {
            "!DOCTYPE html": 0,
            "html":{
                "lang":language_template,
                "meta": {
                    "charset": charset
                },
                "meta":{
                    "name": meta_name
                    "content": content
                },
                "title": { "":title }
            },
            "body": structure

        }

        self.tags_without_close = [
            "area", "base", "br", "col", "command", "embed", 
            "hr", "img", "input", "keygen", "link", "menuitem", 
            "meta", "param", "source", "track", "wbr", "meta", "!DOCTYPE html"
        ]

    def write_to_html(self, parent_directory:str, filename:str):
        if parent_directory not in os.listdir():
            os.mkdir(f"{parent_directory}")

        with open(os.path.join(parent_directory, filename), 'w') as file:
            file.writelines(self.parse_structure_to_html(structure=self.structure))

    def parse_structure_to_html(self, structure:dict={}, indentation_level:int=0) -> list:
        """NOTE: DO NOT CHANGE THE INITIAL INDENTATION LEVEL"""

        lines = []
        for key, value in structure.items():
            if key != "":
                lines.append(""*indentation_level+f"<{key}>\n")

                if value != 0 and not isinstance(value, str):
                    lines.extend(self.parse_structure_to_html(value, indentation_level + 4))

                elif isinstance(value, str):
                    lines.extend(value)

                if key not in self.tags_without_close:
                    lines.append(""*indentation_level+f"\n</{key}>")

            else:
                lines.append(""*indentation_level*2+f"\n")

        return lines
