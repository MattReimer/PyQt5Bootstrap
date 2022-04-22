import os
# from collections import UserDict
from lxml import etree

from src.model.design import Design


class Project:

    def __init__(self, *args) -> None:

        self.name = ''
        self.description = ''
        self.designs = {}

        if len(args) == 1:
            # Existing project XML file path

            self.project_xml_path = args[0]
            if not os.path.isfile(self.project_xml_path):
                raise Exception('Project file does not exist at {}'.format(self.project_xml_path))

            self.load()
        else:
            # New project file
            self.project_xml_path = args[0]
            self.name = args[1]
            self.description = args[2]
            self.save()

    def load(self):
        # load the elements

        self.designs = {}
        xml_project = etree.parse(self.project_xml_path).getroot()

        self.name = xml_project.find('Name')
        self.description = xml_project.find('Description')

        for xml_design in xml_project.findall('Designs/Design'):
            design = Design('place holder', 'desc')
            design.load(xml_design)

    def save(self):
        # save the elements

        xml_project = etree.Element('Project')
        etree.SubElement(xml_project, 'Name').text = self.name
        etree.SubElement(xml_project, 'Description').text = self.description

        # Designs
        xml_designs = etree.SubElement(xml_project, 'Designs')
        [design.save(xml_designs) for _name, design in self.designs.items()]

        with open(self.project_xml_path, 'w') as f:
            f.write(etree.tostring(xml_project, pretty_print=True).decode())
