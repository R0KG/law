# LegalDoc AI Assistant

A powerful AI-powered tool for analyzing legal documents using OCR and state-of-the-art NLP models. This application can extract text from legal document images, provide summaries, and answer specific questions about the content.

## Features

- 📷 **OCR Text Extraction**: Convert images of legal documents into machine-readable text
- 📝 **Document Summarization**: Generate concise summaries of legal documents using advanced LLMs
- ❓ **Question Answering**: Get specific answers to questions about the document content
- 🚀 **Optimized Performance**: Optional model quantization for improved efficiency
- 🔍 **Text Processing**: Clean and process extracted text for better accuracy

## Prerequisites

- Python 3.8 or higher
- Tesseract OCR installed on your system
  - Windows: Download and install from [GitHub Tesseract Release](https://github.com/UB-Mannheim/tesseract/wiki)
  - Linux: `sudo apt-get install tesseract-ocr`
  - macOS: `brew install tesseract`

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/legaldoc-ai-assistant.git
cd legaldoc-ai-assistant
```

2. Create and activate a virtual environment:
```bash
python -m venv venv
# Windows
.\venv\Scripts\activate
# Linux/macOS
source venv/bin/activate
```

3. Install required packages:
```bash
pip install -r requirements.txt
```

## Usage

1. Place your legal document image in the `input` directory
2. Run the main script:
```bash
python main.py --input path/to/your/document.png
```

3. For interactive question answering:
```bash
python qa_interface.py --document path/to/your/document.png
```

## Project Structure

```
legaldoc-ai-assistant/
├── input/                  # Input directory for document images
├── output/                 # Output directory for processed results
├── src/
│   ├── ocr.py            # OCR processing module
│   ├── nlp.py            # NLP operations (summarization, QA)
│   ├── utils.py          # Utility functions
│   └── main.py           # Main application script
├── requirements.txt       # Project dependencies
└── README.md             # Project documentation
```

## Models Used

- **OCR**: Tesseract OCR
- **Summarization**: BART/DistilBART
- **Question Answering**: RoBERTa-based model

## Performance Optimization

The project includes optional model quantization for improved performance:

1. Standard models for high accuracy
2. Quantized models for faster inference
3. Cloud deployment options for scalability

## Contributing

1. Fork the repository
2. Create your feature branch (`git checkout -b feature/AmazingFeature`)
3. Commit your changes (`git commit -m 'Add some AmazingFeature'`)
4. Push to the branch (`git push origin feature/AmazingFeature`)
5. Open a Pull Request

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Hugging Face Transformers library
- Tesseract OCR
- PyTorch community
- Legal Tech community

## Future Improvements

- [ ] Web interface implementation
- [ ] Support for multiple document formats
- [ ] Enhanced document preprocessing
- [ ] API endpoint creation
- [ ] Batch processing capability
- [ ] Custom model fine-tuning options

## Contact

Your Name - [@yourtwitter](https://twitter.com/yourtwitter)
Project Link: [https://github.com/yourusername/legaldoc-ai-assistant](https://github.com/yourusername/legaldoc-ai-assistant) 