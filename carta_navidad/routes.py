from flask import Flask, render_template, request, redirect, url_for, flash, jsonify
from .services import cartas_data
import os

def init_app(app):

    @app.route('/')
    def index():
        """Página principal con formulario navideño"""
        return render_template('inicio.html')

    @app.route('/verificar', methods=['POST'])
    def verificar_carta():
        """Procesa el formulario y redirige a la carta correspondiente"""
        nombre = request.form.get('nombre', '').strip()
        fecha = request.form.get('fecha', '').strip()
        
        if not nombre or not fecha:
            flash('Por favor completa todos los campos', 'error')
            return redirect(url_for('index'))
        
        # Buscar carta
        resultado = cartas_data.buscar_carta(nombre, fecha)
        
        if resultado['encontrada']:
            carta = resultado['data']
            flash(f'¡Hola {carta["destinatario"]}! Redirigiendo a tu carta...', 'success')
            return redirect(url_for('mostrar_carta', carta_id=carta['carta_id']))
        else:
            flash('No se encontró una carta para esta combinación de nombre y fecha. Comunicate con el creador', 'error')
            return redirect(url_for('index'))

    @app.route('/carta/<carta_id>')
    def mostrar_carta(carta_id):
        """Muestra una carta específica"""
        carta = cartas_data.obtener_carta_por_id(carta_id)
        
        if not carta:
            flash('Carta no encontrada', 'error')
            return redirect(url_for('index'))
        
        return render_template('carta.html', carta=carta)

    @app.route('/api/verificar-carta', methods=['POST'])
    def api_verificar_carta():
        """API endpoint para verificación AJAX (opcional)"""
        data = request.get_json()
        nombre = data.get('nombre', '').strip()
        fecha = data.get('fecha', '').strip()
        
        resultado = cartas_data.buscar_carta(nombre, fecha)
        
        if resultado['encontrada']:
            carta = resultado['data']
            return jsonify({
                'encontrada': True,
                'carta_id': carta['carta_id'],
                'nombre_personalizado': carta['destinatario'],
                'url_redireccion': url_for('mostrar_carta', carta_id=carta['carta_id'])
            })
        else:
            return jsonify({
                'encontrada': False,
                'mensaje': 'No se encontró una carta para esta combinación'
            })