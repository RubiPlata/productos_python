from models.Pro import Pro
from flask import jsonify
from config import db

def get_all_productos():
    """Obtiene todos los productos de la base de datos"""
    try:
        productos = Pro.query.all()
        return [pro.to_dict() for pro in productos]
    except Exception as error:
        print(f"ERROR {error}")
        return {'error': str(error)}, 500

def get_producto_by_id(id):
    """Obtiene un producto específico por su ID"""
    try:
        producto = Pro.query.get(id)
        if producto:
            return producto.to_dict()
        return None
    except Exception as error:
        print(f"ERROR {error}")
        return {'error': str(error)}, 500

def create_pro(nombre, categoria, cantidad):
    """Crea un nuevo producto en la base de datos"""
    try:
        new_pro = Pro(nombre=nombre, categoria=categoria, cantidad=cantidad)
        db.session.add(new_pro)
        db.session.commit()
        return new_pro.to_dict()
    except Exception as e:
        db.session.rollback()
        print(f"ERROR {e}")
        return {'error': str(e)}, 500

def update_producto(id, nombre=None, categoria=None, cantidad=None):
    """Actualiza un producto existente"""
    try:
        producto = Pro.query.get(id)
        if not producto:
            return None
            
        if nombre is not None:
            producto.nombre = nombre
        if categoria is not None:
            producto.categoria = categoria
        if cantidad is not None:
            producto.cantidad = cantidad
            
        db.session.commit()
        return producto.to_dict()
    except Exception as e:
        db.session.rollback()
        print(f"ERROR {e}")
        return {'error': str(e)}, 500

def delete_producto(id):
    """Elimina un producto de la base de datos"""
    try:
        producto = Pro.query.get(id)
        if not producto:
            return False
            
        db.session.delete(producto)
        db.session.commit()
        return True
    except Exception as e:
        db.session.rollback()
        print(f"ERROR {e}")
        return {'error': str(e)}, 500