# IDFY_Hackathon_2024
# Project
This projects offers accurate identification and classification of Personally Identifiable Information (PII) within diverse data repositories.
|High Level Diagram|
|---------------------|
| ![WhatsApp Image 2024-09-15 at 21 08 51](https://github.com/user-attachments/assets/661f1ba8-9161-42fe-a5ff-dba105126b0e)|
```bash

Text Model : Finetuned Dliner model
Vision Model : Finetuned Yolo v8 nano

Currently We offer data ingestion from following data sources
├── AWS S3 Bucket  
├── SQL server
├── Local Folder
└── Copy and Paste Text data

We offer two interfaces
├── Web Application  
└── Command line application
```




# Web Application


|Landing Page|Select Your Data|
|---------------------|---------------------|
| ![sc6](https://github.com/user-attachments/assets/6e94b1c8-c455-42ea-9373-df131223480f)|![sc5](https://github.com/user-attachments/assets/92d2d028-8ba0-425e-aea1-ffaacec31d66)|

|Local Folder Search|SQL Server Integration|
|---------------------|---------------------|
|![sc2](https://github.com/user-attachments/assets/d63ac5cb-de90-4eb4-a9e7-8cef59c64033)|![sc3](https://github.com/user-attachments/assets/9843ff20-e8fd-4c16-adc9-9ddcffade007)|

|Text Analysis|Results|
|---------------------|---------------------|
|![sc1](https://github.com/user-attachments/assets/5fb4c311-f0d7-461a-914a-3d4bec1ee3b4)|![sc8](https://github.com/user-attachments/assets/fc30642b-18de-4a31-b388-feb455208caa)|

# CLI tool
![ter](https://github.com/user-attachments/assets/a73fa89f-ea80-4510-b4ac-1e7f94ad35f2)
**Running Command line application**
```bash
cd backend
```
```bash
python3 Test.py
```
For local folder search input the path as "Test".

# Risk Score Calculation
|||
|---------------------|---------------------|
|![WhatsApp Image 2024-09-14 at 16 44 18](https://github.com/user-attachments/assets/3ec975eb-deb1-49d3-bc01-5455f2e31e2f)|![WhatsApp Image 2024-09-14 at 16 43 57](https://github.com/user-attachments/assets/c2e6a4ae-ef66-4ba2-a7b0-dbaacf0f1b53)|









