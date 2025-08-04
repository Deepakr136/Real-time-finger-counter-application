import streamlit as st
import cv2
import numpy as np
import mediapipe as mp
import tempfile
import os

class FingerCounter:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=False,
            max_num_hands=2,
            min_detection_confidence=0.7,
            min_tracking_confidence=0.5
        )
        self.mp_drawing = mp.solutions.drawing_utils
        
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

def main():
    st.set_page_config(
        page_title="Compteur de Doigts",
        page_icon="✋",
        layout="wide"
    )
    
    st.title("🖐️ Compteur de Doigts en Temps Réel")
    st.markdown("---")
    
    # Sidebar pour les paramètres
    st.sidebar.title("Paramètres")
    confidence_threshold = st.sidebar.slider(
        "Seuil de confiance", 
        min_value=0.1, 
        max_value=1.0, 
        value=0.7, 
        step=0.05
    )
    
    # Initialiser le compteur de doigts
    finger_counter = FingerCounter()
    
    # Colonnes pour l'affichage
    col1, col2 = st.columns([2, 1])
    
    with col1:
        st.subheader("📹 Webcam")
        run = st.checkbox('Démarrer la webcam')
        FRAME_WINDOW = st.image([])
        
    with col2:
        st.subheader("📊 Résultats")
        finger_count_display = st.empty()
        hand_count_display = st.empty()
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
        
        while run:
            ret, frame = cap.read()
            
            if not ret:
                st.error("Erreur lors de la lecture de la webcam")
                break
                
            # Flip horizontal pour effet miroir
            frame = cv2.flip(frame, 1)
            
            # Conversion BGR vers RGB pour MediaPipe
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            # Détection des mains
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
            cv2.putText(frame, f'Total Doigts: {total_fingers}', (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            cv2.putText(frame, f'Mains: {hand_count}', (10, 70), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            
            # Mettre à jour l'affichage Streamlit
            FRAME_WINDOW.image(frame, channels="BGR")
            
            # Mettre à jour les métriques
            with col2:
                finger_count_display.metric("🖐️ Total Doigts", total_fingers)
                hand_count_display.metric("👐 Nombre de Mains", hand_count)
                
                if hand_count > 0:
                    status_display.success("✅ Mains détectées!")
                else:
                    status_display.info("⏳ Montrez vos mains à la caméra")
        
        cap.release()
    
    # Section d'informations
    st.markdown("---")
    st.subheader("ℹ️ Instructions")
    st.markdown("""
    1. **Cliquez sur 'Démarrer la webcam'** pour commencer la détection
    2. **Placez vos mains** devant la caméra
    3. **Levez vos doigts** pour les compter
    4. **Le système détecte** jusqu'à 2 mains simultanément
    
    **Conseils pour une meilleure détection :**
    - Assurez-vous d'avoir un bon éclairage
    - Gardez vos mains bien visibles dans le cadre
    - Évitez les arrière-plans trop chargés
    """)
    
    st.markdown("---")
    st.markdown("**Technologies:** Python • OpenCV • MediaPipe • Streamlit")

if __name__ == "__main__":
    main()