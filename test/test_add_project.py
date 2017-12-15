from model.project import Project

project = Project(name='test_project3', status='release', view_status='public')
username = "administrator"
password = "root"

def test_add_project(app, db):
    app.session.login(username, password)
    old_projects = db.get_project_list()
    app.project.create_project(project)
    new_projects = db.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key = Project.id_or_max) == sorted(new_projects, key = Project.id_or_max)
    app.session.logout()

def test_add_project_with_soap_checking(app, soap):
    old_projects = soap.get_projects(username, password)
    app.project.create_project(project)
    new_projects = soap.get_projects(username, password)
    old_projects.append(project)
    assert sorted(old_projects, key = Project.id_or_max) == sorted(new_projects, key = Project.id_or_max)