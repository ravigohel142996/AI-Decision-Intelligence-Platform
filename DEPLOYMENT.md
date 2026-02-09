# 🚀 Deployment Guide - DecisionPilot AI

## Deployment Options

### Option 1: Streamlit Cloud (Recommended)

**Perfect for:** Quick deployment, team access, no infrastructure management

#### Steps:

1. **Push to GitHub**
   ```bash
   git add .
   git commit -m "Deploy DecisionPilot AI"
   git push origin main
   ```

2. **Deploy on Streamlit Cloud**
   - Go to [share.streamlit.io](https://share.streamlit.io)
   - Sign in with GitHub
   - Click "New app"
   - Select your repository
   - Main file path: `app.py`
   - Click "Deploy"

3. **Configure (Optional)**
   - App URL: Custom subdomain
   - Python version: 3.9+
   - Secrets: Add API keys if needed

4. **Access Your App**
   - URL: `https://[your-app-name].streamlit.app`
   - Share with team members

**Pros:**
- ✅ Free tier available
- ✅ Automatic HTTPS
- ✅ Easy updates (git push)
- ✅ No server management

**Cons:**
- ❌ Resource limits on free tier
- ❌ Public by default
- ❌ Cold start delays

---

### Option 2: Docker Container

**Perfect for:** Production deployment, scalability, custom infrastructure

#### Dockerfile

Create a `Dockerfile`:

```dockerfile
FROM python:3.9-slim

# Set working directory
WORKDIR /app

# Install system dependencies
RUN apt-get update && apt-get install -y \
    build-essential \
    curl \
    software-properties-common \
    && rm -rf /var/lib/apt/lists/*

# Copy requirements
COPY requirements.txt .

# Install Python dependencies
RUN pip install --no-cache-dir -r requirements.txt

# Copy application files
COPY . .

# Expose port
EXPOSE 8501

# Health check
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health || exit 1

# Run the application
CMD ["streamlit", "run", "app.py", "--server.address=0.0.0.0"]
```

#### Build and Run

```bash
# Build image
docker build -t decisionpilot-ai .

# Run container
docker run -p 8501:8501 decisionpilot-ai

# Access at http://localhost:8501
```

#### Docker Compose

Create `docker-compose.yml`:

```yaml
version: '3.8'

services:
  app:
    build: .
    ports:
      - "8501:8501"
    volumes:
      - ./data:/app/data
      - ./models:/app/models
    environment:
      - STREAMLIT_SERVER_HEADLESS=true
      - STREAMLIT_SERVER_PORT=8501
    restart: unless-stopped
```

Run with:
```bash
docker-compose up -d
```

---

### Option 3: AWS Deployment

**Perfect for:** Enterprise deployment, high availability, custom scaling

#### AWS EC2

1. **Launch EC2 Instance**
   - Instance type: t3.medium or larger
   - OS: Ubuntu 22.04 LTS
   - Security group: Allow port 8501

2. **Connect and Setup**
   ```bash
   ssh -i your-key.pem ubuntu@your-instance-ip
   
   # Update system
   sudo apt update && sudo apt upgrade -y
   
   # Install Python
   sudo apt install python3-pip python3-venv -y
   
   # Clone repository
   git clone https://github.com/yourusername/AI-Decision-Intelligence-Platform.git
   cd AI-Decision-Intelligence-Platform
   
   # Create virtual environment
   python3 -m venv venv
   source venv/bin/activate
   
   # Install dependencies
   pip install -r requirements.txt
   
   # Run with nohup
   nohup streamlit run app.py --server.port=8501 --server.address=0.0.0.0 &
   ```

3. **Access**
   - URL: `http://your-instance-ip:8501`

#### AWS ECS (Container Service)

1. Push Docker image to ECR
2. Create ECS Task Definition
3. Create ECS Service
4. Configure Load Balancer
5. Set up Auto Scaling

---

### Option 4: Azure Deployment

**Perfect for:** Microsoft Azure users, integration with Azure services

#### Azure App Service

```bash
# Login to Azure
az login

# Create resource group
az group create --name DecisionPilotRG --location eastus

# Create App Service plan
az appservice plan create \
  --name DecisionPilotPlan \
  --resource-group DecisionPilotRG \
  --sku B1 --is-linux

# Create web app
az webapp create \
  --resource-group DecisionPilotRG \
  --plan DecisionPilotPlan \
  --name decisionpilot-ai \
  --runtime "PYTHON:3.9"

# Deploy from GitHub
az webapp deployment source config \
  --name decisionpilot-ai \
  --resource-group DecisionPilotRG \
  --repo-url https://github.com/yourusername/repo \
  --branch main \
  --manual-integration
```

---

### Option 5: Google Cloud Platform

**Perfect for:** GCP users, serverless deployment

#### Cloud Run

```bash
# Build and push to Container Registry
gcloud builds submit --tag gcr.io/PROJECT_ID/decisionpilot-ai

# Deploy to Cloud Run
gcloud run deploy decisionpilot-ai \
  --image gcr.io/PROJECT_ID/decisionpilot-ai \
  --platform managed \
  --region us-central1 \
  --allow-unauthenticated \
  --port 8501
```

---

### Option 6: Heroku

**Perfect for:** Quick prototyping, simple deployment

#### Setup Files

Create `Procfile`:
```
web: streamlit run app.py --server.port=$PORT --server.address=0.0.0.0
```

Create `setup.sh`:
```bash
mkdir -p ~/.streamlit/
echo "[server]
headless = true
port = $PORT
enableCORS = false
" > ~/.streamlit/config.toml
```

#### Deploy

```bash
# Login to Heroku
heroku login

# Create app
heroku create decisionpilot-ai

# Push code
git push heroku main

# Open app
heroku open
```

---

## Production Considerations

### 1. Security

**Authentication:**
```python
# Add to app.py
import streamlit_authenticator as stauth

authenticator = stauth.Authenticate(
    credentials,
    'decisionpilot',
    'auth_key',
    30
)

name, authentication_status, username = authenticator.login('Login', 'main')

if authentication_status:
    # Show app
    main()
elif authentication_status == False:
    st.error('Username/password is incorrect')
```

**HTTPS:**
- Use reverse proxy (nginx)
- Enable SSL certificates
- Configure in deployment platform

**API Keys:**
```bash
# Use environment variables
export OPENAI_API_KEY="your-key"
export DB_PASSWORD="your-password"
```

### 2. Performance

**Caching:**
```python
@st.cache_data
def load_data():
    return pd.read_csv('data.csv')

@st.cache_resource
def load_model():
    return joblib.load('model.pkl')
```

**Database:**
- Use PostgreSQL instead of SQLite
- Implement connection pooling
- Cache frequently accessed data

**Async Operations:**
```python
import asyncio

async def fetch_data():
    # Async operations
    pass
```

### 3. Monitoring

**Application Metrics:**
```python
import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

logger.info("User action: forecasted revenue")
```

**Health Checks:**
```python
# Add health endpoint
if st.experimental_get_query_params().get('health'):
    st.write("OK")
    st.stop()
```

**Error Tracking:**
- Integrate Sentry
- Set up alerts
- Monitor performance

### 4. Scaling

**Horizontal Scaling:**
- Use load balancer
- Multiple app instances
- Shared data storage

**Vertical Scaling:**
- Increase instance size
- More CPU/RAM
- GPU for ML models

**Caching Layer:**
- Redis for sessions
- Memcached for data
- CDN for static files

---

## Environment Variables

Create `.env` file (don't commit!):

```bash
# Application
APP_ENV=production
DEBUG=false

# Database
DATABASE_URL=postgresql://user:pass@host:5432/db

# API Keys
OPENAI_API_KEY=sk-xxxxx
AWS_ACCESS_KEY=xxxxx
AWS_SECRET_KEY=xxxxx

# Feature Flags
ENABLE_ML=true
ENABLE_SIMULATION=true
```

Load in app:
```python
from dotenv import load_dotenv
import os

load_dotenv()

api_key = os.getenv('OPENAI_API_KEY')
```

---

## Backup and Recovery

### Data Backup

```bash
# Backup data folder
tar -czf backup-$(date +%Y%m%d).tar.gz data/

# Backup to S3
aws s3 cp backup-$(date +%Y%m%d).tar.gz s3://your-bucket/backups/
```

### Model Versioning

```python
# Save with timestamp
import datetime

timestamp = datetime.datetime.now().strftime('%Y%m%d_%H%M%S')
model.save(f'models/model_{timestamp}.h5')
```

---

## CI/CD Pipeline

### GitHub Actions

Create `.github/workflows/deploy.yml`:

```yaml
name: Deploy to Production

on:
  push:
    branches: [ main ]

jobs:
  deploy:
    runs-on: ubuntu-latest
    
    steps:
    - uses: actions/checkout@v2
    
    - name: Set up Python
      uses: actions/setup-python@v2
      with:
        python-version: '3.9'
    
    - name: Install dependencies
      run: |
        pip install -r requirements.txt
    
    - name: Run tests
      run: |
        python -m pytest tests/
    
    - name: Deploy to Streamlit Cloud
      run: |
        # Trigger deployment
        curl -X POST $STREAMLIT_WEBHOOK_URL
```

---

## Cost Optimization

### Cloud Costs

| Platform | Free Tier | Paid Start | Best For |
|----------|-----------|------------|----------|
| Streamlit Cloud | 1 app free | $20/month | Small teams |
| Heroku | Hobby free | $7/month | Prototypes |
| AWS EC2 | 12 months free | $10/month | Full control |
| Google Cloud Run | 2M requests | Pay per use | Variable load |
| Azure App Service | 10 apps free | $13/month | Enterprise |

### Optimization Tips

1. **Use caching** - Reduce compute time
2. **Lazy loading** - Load only when needed
3. **Compression** - Reduce data transfer
4. **Serverless** - Pay only for usage
5. **Spot instances** - Save on compute

---

## Support and Maintenance

### Regular Tasks

- **Daily:** Monitor error logs
- **Weekly:** Check performance metrics
- **Monthly:** Update dependencies
- **Quarterly:** Review security
- **Annually:** Architecture review

### Updates

```bash
# Update dependencies
pip install --upgrade -r requirements.txt

# Test updates
python -m pytest

# Deploy
git push origin main
```

---

## Troubleshooting

### Common Issues

**Port Already in Use:**
```bash
lsof -ti:8501 | xargs kill -9
```

**Memory Issues:**
```python
# Clear cache
st.cache_data.clear()
st.cache_resource.clear()
```

**Slow Loading:**
- Enable caching
- Optimize data queries
- Use pagination

---

**Need Help?** Contact support or check documentation at [README.md](README.md)
