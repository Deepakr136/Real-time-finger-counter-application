#!/usr/bin/env python3
"""
Script de lancement rapide pour le Compteur de Doigts
"""

import subprocess
import sys
import os
import webbrowser
import time

def run_streamlit_app(app_file):
    """Lance l'application Streamlit"""
    if not os.path.exists(app_file):
        print(f"❌ Fichier {app_file} non trouvé")
        return False
    
    print(f"🚀 Lancement de {app_file}...")
    print("⏳ Démarrage du serveur Streamlit...")
    
    try:
        # Lancer Streamlit
        process = subprocess.Popen([
            sys.executable, "-m", "streamlit", "run", app_file,
            "--server.headless", "true",
            "--server.port", "8501"
        ])
        
        # Attendre un peu que le serveur démarre
        time.sleep(3)
        
        # Ouvrir le navigateur
        url = "http://localhost:8501"
        print(f"🌐 Ouverture de {url}")
        webbrowser.open(url)
        
        print("\n" + "="*50)
        print("✅ Application lancée avec succès!")
        print("🖐️  Montrez vos mains à la webcam pour commencer")
        print("⏹️  Appuyez sur Ctrl+C pour arrêter")
        print("="*50 + "\n")
        
        # Attendre l'interruption
        process.wait()
        
    except KeyboardInterrupt:
        print("\n⏹️  Arrêt de l'application...")
        process.terminate()
    except Exception as e:
        print(f"❌ Erreur: {e}")
        return False
    
    return True

def main():
    """Menu principal"""
    print("🖐️ Compteur de Doigts - Lanceur")
    print("=" * 40)
    print("Choisissez une version:")
    print("1. Version MediaPipe (recommandée)")
    print("2. Version avec YOLO + MediaPipe")
    print("3. Installer les dépendances")
    print("4. Quitter")
    
    try:
        choice = input("\nVotre choix (1-4): ").strip()
        
        if choice == "1":
            run_streamlit_app("app.py")
        elif choice == "2":
            run_streamlit_app("app_yolo.py")
        elif choice == "3":
            print("📦 Lancement de l'installation...")
            subprocess.run([sys.executable, "install.py"])
        elif choice == "4":
            print("👋 Au revoir!")
        else:
            print("❌ Choix invalide")
            
    except KeyboardInterrupt:
        print("\n👋 Au revoir!")
    except Exception as e:
        print(f"❌ Erreur: {e}")

if __name__ == "__main__":
    main()