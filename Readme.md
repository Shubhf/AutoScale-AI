
# AutoScaleAI 🚀
*A Lightweight Inference Server with Resource-Aware Scheduling*

AutoScaleAI is a modular Python-based microservice that performs real-time machine learning inference while monitoring system performance. It simulates intelligent auto-scaling behavior by tracking latency, CPU usage, and memory consumption per request — mimicking how infrastructure-aware systems like Nutanix dynamically adapt to workload pressure.

---

## 💡 Project Highlights

- ✅ **FastAPI-based RESTful server** for ML inference
- ✅ **Pre-trained RandomForest model** on the digits dataset
- ✅ **System monitoring** using `psutil` to track CPU and memory usage
- ✅ **Latency analysis** for every prediction
- ✅ **Auto-scaling logic** simulated via conditional triggers in `autoscaler.py`
- ✅ **Modular architecture** with clear separation of concerns

---

## 🛠️ Tech Stack

- **Backend**: Python 3.11, FastAPI, Uvicorn
- **ML Model**: scikit-learn `RandomForestClassifier`
- **Monitoring**: `psutil` (CPU + Memory)
- **Packaging**: `joblib`
- **Serving**: REST API via Uvicorn

---

## 📦 Folder Structure

```
AutoScaleAI/
├── app/
│   ├── main.py            # FastAPI API endpoints
│   ├── model.py           # Model loading and prediction
│   ├── autoscaler.py      # Latency-based scaling logic
│   ├── utils.py           # Helper functions (monitoring, formatting)
│   └── train_model.py     # One-time model training script
├── requirements.txt
└── README.md
```

---

## 🚀 Getting Started

### 1. Clone the repository
```bash
git clone https://github.com/shubh-garg/AutoScaleAI.git
cd AutoScaleAI
```

### 2. Install dependencies
```bash
pip install -r requirements.txt
```

### 3. Train the model
```bash
python app/train_model.py
```

### 4. Run the FastAPI server
```bash
uvicorn app.main:app --reload
```

Visit [http://127.0.0.1:8000/docs](http://127.0.0.1:8000/docs) for the Swagger UI.

---

## 🧪 Example API Call

**Endpoint**:
```
POST /predict/
```

**Sample Payload**:
```json
{
  "features": [0.0, 0.0, 10.0, 5.0, 8.0, 3.0, ..., 0.0]
}
```

**Sample Response**:
```json
{
  "prediction": 4,
  "latency": 0.0075,
  "cpu": 13.6,
  "memory": 83.6
}
```

---

## 💼 Resume Bullet Points

- Developed a modular FastAPI microservice for AI inference that dynamically reports latency and system usage to simulate resource-aware scheduling.
- Integrated lightweight model serving (`RandomForestClassifier`) with live system telemetry via `psutil`, achieving <10ms latency on local CPU with scaling logic triggers.

---

## 🌟 Possible Extensions

- Add async queueing / worker threads
- Deploy with Docker and Gunicorn
- Integrate GPU usage metrics (if available)
- Replace RF with ONNX or quantized Transformer model
- Live dashboard with Plotly or Grafana

---

## 📄 License

MIT © 2025 Shubh Garg
