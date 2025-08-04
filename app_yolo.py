import streamlit as st
import cv2
import numpy as np
import mediapipe as mp
from ultralytics import YOLO
import tempfile
import os

class YOLOFingerCounter:
    def __init__(self):
        # MediaPipe pour le comptage des doigts
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )
        self.mp_drawing = mp.solutions.drawing_utils
        
        # YOLO pour la détection d'objets (optionnel, pour détecter des personnes)
        try:
            self.yolo_model = YOLO('yolov8n.pt')  # Modèle léger
        except:
            self.yolo_model = None
            st.warning("⚠️ Modèle YOLO non disponible. Utilisation de MediaPipe uniquement.")
        
    def count_fingers(self, landmarks):
        """Compte le nombre de doigts levés basé sur les landmarks de la main"""
        finger_tips = [4, 8, 12, 16, 20]  # Index des bouts des doigts
        finger_pip = [3, 6, 10, 14, 18]   # Index des articulations PIP
        
        fingers_up = []
        
        # Pouce (logique différente car il se déplace horizontalement)
        if landmarks[finger_tips[0]].x > landmarks[finger_pip[0]].x:
            fingers_up.append(1)
        else:
            fingers_up.append(0)
            
        # Autres doigts (ils se déplacent verticalement)
        for i in range(1, 5):
            if landmarks[finger_tips[i]].y < landmarks[finger_pip[i]].y:
                fingers_up.append(1)
            else:
                fingers_up.append(0)
                
        return sum(fingers_up)
    
    def detect_persons(self, frame):
        """Utilise YOLO pour détecter les personnes dans le frame"""
        if self.yolo_model is None:
            return frame, 0
            
        try:
            results = self.yolo_model(frame, verbose=False)
            person_count = 0
            
            for result in results:
                boxes = result.boxes
                if boxes is not None:
                    for box in boxes:
                        cls = int(box.cls[0])
                        if cls == 0:  # Classe 'person' dans COCO
                            person_count += 1
                            # Dessiner la boîte englobante
                            x1, y1, x2, y2 = box.xyxy[0].cpu().numpy().astype(int)
                            cv2.rectangle(frame, (x1, y1), (x2, y2), (0, 255, 255), 2)
                            cv2.putText(frame, f'Personne {box.conf[0]:.2f}', 
                                      (x1, y1-10), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (0, 255, 255), 1)
            
            return frame, person_count
        except Exception as e:
            return frame, 0

