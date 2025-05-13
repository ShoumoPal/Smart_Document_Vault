from sqlalchemy.orm import Session
from models import VaultDB, VaultItem, CreateVaultItem

def add_to_vault(db: Session, item : CreateVaultItem):
    db_vaultitem = VaultDB(summary=item.summary, filename=item.filename, tags = item.tags)
    db.add(db_vaultitem)
    db.commit()
    db.refresh(db_vaultitem)
    return db_vaultitem

def delete_from_vault(db:Session, id : int):
    db_vaultitem = db.query(VaultDB).filter(VaultDB.id == id).first()
    if db_vaultitem is None:
        return None
    
    db.delete(db_vaultitem)
    db.commit()

    return db_vaultitem

def get_from_vault(db:Session):
    return db.query(VaultDB).all()