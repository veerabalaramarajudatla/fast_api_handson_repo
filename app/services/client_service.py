from app.model.client import Client

def create_client(db, client):
    new_client = Client(
        client_name=client.client_name
    )
    db.add(new_client)
    db.commit()
    db.refresh(new_client)
    return new_client

def get_all_clients(db):
    return db.query(Client).all()


def get_client_by_id(db, client_id):
    return (
        db.query(Client)
        .filter(Client.client_id == client_id)
        .first()
    )