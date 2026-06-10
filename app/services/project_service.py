from app.model.project import Project

def create_project(db, project):
    new_project = Project(project_name=project.project_name,client_id=project.client_id)
    db.add(new_project)
    db.commit()
    db.refresh(new_project)
    return new_project

def get_all_projects(db):
    return db.query(Project).all()

def get_project_by_id(db, project_id):
    return (db.query(Project).filter(Project.project_id == project_id).first())

def get_projects_by_client(db, client_id):
    return (db.query(Project).filter(Project.client_id == client_id).all())