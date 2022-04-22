from lxml import etree


class Design:

    def __init__(self, name, description) -> None:
        self.name = name
        self.description = description

    def load(self, xml_data: etree):
        self.name = xml_data.find('Name')

    def save(self, xml_parent: etree):

        xml_design = etree.SubElement(xml_parent, 'Design')
        etree.SubElement(xml_design, 'Name').text = self.name
