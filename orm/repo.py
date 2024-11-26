import orm.modelos as modelos
from sqlalchemy.orm import Session

# Esta función es llamada por api.py
# Para atender GET '/usuarios/(id)'
# select * from usuarios where id = id_usuarios
def usuario_por_id(session:Session, id_usuario:int):
    print("Select * from app.usuarios where id = ", id_usuario)
    return sesion.query(modelos.Usuario).filter(modelos.Usuario.id==id_usuario).first()

def compra_por_id(session:Session, id_compra:int):
    print("Select * from app.compras where id = ", id_compras)
    return sesion.query(modelos.Compra).filter(modelos.Compra.id==id_compra).first()

def foto_por_id(session:Session, id_foto:int):
    print("Select * from app.fotos where id = ", id_foto)
    return session.query(modelos.Foto).filter(modelos.Foto.id==id_foto).first()