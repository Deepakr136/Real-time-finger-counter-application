"""
Configuration globale pour le Compteur de Doigts
"""

# Configuration MediaPipe
MEDIAPIPE_CONFIG = {
    'static_image_mode': False,
    'max_num_hands': 2,
    'min_detection_confidence': 0.7,
    'min_tracking_confidence': 0.5
}

# Configuration YOLO
YOLO_CONFIG = {
    'model_name': 'yolov8n.pt',  # Modèle léger pour de meilleures performances
    'confidence_threshold': 0.5,
    'device': 'cpu'  # Utiliser 'cuda' si disponible
}

# Configuration Webcam
WEBCAM_CONFIG = {
    'width': 640,
    'height': 480,
    'fps': 30,
    'flip_horizontal': True  # Effet miroir
}

# Configuration Streamlit
STREAMLIT_CONFIG = {
    'page_title': "Compteur de Doigts",
    'page_icon': "✋",
    'layout': "wide",
    'initial_sidebar_state': "expanded"
}

# Couleurs pour l'affichage
COLORS = {
    'finger_count': (0, 255, 0),      # Vert pour le nombre de doigts
    'hand_landmarks': (255, 0, 0),    # Rouge pour les points de la main
    'yolo_bbox': (0, 255, 255),       # Jaune pour les boîtes YOLO
    'text_info': (255, 255, 255),     # Blanc pour le texte
    'text_shadow': (0, 0, 0)          # Noir pour l'ombre du texte
}

# Messages de l'interface
MESSAGES = {
    'no_webcam': "❌ Impossible d'accéder à la webcam!",
    'hands_detected': "✅ Mains détectées!",
    'show_hands': "⏳ Montrez vos mains à la caméra",
    'person_detected': "👤 Personne détectée - montrez vos mains!",
    'show_yourself': "⏳ Montrez-vous à la caméra",
    'yolo_unavailable': "⚠️ Modèle YOLO non disponible. Utilisation de MediaPipe uniquement."
}

# Performance
PERFORMANCE = {
    'max_fps': 30,
    'frame_skip': 1,  # Traiter 1 frame sur n pour améliorer les performances
    'resize_factor': 1.0  # Facteur de redimensionnement des images
}

# Paramètres de détection des doigts
FINGER_DETECTION = {
    'finger_tips': [4, 8, 12, 16, 20],    # Index des bouts des doigts
    'finger_pip': [3, 6, 10, 14, 18],     # Index des articulations PIP
    'thumb_threshold': 0.05,              # Seuil pour la détection du pouce
    'finger_threshold': 0.02              # Seuil pour les autres doigts
}

# Zones d'intérêt pour l'affichage
UI_ZONES = {
    'info_start_y': 30,
    'info_line_height': 30,
    'info_font_scale': 0.7,
    'info_thickness': 2,
    'finger_label_offset': (-30, -30),
    'finger_label_font_scale': 1,
    'finger_label_thickness': 2
}