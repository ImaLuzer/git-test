
from jinja2 import Template 

example_text = """
Some text with expressions {{ 3 + 13 }}
Some text with a variable {{ VAR }}
"""

my_template = example_text

j2_template = Template(my_template)

output = j2_template.render(VAR=2)

print(output)



