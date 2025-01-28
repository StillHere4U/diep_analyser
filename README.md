# diep_analyser

# Install env and run script
- sudo apt install python3.10-venv
- python3 -m venv .penv
- source .penv/bin/activate
- pip install -r requirements.txt 
- python diep_compute_volume.py

# Get Dicom (.dcm) files:
- Using 3D Slicer export Files to .dcm format using right click on "PERFORANTES" and Export to DICOM
- Copy .zip file into a "dicom/dicom_name" folder into this reporsitory
- Extract data by typing:
    - unzip ./dicom/dicom_name/dicom_name.zip
- Do this fo pre DIEP files and post DIEP files, foolders should looks like :
    └── dicom
        └── pre_dicom
            └── images.dcm
            └── ...
        └── post_dicom
            └── images.dcm
            └── ...
    
- configure pre_config.yaml and post_config.yaml file to add relative path as "dicom/pre_dicom/" (don't forget last "/")
- configure frames, xmin, xmax, ymin and ymax into config files
- run script