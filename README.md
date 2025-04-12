# Integrated Receipt reading system using OCR and NLP techniques

An integrated pipeline for **OCR + Information Extraction** using a combination of traditional computer vision (OpenCV), neural OCR (EasyOCR), SuryaOCR and large language models (NuMind’s NuExtract + fine-tuned Gemma). Designed for robust parsing of **printed receipts** and structured data extraction.

---

## Overview

This project aims to:

- **Detect and preprocess receipt images** for optimal OCR
- **Extract high-confidence text regions** using EasyOCR
- **Analyze shapes and directions** using contours and polygon angle heuristics
- **Parse structured fields** like total amount, item list, date, or customer info using fine-tuned LLMs
- Build a modular architecture to scale with real-world OCR + NLP applications

---

## Tech Stack

| Component | Technology |
|----------|-------------|
| Image Preprocessing | OpenCV |
| OCR Engine | EasyOCR, Surya OCR, GOT
| Entity Extraction | NuMind NuExtract-tiny, Fine-tuned Gemma  2B |

---

## Project Structure

```bash
.
├── ocr_opencv.py         # OpenCV-based image preprocessing (blur, threshold, etc.)
├── ocr_trial.py          # EasyOCR reader with high-confidence filtering and overlay
├── cv2_filter.py         # Contour detection and filtering via adaptive thresholding
├── cv2_contour.py        # Shape recognition for arrows and direction inference
├── nuextract.py          # Prompt-based Small LM extractor using NuMind NuExtract
├── text_extraction_Gemma # Prompt-based fine-tuned LLM for targetted test extraction 
├── requirements.txt      # Dependencies
└── README.md             # You're here!
```
### 1. Preprocess Image (Optional)

```bash
python cv2_filter.py
python cv2_contour_filter.py
python ocr_opencv.py

```
Features:
-Adjustable Gaussian blur, thresholding
-Adaptive thresholding for variable lighting
-Contour/arrow visualization for layout debugging

### 2. OCR
#### 1. Surya OCR
-State-of-the-art OCR model with multilingual support
-Best performance for noisy or distorted scans

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
-Used to post-process raw OCR outputs and improve formatting
-Ideal for correcting structure, punctuation, and messy alignments
```bash
python transformer_model_GOT.py
```

### 3. Entity Recognision
#### 1. Using Nuextract Small LM
-Fast and lightweight model for structured entity parsing
-Schema-driven extraction using prompt-based instructions

```bash
python text_detail_extraction.ipynb
```
#### 2. Using fine-tuned Gemma 2B
-Custom fine-tuning on receipt datasets for more accurate field parsing
-Handles nuanced structures, especially item-price tables and noisy input
```bash
python text_extraction_Gemma.ipynb
```

## Credits

This project is built on top of amazing open-source and research contributions:

- [NuMind.ai – NuExtract-tiny](https://numind.ai): Lightweight, schema-driven language model for entity extraction.
- [EasyOCR](https://github.com/JaidedAI/EasyOCR): Open-source OCR library supporting multiple languages.
- [SuryaOCR](https://github.com/rohitguptacs/SuryaOCR): High-accuracy multilingual OCR model based on deep learning.
- [GOT OCR](https://huggingface.co/guillaume-be/GOT-ocr): Generic OCR Transformer for post-processing and layout-aware corrections.
- [Gemma](https://ai.google.dev/gemma): Google's open LLM family; used here in a fine-tuned 2B variant for receipt extraction.