def main():
    st.set_page_config(
        page_title="Compteur de Doigts avec YOLO",
        page_icon="✋",
        layout="wide"
    )
    
    st.title("🖐️ Compteur de Doigts avec YOLO + MediaPipe")
    st.markdown("---")
    
    # Sidebar pour les paramètres
    st.sidebar.title("Paramètres")
    confidence_threshold = st.sidebar.slider(
        "Seuil de confiance MediaPipe", 
        min_value=0.1, 
        max_value=1.0, 
        value=0.7, 
        step=0.05
    )
    
    use_yolo = st.sidebar.checkbox("Utiliser YOLO pour détecter les personnes", value=True)
    show_fps = st.sidebar.checkbox("Afficher les FPS", value=False)
    
    # Initialiser le compteur de doigts
    finger_counter = YOLOFingerCounter()
    
    # Colonnes pour l'affichage
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📹 Webcam avec IA")
        run = st.checkbox('Démarrer la webcam')
        FRAME_WINDOW = st.image([])
        
    with col2:
        st.subheader("📊 Résultats")
        finger_count_display = st.empty()
        hand_count_display = st.empty()
        person_count_display = st.empty()
        fps_display = st.empty()
        status_display = st.empty()
    
    if run:
        # Initialiser la capture vidéo
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            st.error("Impossible d'accéder à la webcam!")
            return
            
        # Configuration de la webcam
        cap.set(cv2.CAP_PROP_FRAME_WIDTH, 640)
        cap.set(cv2.CAP_PROP_FRAME_HEIGHT, 480)
        
        # Variables pour FPS
        frame_count = 0
        fps = 0
        
        while run:
            ret, frame = cap.read()
            
            if not ret:
                st.error("Erreur lors de la lecture de la webcam")
                break
                
            frame_count += 1
            
            # Flip horizontal pour effet miroir
            frame = cv2.flip(frame, 1)
            
            # Détection YOLO des personnes
            person_count = 0
            if use_yolo:
                frame, person_count = finger_counter.detect_persons(frame)
            
            # Conversion BGR vers RGB pour MediaPipe
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Détection des mains avec MediaPipe
            results = finger_counter.hands.process(rgb_frame)
            
            total_fingers = 0
            hand_count = 0
            
            if results.multi_hand_landmarks:
                hand_count = len(results.multi_hand_landmarks)
                
                for hand_landmarks in results.multi_hand_landmarks:
                    # Dessiner les landmarks
                    finger_counter.mp_drawing.draw_landmarks(
                        frame, hand_landmarks, finger_counter.mp_hands.HAND_CONNECTIONS
                    )
                    
                    # Compter les doigts pour cette main
                    fingers = finger_counter.count_fingers(hand_landmarks.landmark)
                    total_fingers += fingers
                    
                    # Afficher le nombre de doigts près de la main
                    h, w, c = frame.shape
                    cx = int(hand_landmarks.landmark[9].x * w)
                    cy = int(hand_landmarks.landmark[9].y * h)
                    
                    cv2.putText(frame, str(fingers), (cx-30, cy-30), 
                              cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            # Afficher les informations sur l'image
            info_y = 30
            cv2.putText(frame, f'Doigts: {total_fingers}', (10, info_y), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
            info_y += 30
            cv2.putText(frame, f'Mains: {hand_count}', (10, info_y), 
                       cv2.FONT_HERSHEY_SIMPLEX, 0.7, (255, 0, 0), 2)
            
            if use_yolo and person_count > 0:
                info_y += 30
                cv2.putText(frame, f'Personnes: {person_count}', (10, info_y), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 255), 2)
            
            if show_fps and frame_count > 30:  # Calculer FPS après quelques frames
                fps = 30  # Approximation
                cv2.putText(frame, f'FPS: {fps}', (frame.shape[1]-100, 30), 
                           cv2.FONT_HERSHEY_SIMPLEX, 0.7, (0, 255, 0), 2)
            
            # Mettre à jour l'affichage Streamlit
            FRAME_WINDOW.image(frame, channels="BGR")
            
            # Mettre à jour les métriques
            with col2:
                finger_count_display.metric("🖐️ Total Doigts", total_fingers)
                hand_count_display.metric("👐 Nombre de Mains", hand_count)
                
                if use_yolo:
                    person_count_display.metric("👤 Personnes Détectées", person_count)
                
                if show_fps:
                    fps_display.metric("⚡ FPS", fps)
                
                if hand_count > 0:
                    status_display.success("✅ Mains détectées!")
                elif person_count > 0:
                    status_display.info("👤 Personne détectée - montrez vos mains!")
                else:
                    status_display.info("⏳ Montrez-vous à la caméra")
        
        cap.release()
    
    # Section d'informations
    st.markdown("---")
    st.subheader("🤖 Technologies IA")
    
    col1, col2 = st.columns(2)
    
    with col1:
        st.markdown("""
        **MediaPipe (Google)**
        - Détection des mains en temps réel
        - Tracking des 21 points de repère
        - Comptage précis des doigts
        """)
    
    with col2:
        st.markdown("""
        **YOLO (Ultralytics)**
        - Détection d'objets en temps réel
        - Reconnaissance des personnes
        - Optimisé pour la performance
        """)
    
    st.markdown("---")
    st.subheader("ℹ️ Instructions")
    st.markdown("""
    1. **Activez les fonctionnalités** dans la barre latérale
    2. **Démarrez la webcam** pour commencer la détection
    3. **Placez-vous** devant la caméra (YOLO vous détectera)
    4. **Montrez vos mains** et levez vos doigts
    5. **L'IA compte** automatiquement vos doigts !
    """)

if __name__ == "__main__":
    main()