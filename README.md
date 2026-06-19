Multi Modal Fake News Detector

I made A full stack web application that analyzes news articles using multiple verification methods to provide accurate credibility scores.

The Features are:

It Analizes text via Google Fact Check API
Does domain Analysis by WHOIS lookup, reputation checks, satirical detection
Cross checks the news headline and verfies fr different media outlets (SerpAPI)
The feature that took more effors is the image analysis by EXIF metadata extraction and reverse image search
At the end it gives Credibility Score from 0 to 100 showing the reliability of the news


## Start

### Local Development

```bash
# Clone repository
git clone https://github.com/YOUR_USERNAME/fake-news-detector.git
cd fake-news-detector

# Create environment file
cp .env.example .env

# Start application
docker compose up -d --build

# Access application
# Frontend: http://localhost:3000
# Backend API: http://localhost:8000/docs
```

### Stop Application
```bash
docker compose down
```

##  Architecture

- Backend: FastAPI (Python 3.11)
- Frontend: Vanilla HTML/CSS/JavaScript
- Server: Nginx (Alpine)
- Containerization: Docker Compose

## API Keys 

### Google Fact Check API
  Free tier: 1000 calls/day
  Setup: https://console.developers.google.com/
  Add to `.env`: `GOOGLE_FACT_CHECK_API_KEY=your_key`

### SerpAPI
Free tier: 100 searches/month
Setup: https://serpapi.com/
Add to `.env`: `SERPAPI_KEY=your_key`

## Analysis Output

Each analysis provides:
- Credibility Score: 0-100%
- Risk Level: Low / Medium / High
- Text Analysis: Fact-check matches
- Domain Analysis: Age, HTTPS status, reputation
- Headline Corroboration: Number of corroborating sources
- Image Analysis: Metadata and reverse search results
- Flags: Detailed findings

## Project Structure

```
fake-news-detector/
├── backend/
│   ├── main.py                  
│   ├── fact_check.py              
│   ├── image_analysis.py          
│   ├── domain_check.py              
│   └── headline_corroboration.py    
├── frontend/
│   ├── public/index.html          
│   └── Dockerfile                 
├── docker-compose.yml             
└── requirements.txt               
```

## Technology Stack

| Component | Tech |
|-----------|------|
| Backend | FastAPI (Python 3.11) |
| Frontend | HTML5, CSS3, Vanilla JS |
| Server | Nginx Alpine |
| Containerization | Docker Compose |
| APIs | Google Fact Check, SerpAPI, WHOIS |



## Contributing

1. Fork repository
2. Create feature branch: `git checkout -b feature/amazing-feature`
3. Commit: `git commit -m 'Add feature'`
4. Push: `git push origin feature/amazing-feature`
5. Open Pull Request


---

**Made with ❤️ by Shanit⚡️**
