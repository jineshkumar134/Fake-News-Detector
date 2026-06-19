# 🔍 Multi-Modal Fake News Detector
Multi Modal Fake News Detector

A full-stack web application that analyzes news articles using multiple verification methods to provide accurate credibility scores.
I made A full stack web application that analyzes news articles using multiple verification methods to provide accurate credibility scores.

## ✨ Features
The Features are:

- **Text Analysis** - Fact-checking via Google Fact Check API
- **Domain Analysis** - WHOIS lookup, reputation checks, satirical detection
- **Headline Corroboration** - News source cross-verification (SerpAPI)
- **Image Analysis** - EXIF metadata extraction, reverse image search
- **Credibility Score** - 0-100% with risk levels (Low/Medium/High)
It Analizes text via Google Fact Check API
Does domain Analysis by WHOIS lookup, reputation checks, satirical detection
Cross checks the news headline and verfies fr different media outlets (SerpAPI)
The feature that took more effors is the image analysis by EXIF metadata extraction and reverse image search
At the end it gives Credibility Score from 0 to 100 showing the reliability of the news

## 🚀 Quick Start

## Start

### Local Development

@@ -35,56 +36,54 @@ docker compose up -d --build
docker compose down
```

## 🏗️ Architecture
##  Architecture

- **Backend**: FastAPI (Python 3.11)
- **Frontend**: Vanilla HTML/CSS/JavaScript
- **Server**: Nginx (Alpine)
- **Containerization**: Docker Compose
- Backend: FastAPI (Python 3.11)
- Frontend: Vanilla HTML/CSS/JavaScript
- Server: Nginx (Alpine)
- Containerization: Docker Compose

## 🔑 API Keys (Optional)
## API Keys 

### Google Fact Check API
- Free tier: 1000 calls/day
- Setup: https://console.developers.google.com/
- Add to `.env`: `GOOGLE_FACT_CHECK_API_KEY=your_key`
  Free tier: 1000 calls/day
  Setup: https://console.developers.google.com/
  Add to `.env`: `GOOGLE_FACT_CHECK_API_KEY=your_key`

### SerpAPI
- Free tier: 100 searches/month
- Setup: https://serpapi.com/
- Add to `.env`: `SERPAPI_KEY=your_key`

**Note:** App works without API keys using mock data for demo mode.
Free tier: 100 searches/month
Setup: https://serpapi.com/
Add to `.env`: `SERPAPI_KEY=your_key`

## 📊 Analysis Output
## Analysis Output

Each analysis provides:
- **Credibility Score**: 0-100%
- **Risk Level**: Low (✅) / Medium (⚠️) / High (🚨)
- **Text Analysis**: Fact-check matches
- **Domain Analysis**: Age, HTTPS status, reputation
- **Headline Corroboration**: Number of corroborating sources
- **Image Analysis**: Metadata and reverse search results
- **Flags**: Detailed findings
- Credibility Score: 0-100%
- Risk Level: Low / Medium / High
- Text Analysis: Fact-check matches
- Domain Analysis: Age, HTTPS status, reputation
- Headline Corroboration: Number of corroborating sources
- Image Analysis: Metadata and reverse search results
- Flags: Detailed findings

## 📁 Project Structure
## Project Structure

```
fake-news-detector/
├── backend/
│   ├── main.py                    # FastAPI app
│   ├── fact_check.py              # Fact-checking
│   ├── image_analysis.py          # Image verification
│   ├── domain_check.py            # Domain reputation
│   └── headline_corroboration.py  # News corroboration
│   ├── main.py                  
│   ├── fact_check.py              
│   ├── image_analysis.py          
│   ├── domain_check.py              
│   └── headline_corroboration.py    
├── frontend/
│   ├── public/index.html          # Web interface
│   └── Dockerfile                 # Nginx container
├── docker-compose.yml             # Orchestration
└── requirements.txt               # Dependencies
│   ├── public/index.html          
│   └── Dockerfile                 
├── docker-compose.yml             
└── requirements.txt               
```

## 🛠️ Technology Stack
## Technology Stack

| Component | Tech |
|-----------|------|
@@ -94,63 +93,17 @@ fake-news-detector/
| Containerization | Docker Compose |
| APIs | Google Fact Check, SerpAPI, WHOIS |

## 🚢 Deployment

### Railway (Recommended)
1. Go to https://railway.app/
2. Create new project
3. Connect GitHub repository
4. Auto-deploy on push

### Render
1. Go to https://render.com/
2. Create Web Service
3. Connect GitHub
4. Select Docker build

### DigitalOcean
1. Go to https://cloud.digitalocean.com/apps
2. Create new App
3. Connect GitHub
4. Deploy

## 🐛 Troubleshooting

### Port Already in Use
```bash
lsof -i :3000
kill -9 <PID>
```

### Containers Won't Start
```bash
docker compose logs -f
docker compose build --no-cache
docker compose up -d
```

### API Keys Not Working
- Verify `.env` file exists
- Restart containers: `docker compose restart backend`
- Check logs: `docker logs fake-news-backend`

## 📄 License

MIT License - See LICENSE file

## 🤝 Contributing
## Contributing

1. Fork repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Commit: `git commit -m 'Add feature'`
4. Push: `git push origin feature/amazing-feature`
5. Open Pull Request

## 📞 Support

- **Issues**: GitHub Issues
- **API Docs**: http://localhost:8000/docs (when running locally)

---

**Made with ❤️ by Your Name**
**Made with ❤️ by Shanit⚡️**
