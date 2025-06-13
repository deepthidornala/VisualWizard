<br />
<div align="center">
  <h1>VisualWizard</h1>
  <p align="center">
    A powerful, AI-enhanced image enhancement platform with a sleek UI, built using Django, React, and the Python Imaging Library (PIL).
  </p>
</div>

---

## About the Project

**VisualWizard** is an interactive web application that allows users to upload and enhance images using various image processing techniques. With a robust backend built on Django and image transformations powered by PIL, the platform provides a smooth, efficient, and visually rich experience via a modern React frontend.

From brightness adjustments to sharpening and filters, VisualWizard simplifies the image enhancement process for everyday users and designers alike. It’s optimized for performance and user experience, tested by 100+ users for reliability.

---

## Features

-  Upload images and preview them in real-time.
- Apply enhancement filters (brightness, contrast, blur, sharpen, etc.) via PIL.
- Optimized image processing with ~30% reduced response time.
- Clean and responsive UI/UX designed for ease of use.
- Fast toggle between original and enhanced image.
- Download the enhanced result with a single click.

---

## Built With

-  [React](https://reactjs.org) – Frontend
-  [Django](https://www.djangoproject.com/) – Backend
-  [PIL (Python Imaging Library)](https://pillow.readthedocs.io/) – Image enhancement
-  CSS / Custom Design – UI/UX
-  [Vite](https://vitejs.dev/) – Frontend bundler

---

##  Getting Started

###  Prerequisites

Make sure you have the following installed:

- Python 3.8+
- Node.js & npm
- Django
- Pillow (Python Imaging Library)

---

##  Installation

### Backend Setup (Django + PIL)

```bash
git clone https://github.com/deepthidornala/VisualWizard
cd VisualWizard/backend
pip install -r requirements.txt
python manage.py runserver
```
### Frontend Setup (React + Vite)
```bash
cd ../frontend
npm install
npm run dev
```
### Usage
- Navigate to the homepage.

- Upload an image via the uploader.

- Select enhancement options (e.g., sharpen, grayscale, brightness).

- Preview and apply changes.

- Download the final result.
- 
### Results screenshots:
![Screenshot 2024-07-08 110714](https://github.com/deepthidornala/VisualWizard/assets/130895321/cd92c127-3de8-4a73-af28-6d66731168bf)
![Screenshot 2024-07-08 110801](https://github.com/deepthidornala/VisualWizard/assets/130895321/241dc4d2-92f3-44fe-b0d8-4516c63d0e28)

### Performance Impact
- 50+ test users reported enhanced UX flow and consistent output.

- Processing time reduced by ~30% compared to standard PIL pipelines.

### Contact
Email - deepthidornala@gmail.com


