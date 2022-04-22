import os
from src.model.project import Project
from src.model.design import Design

test_path = 'text.xml'

if os.path.isfile(test_path):
    my_project = Project(test_path)
    print(my_project)

my_project = Project(test_path, 'proj name', 'proj desc')

my_design = Design('des name', 'des desc')
my_project.save()
