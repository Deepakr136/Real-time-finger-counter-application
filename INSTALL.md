# 📦 Guide d'Installation

## 🚀 Installation Rapide

### Option 1: Installation automatique
```bash
python3 install.py
```

### Option 2: Installation manuelle

1. **Installer les dépendances Python**
   ```bash
   pip3 install streamlit==1.29.0
   pip3 install opencv-python==4.8.1.78
   pip3 install ultralytics==8.0.196
   pip3 install mediapipe==0.10.7
   pip3 install numpy==1.24.3
   pip3 install pillow==10.0.1
   ```

2. **Ou utiliser requirements.txt**
   ```bash
   pip3 install -r requirements.txt
   ```

## 🎯 Lancement

### Méthode 1: Script de lancement
```bash
python3 run.py
```

### Méthode 2: Directement avec Streamlit
```bash
# Version MediaPipe (recommandée)
streamlit run app.py

# Version avec YOLO
streamlit run app_yolo.py
```

## 🔧 Dépannage

### Erreur "Module not found"
```bash
# Vérifier l'installation de pip
python3 -m pip --version

# Installer pip si nécessaire (Ubuntu/Debian)
sudo apt update
sudo apt install python3-pip

# Réinstaller les dépendances
pip3 install --upgrade -r requirements.txt
```

### Problème avec OpenCV
```bash
# Si opencv-python ne fonctionne pas, essayer:
pip3 uninstall opencv-python
pip3 install opencv-python-headless
```

### Erreur de webcam
- Vérifiez que votre webcam est connectée
- Fermez les autres applications utilisant la caméra
- Sur Linux, vérifiez les permissions:
  ```bash
  sudo usermod -a -G video $USER
  # Puis redémarrez votre session
  ```

### Performance YOLO lente
- Le modèle YOLO se télécharge automatiquement au premier lancement
- Pour de meilleures performances, utilisez la version MediaPipe seule

## 📋 Vérification

Testez que tout fonctionne:
```bash
python3 -c "import streamlit, cv2, mediapipe, numpy; print('✅ Tous les modules sont prêts!')"
```

## 🌐 Accès à l'application

Une fois lancée, l'application sera disponible à:
- **URL locale**: http://localhost:8501
- **Réseau local**: http://[votre-ip]:8501

## ⚡ Performance

### Configuration recommandée
- Python 3.8+
- 4 GB RAM minimum
- Webcam 720p ou mieux
- Bon éclairage

### Optimisation
- Fermez les autres applications lourdes
- Utilisez un arrière-plan uni
- Évitez les mouvements brusques