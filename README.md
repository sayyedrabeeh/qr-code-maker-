# QR Code Generator

A professional Django-based QR code generator with a modern, attractive UI. Generate high-quality QR codes instantly for URLs, websites, and text content.

![QR Code Generator](https://img.shields.io/badge/Django-5.0-green.svg)
![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)

## Features

-  **Instant Generation** - Create QR codes in seconds
-  **Modern UI** - Professional, responsive design
-  **Mobile Friendly** - Works seamlessly on all devices
-  **Download Options** - Save QR codes as PNG images
-  **Secure** - No data storage, privacy-focused
-  **Free to Use** - Open source and completely free

[!qrcodepage ](a.png)

## Tech Stack

- **Backend**: Django 5.0+
- **Frontend**: HTML5, CSS3, JavaScript
- **QR Generation**: qrcode library
- **Server**: Gunicorn (production)

## Installation

### Prerequisites

- Python 3.8 or higher
- pip (Python package manager)
- Git

### Local Setup

1. **Clone the repository**
   ```bash
   git clone https://github.com/sayyedrabeeh/qr-code-maker-.git
   cd qr-code-maker-
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   
   # On Windows
   venv\Scripts\activate
   
   # On macOS/Linux
   source venv/bin/activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Run migrations**
   ```bash
   python manage.py migrate
   ```

5. **Run the development server**
   ```bash
   python manage.py runserver
   ```

6. **Access the application**
   
   Open your browser and navigate to `http://127.0.0.1:8000`

## Project Structure

```
qr-code-maker/
├── qrcode_app/          # Main Django app
│   ├── views.py         # View logic
│   ├── urls.py          # URL routing
│   └── templates/       # HTML templates
├── static/              # Static files (CSS, JS, images)
├── media/               # Generated QR codes (temporary)
├── manage.py            # Django management script
├── requirements.txt     # Python dependencies
└── README.md           # Project documentation
```

## Usage

1. Enter a URL or text content in the input field
2. Click "Generate QR Code"
3. View your generated QR code
4. Download the QR code as a PNG image
5. Generate new QR codes as needed

## Dependencies

```txt
Django>=5.0,<6.0
qrcode[pil]>=7.4
Pillow>=10.0
gunicorn>=21.0  # For production deployment
whitenoise>=6.0  # For static files in production
```

 

 
## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Author

**Sayyed Rabeeh**

- GitHub: [@sayyedrabeeh](https://github.com/sayyedrabeeh)

## Acknowledgments

- Django community for excellent documentation
- QR code library contributors
- UI/UX inspiration from modern web applications

## Support

If you find this project helpful, please give it a ⭐ on GitHub!

For issues and questions, please open an issue on the [GitHub repository](https://github.com/sayyedrabeeh/qr-code-maker-/issues).

---

**Made with Sayyed using Django**