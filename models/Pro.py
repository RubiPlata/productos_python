from config import db

class Pro(db.Model):
    id = db.Column(db.Integer, primary_key= True)
    nombre = db.Column(db.String(50), nullable= False)
    categoria = db.Column(db.String(50), unique= True, nullable= False)
    cantidad = db.Column(db.Integer, unique= True, nullable= False)  
    
    def __init__(self, nombre, categoria, cantidad):
        self.nombre = nombre
        self.categoria = categoria
        self.cantidad = cantidad
    
    def to_dict(self):
        return {
            "id": self.id,
            "nombre": self.nombre,
            "categoria": self.categoria,
            "cantidad": self.cantidad,
        }
        
    
    