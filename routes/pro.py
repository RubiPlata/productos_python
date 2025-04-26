from flask import Blueprint, jsonify, request
from controllers.proController import get_all_productos, create_pro, get_producto_by_id, update_producto, delete_producto

producto_bp = Blueprint('productos', __name__)

@producto_bp.route('/productos', methods=['GET'])
def get_productos():
    """
    Obtener todos los productos
    ---
    tags:
      - Productos
    responses:
      200:
        description: Lista de productos
        schema:
          type: array
          items:
            $ref: '#/definitions/Producto'
      500:
        description: Error interno del servidor
    """
    try:
        productos = get_all_productos()
        return jsonify(productos)
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@producto_bp.route('/productos/<int:id>', methods=['GET'])
def get_producto(id):
    """
    Obtener un producto específico por ID
    ---
    tags:
      - Productos
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID del producto
    responses:
      200:
        description: Producto encontrado
        schema:
          $ref: '#/definitions/Producto'
      404:
        description: Producto no encontrado
      500:
        description: Error interno del servidor
    """
    try:
        producto = get_producto_by_id(id)
        if producto:
            return jsonify(producto)
        return jsonify({'message': 'Producto no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@producto_bp.route('/productos', methods=['POST'])
def create_producto():
    """
    Crear un nuevo producto
    ---
    tags:
      - Productos
    parameters:
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/ProductoInput'
    responses:
      201:
        description: Producto creado exitosamente
        schema:
          $ref: '#/definitions/Producto'
      400:
        description: Datos de entrada inválidos
      500:
        description: Error interno del servidor
    """
    try:
        data = request.get_json()
        
        if not data or not all(key in data for key in ['nombre', 'categoria', 'cantidad']):
            return jsonify({'error': 'Datos incompletos'}), 400
            
        nombre = data.get('nombre') 
        categoria = data.get('categoria')
        cantidad = data.get('cantidad')
        
        new_producto = create_pro(nombre, categoria, cantidad)
        return jsonify(new_producto), 201
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@producto_bp.route('/productos/<int:id>', methods=['PUT'])
def update_producto(id):
    """
    Actualizar un producto existente
    ---
    tags:
      - Productos
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID del producto a actualizar
      - in: body
        name: body
        required: true
        schema:
          $ref: '#/definitions/ProductoInput'
    responses:
      200:
        description: Producto actualizado
        schema:
          $ref: '#/definitions/Producto'
      400:
        description: Datos de entrada inválidos
      404:
        description: Producto no encontrado
      500:
        description: Error interno del servidor
    """
    try:
        data = request.get_json()
        
        if not data:
            return jsonify({'error': 'No se proporcionaron datos'}), 400
            
        nombre = data.get('nombre')
        categoria = data.get('categoria')
        cantidad = data.get('cantidad')
        
        updated_producto = update_producto(id, nombre, categoria, cantidad)
        
        if updated_producto:
            return jsonify(updated_producto)
        return jsonify({'message': 'Producto no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@producto_bp.route('/productos/<int:id>', methods=['DELETE'])
def delete_producto(id):
    """
    Eliminar un producto
    ---
    tags:
      - Productos
    parameters:
      - name: id
        in: path
        type: integer
        required: true
        description: ID del producto a eliminar
    responses:
      200:
        description: Producto eliminado
        schema:
          type: object
          properties:
            message:
              type: string
              example: "Producto eliminado exitosamente"
      404:
        description: Producto no encontrado
      500:
        description: Error interno del servidor
    """
    try:
        result = delete_producto(id)
        if result:
            return jsonify({'message': 'Producto eliminado exitosamente'})
        return jsonify({'message': 'Producto no encontrado'}), 404
    except Exception as e:
        return jsonify({'error': str(e)}), 500

# Definiciones Swagger
swagger_definition = {
    'definitions': {
        'Producto': {
            'type': 'object',
            'properties': {
                'id': {
                    'type': 'integer',
                    'example': 1
                },
                'nombre': {
                    'type': 'string',
                    'example': 'Producto Ejemplo'
                },
                'categoria': {
                    'type': 'string',
                    'example': 'Electrónicos'
                },
                'cantidad': {
                    'type': 'integer',
                    'example': 10
                }
            }
        },
        'ProductoInput': {
            'type': 'object',
            'required': ['nombre', 'categoria', 'cantidad'],
            'properties': {
                'nombre': {
                    'type': 'string',
                    'example': 'Producto Ejemplo'
                },
                'categoria': {
                    'type': 'string',
                    'example': 'Electrónicos'
                },
                'cantidad': {
                    'type': 'integer',
                    'example': 10
                }
            }
        }
    }
}