# 🤖 DeepSeek R1 Neural Interface - Cyberpunk RAG Chatbot

A futuristic cyberpunk-themed Retrieval-Augmented Generation (RAG) chatbot powered by DeepSeek R1 via OpenRouter. Features a stunning neon-lit interface with cool animations and effects.

![Cyberpunk Theme](https://img.shields.io/badge/Theme-Cyberpunk-ff0080?style=for-the-badge)
![Python](https://img.shields.io/badge/Python-3.12+-00ff41?style=for-the-badge&logo=python)
![Flask](https://img.shields.io/badge/Flask-3.0.3-00ffff?style=for-the-badge&logo=flask)
![LangChain](https://img.shields.io/badge/LangChain-0.2.3-8000ff?style=for-the-badge)

## ✨ Features

### 🎨 Cyberpunk UI/UX
- **Neon Color Scheme**: Cyan, Pink, Purple, Green glowing effects
- **Futuristic Typography**: Orbitron and Rajdhani fonts
- **Dynamic Animations**: 
  - Moving grid background
  - Floating particle effects
  - Neon flickering text
  - Glitch effects on errors
  - Typing animations
  - Rotating rainbow borders

### 🧠 AI-Powered Features
- **RAG Architecture**: Retrieval-Augmented Generation for accurate responses
- **Document Processing**: Supports PDF and TXT files
- **Vector Search**: FAISS-powered semantic search
- **Source Citations**: Shows relevant document sources
- **Real-time Chat**: Interactive conversation interface

### 🚀 Technical Stack
- **Backend**: Flask (Python)
- **AI Model**: DeepSeek R1 via OpenRouter API
- **Embeddings**: HuggingFace Sentence Transformers
- **Vector Store**: FAISS
- **Frontend**: Vanilla JavaScript with CSS3 animations
- **Document Processing**: LangChain + PyPDF

## 🛠️ Installation

### Prerequisites
- Python 3.12+
- pip
- Virtual environment (recommended)

### Setup

1. **Clone the repository**
   ```bash
   git clone <your-repo-url>
   cd rag_chat
   ```

2. **Create and activate virtual environment**
   ```bash
   python -m venv .venv
   source .venv/bin/activate  # On Windows: .venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   Create a `.env` file in the root directory:
   ```env
   OPENROUTER_API_KEY=your_openrouter_api_key_here
   DEEPSEEK_MODEL_ID=deepseek/deepseek-r1-distill-llama-70b
   ```

5. **Add your documents**
   Place your PDF or TXT files in the `documents/` folder.

6. **Run the application**
   ```bash
   python app.py
   ```

7. **Access the interface**
   Open your browser and navigate to `http://127.0.0.1:5000`

## 📁 Project Structure

```
rag_chat/
├── app.py                 # Flask application entry point
├── rag_chain.py          # RAG chain setup and configuration
├── vector_store.py       # FAISS vector store management
├── document_processor.py # Document loading and chunking
├── requirements.txt      # Python dependencies
├── .env                  # Environment variables (create this)
├── .gitignore           # Git ignore rules
├── documents/           # Place your documents here
│   └── sample.txt       # Sample document
├── faiss_store/         # Vector store (auto-generated)
├── static/
│   └── styles.css       # Cyberpunk CSS styles
└── templates/
    └── index.html       # Main interface template
```

## 🎮 Usage

1. **Start the application** using `python app.py`
2. **Open your browser** to `http://127.0.0.1:5000`
3. **Type your question** in the neural interface
4. **Click EXECUTE** or press Enter
5. **Watch the cyberpunk magic** as the AI responds with typing effects
6. **View sources** from your document database

### Example Queries
- "What is machine learning?"
- "Explain the main concepts in the documents"
- "Summarize the key points about AI"

## 🎨 Cyberpunk Features

### Visual Effects
- **Neon Glow**: Text shadows and border glows
- **Grid Animation**: Moving background grid pattern
- **Particle System**: Floating colored particles
- **Glitch Effects**: Matrix-style text corruption
- **Typing Animation**: Character-by-character text reveal
- **Hover Effects**: Button transformations and light sweeps

### Interactive Elements
- **Loading States**: Spinning neon loader
- **Error Handling**: Glitch effects for errors
- **Auto-scroll**: Smooth scrolling to new messages
- **Responsive Design**: Mobile-friendly layout
- **System Messages**: Random status updates

## 🔧 Configuration

### Environment Variables
- `OPENROUTER_API_KEY`: Your OpenRouter API key
- `DEEPSEEK_MODEL_ID`: DeepSeek model identifier

### Model Options
You can use different models by changing the `DEEPSEEK_MODEL_ID`:
- `deepseek/deepseek-r1-distill-llama-70b` (recommended)
- `deepseek/deepseek-chat`
- Other OpenRouter-supported models

### Customization
- **Colors**: Modify CSS variables in `styles.css`
- **Animations**: Adjust keyframe animations
- **Chunk Size**: Change in `document_processor.py`
- **Retrieval Count**: Modify `search_kwargs` in `rag_chain.py`

## 🐛 Troubleshooting

### Common Issues

1. **FAISS Build Error**
   ```bash
   # Install system dependencies
   sudo apt-get install build-essential python3-dev libblas-dev liblapack-dev gfortran
   ```

2. **API Key Issues**
   - Ensure your OpenRouter API key is valid
   - Check the `.env` file is in the root directory
   - Verify the model ID is correct

3. **Document Loading Problems**
   - Ensure documents are in the `documents/` folder
   - Check file permissions
   - Verify file formats (PDF/TXT only)

4. **Vector Store Issues**
   - Delete `faiss_store/` folder and restart
   - This will regenerate the vector store

## 🤝 Contributing

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

## 📝 License

This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## 🙏 Acknowledgments

- **DeepSeek**: For the amazing AI model
- **OpenRouter**: For API access
- **LangChain**: For RAG framework
- **FAISS**: For vector similarity search
- **HuggingFace**: For embeddings
- **Cyberpunk 2077**: For visual inspiration

## 📊 Dependencies

Key dependencies and their purposes:

| Package | Version | Purpose |
|---------|---------|---------|
| Flask | 3.0.3 | Web framework |
| LangChain | 0.2.3 | RAG framework |
| FAISS | 1.11.0 | Vector similarity search |
| Sentence Transformers | 2.7.0 | Text embeddings |
| PyPDF | 4.2.0 | PDF processing |
| OpenAI | 1.95.1 | API client |

## 🚀 Future Enhancements

- [ ] Voice input/output
- [ ] Multi-language support
- [ ] Advanced document types (DOCX, HTML)
- [ ] Chat history persistence
- [ ] User authentication
- [ ] API endpoints for integration
- [ ] Docker containerization
- [ ] Advanced cyberpunk effects

---

**Built with 💜 by QuarrelsomeDevil17**

*"The future is here, and it's neon-lit."*
