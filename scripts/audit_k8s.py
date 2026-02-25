import yaml
import sys
import os

def check_infra():
    print(f"--- Iniciando revisión de seguridad para {os.getenv('AUDITOR')} ---")
    try:
        with open('k8s/deployment.yaml', 'r') as file:
            config = yaml.safe_load(file)
            container = config['spec']['template']['spec']['containers'][0]
            
            if 'resources' not in container:
                print("❌ ERROR: Faltan límites de recursos (CPU/RAM).")
                sys.exit(1)
            
            print("✅ Configuración validada correctamente.")
    except Exception as e:
        print(f"❌ Error en el archivo: {e}")
        sys.exit(1)

if __name__ == "__main__":
    check_infra()
