#!/usr/bin/env python3
"""
Script d'installation automatique pour le projet Compteur de Doigts
"""

import subprocess
import sys
import os

def run_command(command, description):
    """Exécute une commande système avec gestion d'erreur"""
    print(f"📦 {description}...")
    try:
        result = subprocess.run(command, shell=True, check=True, capture_output=True, text=True)
        print(f"✅ {description} - Terminé")
        return True
    except subprocess.CalledProcessError as e:
        print(f"❌ Erreur lors de {description}")
        print(f"Sortie d'erreur: {e.stderr}")
        return False

def check_python_version():
    """Vérifie la version de Python"""
    print("🔍 Vérification de la version Python...")
    version = sys.version_info
    if version.major == 3 and version.minor >= 8:
        print(f"✅ Python {version.major}.{version.minor}.{version.micro} - Compatible")
        return True
    else:
        print(f"❌ Python {version.major}.{version.minor}.{version.micro} - Version trop ancienne")
        print("⚠️  Python 3.8+ requis")
        return False

def install_requirements():
    """Installe les dépendances depuis requirements.txt"""
    if not os.path.exists("requirements.txt"):
        print("❌ Fichier requirements.txt non trouvé")
        return False
    
    return run_command(
        f"{sys.executable} -m pip install -r requirements.txt",
        "Installation des dépendances"
    )

def test_imports():
    """Teste l'importation des modules principaux"""
    print("🧪 Test des importations...")
    modules_to_test = [
        ("streamlit", "Streamlit"),
        ("cv2", "OpenCV"),
        ("mediapipe", "MediaPipe"),
        ("ultralytics", "YOLO/Ultralytics"),
        ("numpy", "NumPy")
    ]
    
    all_good = True
    for module, name in modules_to_test:
        try:
            __import__(module)
            print(f"  ✅ {name}")
        except ImportError:
            print(f"  ❌ {name} - Non installé")
            all_good = False
    
    return all_good

def download_yolo_model():
    """Télécharge le modèle YOLO si nécessaire"""
    print("🤖 Préparation du modèle YOLO...")
    try:
        from ultralytics import YOLO
        model = YOLO('yolov8n.pt')  # Télécharge automatiquement si nécessaire
        print("✅ Modèle YOLO prêt")
        return True
    except Exception as e:
        print(f"⚠️  Avertissement: {e}")
        print("   Le modèle YOLO sera téléchargé au premier lancement")
        return True

def main():
    """Fonction principale d'installation"""
    print("🚀 Installation du Compteur de Doigts")
    print("=" * 50)
    
    # Vérifier Python
    if not check_python_version():
        sys.exit(1)
    
    # Installer les dépendances
    if not install_requirements():
        print("❌ Échec de l'installation des dépendances")
        sys.exit(1)
    
    # Tester les importations
    if not test_imports():
        print("❌ Certains modules ne peuvent pas être importés")
        print("💡 Essayez de relancer l'installation ou installez manuellement:")
        print("   pip install -r requirements.txt")
        sys.exit(1)
    
    # Préparer YOLO
    download_yolo_model()
    
    print("\n" + "=" * 50)
    print("🎉 Installation terminée avec succès!")
    print("\n📋 Prochaines étapes:")
    print("   1. streamlit run app.py           (Version MediaPipe)")
    print("   2. streamlit run app_yolo.py      (Version avec YOLO)")
    print("\n🌐 L'application s'ouvrira dans votre navigateur à:")
    print("   http://localhost:8501")
    print("\n📖 Consultez README.md pour plus d'informations")

if __name__ == "__main__":
    main()