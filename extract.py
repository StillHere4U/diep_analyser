import os
import numpy as np
from PIL import Image
import pydicom
from pydicom.dataset import Dataset
from pydicom.uid import generate_uid

# Chemin de l'image sans extension
image_path = "scan_image"  # Modifier le chemin

# Étape 1: Lire l'image
# Tenter de lire l'image en utilisant PIL (en supposant que c'est une image PNG/JPG)
try:
    image = Image.open(image_path)
except Exception as e:
    print(f"Erreur lors de la lecture de l'image : {e}")
    exit()

# Convertir l'image en un tableau numpy
image_array = np.array(image)

# Étape 2: Créer un fichier DICOM
dcm = Dataset()

# Remplir le dataset DICOM avec les informations de base
dcm.PatientName = "Nom_du_patient"
dcm.PatientID = "ID_du_patient"
dcm.Modality = "CT"  # Type de scan (CT, si c'est une tomodensitométrie)
dcm.StudyDescription = "Scan Thoracique"
dcm.SeriesDescription = "Scan Thoracique"

# Remplir les informations spécifiques au fichier DICOM
dcm.SamplesPerPixel = 1
dcm.PhotometricInterpretation = "MONOCHROME2"
dcm.Rows, dcm.Columns = image_array.shape
dcm.PixelSpacing = [1.0, 1.0]  # Ajuster la valeur selon votre image
dcm.PixelData = image_array.tobytes()

# Générer un UID unique pour cette instance
dcm.SOPInstanceUID = generate_uid()

# Ajouter d'autres informations si nécessaire...

# Étape 3: Sauvegarder le fichier DICOM
output_dcm_path = "scan_image.dcm"
dcm.save_as(output_dcm_path)

print(f"Le fichier DICOM a été enregistré sous {output_dcm_path}")