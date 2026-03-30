import os
from flask import Flask, render_template, request, jsonify
from config import Config

def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    @app.route('/')
    def home():
        return render_template('base.html', active_page='home')

    @app.route('/about')
    def about():
        return render_template('about.html', active_page='about')

    @app.route('/portfolio')
    def portfolio():
        return render_template('portfolio.html', active_page='portfolio')

    @app.route('/contact', methods=['GET', 'POST'])
    def contact():
        if request.method == 'POST':
            data = request.json
            # Simple validation
            if not all(k in data for k in ('name', 'email', 'message')):
                return jsonify({'error': 'All fields required'}), 400
            # Log contact (in production, send email)
            print(f"Contact from {data['name']} ({data['email']}): {data['message']}")
            return jsonify({'success': True}), 200
        return render_template('contact.html', active_page='contact')

    return app

if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
