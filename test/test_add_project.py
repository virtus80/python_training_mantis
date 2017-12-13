from model.project import Project

project = Project(name='test_project', status='release', view_status='public')

def test_add_project(app, db):
    old_projects = db.get_project_list()
    app.project.create_project(project)
    new_projects = db.get_project_list()
    old_projects.append(project)
    assert sorted(old_projects, key = Project.id_or_max) == sorted(new_projects, key = Project.id_or_max)