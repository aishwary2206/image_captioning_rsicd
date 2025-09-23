# 🛰️ Image Captioning on RSICD Dataset

This project explores **image captioning of satellite images** using the **RSICD dataset**.  
We compare **classical machine learning models** (Logistic Regression, Random Forest, SVM, k-NN) with a **neural CNN+LSTM model**.

---

## 📂 Repository Structure

image-captioning-rsicd/
├─ notebooks/
│ ├─ 01_preprocessing_RSICD.ipynb # already run, outputs saved
│ ├─ 02_classical_baselines.ipynb # ML baselines (to be done by group)
│ └─ 03_cnn_lstm_captioner.ipynb # neural model (to be done by group)
├─ data/
│ └─ preprocessed/ # preprocessed dataset (ready to use)
│ ├─ captions_tokens.json
│ ├─ idx_to_word.json
│ ├─ image_features.npy
│ ├─ image_map.json
│ ├─ train.json
│ ├─ val.json
│ └─ test.json
├─ src/
│ └─ dataloading.py # helper to load preprocessed data
├─ requirements.txt
├─ .gitignore
└─ README.md

---

📊 Data

Preprocessed data is already in data/preprocessed/:

image_features.npy – ResNet50 embeddings (N×2048)

captions_tokens.json – tokenized captions

word_to_idx.json / idx_to_word.json – vocabulary

train.json / val.json / test.json – dataset splits

Raw images (RSICD_images/) are not included due to size. 
Download here - https://drive.google.com/drive/folders/1M5rr-I0tLB9vDGrSr3Z3SUm6HJNajtoQ?usp=sharing


---

📓 Notebooks

01_preprocessing_RSICD.ipynb → Prepares vocab, tokenized captions, and CNN features.

---

👥 Team Workflow

Each teammate works on a separate notebook or branch:

feat/logreg-svm

feat/random-forest

feat/cnn-lstm

Open Pull Requests to merge into main.

---


## ⚙️ Setup Instructions

1. Clone the repo:
   ```bash
   git clone https://github.com/<your-username>/image-captioning-rsicd.git
   cd image-captioning-rsicd

2. Create a virtual environment & install dependencies:

python -m venv .venv
source .venv/bin/activate     # Windows: .venv\Scripts\activate
pip install -r requirements.txt

