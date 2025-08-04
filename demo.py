#!/usr/bin/env python3
"""
Démonstration du compteur de doigts avec images de test
"""

import cv2
import numpy as np
import mediapipe as mp
import os

class FingerCounterDemo:
    def __init__(self):
        self.mp_hands = mp.solutions.hands
        self.hands = self.mp_hands.Hands(
            static_image_mode=True,
            max_num_hands=2,
            min_detection_confidence=0.7
        )
        self.mp_drawing = mp.solutions.drawing_utils
        
    def count_fingers(self, landmarks):
        """Compte le nombre de doigts levés"""
        finger_tips = [4, 8, 12, 16, 20]
        finger_pip = [3, 6, 10, 14, 18]
        
        fingers_up = []
        
        # Pouce
        if landmarks[finger_tips[0]].x > landmarks[finger_pip[0]].x:
            fingers_up.append(1)
        else:
            fingers_up.append(0)
            
        # Autres doigts
        for i in range(1, 5):
            if landmarks[finger_tips[i]].y < landmarks[finger_pip[i]].y:
                fingers_up.append(1)
            else:
                fingers_up.append(0)
                
        return sum(fingers_up)
    
    def create_test_image(self, text, color=(255, 255, 255)):
        """Crée une image de test avec du texte"""
        img = np.zeros((400, 600, 3), dtype=np.uint8)
        cv2.putText(img, text, (50, 200), cv2.FONT_HERSHEY_SIMPLEX, 1, color, 2)
        return img
    
    def demo_with_webcam(self):
        """Démonstration avec webcam si disponible"""
        print("🔍 Recherche de webcam...")
        cap = cv2.VideoCapture(0)
        
        if not cap.isOpened():
            print("❌ Aucune webcam détectée")
            return False
            
        print("📹 Webcam détectée! Appuyez sur 'q' pour quitter")
        
        while True:
            ret, frame = cap.read()
            if not ret:
                break
                
            frame = cv2.flip(frame, 1)
            rgb_frame = cv2.cvtColor(frame, cv2.COLOR_BGR2RGB)
            
            results = self.hands.process(rgb_frame)
            
            total_fingers = 0
            if results.multi_hand_landmarks:
                for hand_landmarks in results.multi_hand_landmarks:
                    self.mp_drawing.draw_landmarks(
                        frame, hand_landmarks, self.mp_hands.HAND_CONNECTIONS
                    )
                    
                    fingers = self.count_fingers(hand_landmarks.landmark)
                    total_fingers += fingers
                    
                    h, w, c = frame.shape
                    cx = int(hand_landmarks.landmark[9].x * w)
                    cy = int(hand_landmarks.landmark[9].y * h)
                    
                    cv2.putText(frame, str(fingers), (cx-30, cy-30), 
                              cv2.FONT_HERSHEY_SIMPLEX, 1, (0, 255, 0), 2)
            
            cv2.putText(frame, f'Total: {total_fingers}', (10, 30), 
                       cv2.FONT_HERSHEY_SIMPLEX, 1, (255, 0, 0), 2)
            
            cv2.imshow('Demo Compteur de Doigts', frame)
            
            if cv2.waitKey(1) & 0xFF == ord('q'):
                break
        
        cap.release()
        cv2.destroyAllWindows()
        return True
    
    def demo_without_webcam(self):
        """Démonstration sans webcam"""
        print("📱 Mode démonstration sans webcam")
        
        # Créer des images de test
        test_images = [
            ("Montrez vos mains!", (255, 255, 255)),
            ("Levez 1 doigt", (0, 255, 0)),
            ("Levez 2 doigts", (0, 255, 255)),
            ("Levez 5 doigts", (255, 0, 255)),
            ("Demo terminee - Appuyez sur une touche", (255, 255, 0))
        ]
        
        for text, color in test_images:
            img = self.create_test_image(text, color)
            cv2.imshow('Demo Compteur de Doigts', img)
            cv2.waitKey(2000)  # Attendre 2 secondes
        
        cv2.destroyAllWindows()

def test_modules():
    """Teste la disponibilité des modules"""
    print("🧪 Test des modules...")
    
    modules = {
        'OpenCV': 'cv2',
        'MediaPipe': 'mediapipe',
        'NumPy': 'numpy'
    }
    
    all_ok = True
    for name, module in modules.items():
        try:
            __import__(module)
            print(f"  ✅ {name}")
        except ImportError:
            print(f"  ❌ {name} - Non installé")
            all_ok = False
    
    return all_ok

def main():
    print("🖐️ Démonstration du Compteur de Doigts")
    print("=" * 50)
    
    # Tester les modules
    if not test_modules():
        print("\n❌ Certains modules manquent.")
        print("💡 Installez les dépendances avec:")
        print("   python3 install.py")
        print("   ou")
        print("   pip3 install -r requirements.txt")
        return
    
    print("\n✅ Tous les modules sont disponibles!")
    
    # Créer le démonstrateur
    demo = FingerCounterDemo()
    
    print("\nChoisissez le mode de démonstration:")
    print("1. Avec webcam (recommandé)")
    print("2. Sans webcam (simulation)")
    print("3. Quitter")
    
    try:
        choice = input("\nVotre choix (1-3): ").strip()
        
        if choice == "1":
            if not demo.demo_with_webcam():
                print("⚠️ Basculement vers le mode simulation")
                demo.demo_without_webcam()
        elif choice == "2":
            demo.demo_without_webcam()
        elif choice == "3":
            print("👋 Au revoir!")
        else:
            print("❌ Choix invalide")
            
    except KeyboardInterrupt:
        print("\n👋 Démonstration interrompue")

if __name__ == "__main__":
    main()