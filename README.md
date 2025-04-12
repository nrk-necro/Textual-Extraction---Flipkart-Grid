# 🧾 Integrated Receipt reading system using OCR and NLP techniques

An integrated pipeline for **OCR + Information Extraction** using a combination of traditional computer vision (OpenCV), neural OCR (EasyOCR), SuryaOCR and large language models (NuMind’s NuExtract + fine-tuned Gemma). Designed for robust parsing of **printed receipts** and structured data extraction.

---

## Overview

This project aims to:

- **Detect and preprocess receipt images** for optimal OCR
- **Extract high-confidence text regions** using EasyOCR
- **Analyze shapes and directions** using contours and polygon angle heuristics
- **Parse structured fields** like total amount, item list, date, or customer info using fine-tuned LLMs
- Build a modular architecture to scale with real-world OCR + NLU applications

---

## Tech Stack

| Component | Technology |
|----------|-------------|
| OCR Engine | EasyOCR |
| Image Preprocessing | OpenCV |
| Entity Extraction | NuMind NuExtract-tiny, Fine-tuned Gemma |
| ML Framework | PyTorch, HuggingFace Transformers |
| Visualization | OpenCV, Matplotlib |

---

## Project Structure

```bash
.
├── ocr_opencv.py         # OpenCV-based image preprocessing (blur, threshold, etc.)
├── ocr_trial.py          # EasyOCR reader with high-confidence filtering and overlay
├── cv2_filter.py         # Contour detection and filtering via adaptive thresholding
├── cv2_contour.py        # Shape recognition for arrows and direction inference
├── nuextract.py          # Prompt-based LLM extractor using NuMind NuExtract
├── requirements.txt      # Dependencies
└── README.md             # You're here!
```
### 1. Preprocess Image (Optional)

```bash
python cv2_filter.py
python cv2_contour_filter.py
python ocr_opencv.py

```

### 2. OCR
#### 1. Surya OCR
-Most accurate among the models tested. Has multilingual support.
```bash
jupyterlab OCR_Surya.ipynb
```
### 2. EasyOCR
-Performs OCR using EasyOCR.
-Filters recognized text with confidence > 90%.
-Annotates detected text directly on the image

```bash
python ocr_trial.py
```

#### 3. GOT

```bash
python transformer_model_GOT.py
```

### 3. Entity Recognision
#### 1. Using Nuextract Small LM

```bash
python text_detail_extraction.ipynb
```
#### 2. Using fine-tuned Gemma 2B

```bash
python text_extraction_Gemma.ipynb
```
