import click
import re

@click.command()
@click.option('--exclude', '-e', multiple=True, help='name of a tag to exclude')
@click.argument('input_file', default='world', required=True)
def main(exclude, input_file):

    in_section = []

    with open(input_file) as f:
        content = f.readlines()

        for line in content:

            match_obj = re.match(r'<!-- (START|END):(.*) -->', line, re.M | re.I)

            if match_obj:
                if match_obj.group(1).upper() == "START":
                    # Add this new section to the list
                    in_section.append(match_obj.group(2).upper())

                elif match_obj.group(1).upper() == "END":
                    # Remove the section from the list
                    in_section.remove(match_obj.group(2).upper())

            else:
                # Check if we should print the next line
                if not(set(in_section).intersection(exclude)):
                    print(line, end="")

main()
