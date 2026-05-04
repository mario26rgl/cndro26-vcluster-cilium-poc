#!/usr/bin/env python3
import psutil
import socket
import os
from datetime import datetime
from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/health', methods=['GET'])
def health():
    """Health check endpoint."""
    return jsonify({'status': 'OK'}), 200

@app.route('/metrics', methods=['GET'])
def metrics():
    """System metrics endpoint."""
    try:
        # CPU metrics
        cpu_percent = psutil.cpu_percent(interval=1)
        cpu_count = psutil.cpu_count(logical=True)
        
        # Memory metrics
        memory = psutil.virtual_memory()
        memory_percent = memory.percent
        memory_used_mb = memory.used / (1024 * 1024)
        memory_total_mb = memory.total / (1024 * 1024)
        
        # Container metadata
        hostname = socket.gethostname()
        pid = os.getpid()
        timestamp = datetime.utcnow().isoformat()
        
        return jsonify({
            'status': 'OK',
            'timestamp': timestamp,
            'container': {
                'hostname': hostname,
                'pid': pid
            },
            'cpu': {
                'percent': cpu_percent,
                'count': cpu_count
            },
            'memory': {
                'percent': memory_percent,
                'used_mb': round(memory_used_mb, 2),
                'total_mb': round(memory_total_mb, 2)
            }
        }), 200
    except Exception as e:
        return jsonify({'status': 'error', 'message': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80, debug=False)
