from model.project import Project

class ProjectHelper:

    def __init__(self, app):
        self.app = app

    def open_manage_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_overview_page.php")):
            wd.find_element_by_link_text("Manage").click()

    def open_manage_project_page(self):
        wd = self.app.wd
        if not (wd.current_url.endswith("/manage_proj_page.php")):
            wd.find_element_by_link_text("Manage Projects").click()

    def create_project(self, project):
        wd = self.app.wd
        self.open_manage_page()
        self.open_manage_project_page()
        # init group creation
        wd.find_element_by_css_selector("input[value='Create New Project']").click()
        self.fill_project_form(project)
        # submit group creation
        wd.find_element_by_css_selector("input[value='Add Project']").click()

    def fill_project_form(self, project):
        self.app.change_field_value("name", project.name)
        self.select_status(project.status)
        self.select_view_status(project.view_status)
        self.app.change_field_value("description", project.description)

    def select_status(self, status):
        wd = self.app.wd
        wd.find_element_by_xpath("//select[@name='status']/option[text()='%s']" %status).click()

    def select_view_status(self, view_status):
        wd = self.app.wd
        wd.find_element_by_xpath("//select[@name='view_state']/option[text()='%s']" % view_status).click()

    def delete_project_by_id(self, id):
        wd = self.app.wd
        self.open_manage_page()
        self.open_manage_project_page()
        self.select_project_by_id(id)
        wd.find_element_by_css_selector("input[value='Delete Project']").click()
        # submit deletion
        wd.find_element_by_css_selector("input[value='Delete Project']").click()

    def select_project_by_id(self, id):
        wd = self.app.wd
        wd.find_element_by_css_selector("a[href='manage_proj_edit_page.php?project_id=%s']" % id).click()