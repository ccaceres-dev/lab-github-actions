import subprocess
import sys
import os

def check_status():
    user = os.getenv('GITHUB_ACTOR', 'Desconocido')
    print(f"--- Verificación de Despliegue iniciada por {user} ---")
    
    # Comando de Kubernetes para esperar a que el despliegue esté listo
    try:
        # En un entorno real, el Runner tendría acceso al cluster vía kubeconfig
        print("Validando estado de los pods para 'web-server'...")
        # Simulamos la validación para el pipeline
        print("✅ Simulación: Rollout exitoso detectado.")
        return True
    except Exception as e:
        print(f"❌ Error en validación: {e}")
        sys.exit(1)

if __name__ == "__main__":
    check_status()
