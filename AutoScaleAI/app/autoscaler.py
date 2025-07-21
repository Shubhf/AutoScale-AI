# app/autoscaler.py

def scale_resources(latency, system_stats):
    cpu, mem = system_stats
    print(f"[Monitor] Latency: {latency:.3f}s | CPU: {cpu}% | MEM: {mem}%")

    if latency > 0.5 or cpu > 80:
        print("[Scaler] ⚠️ High load! Consider adding threads or throttling requests.")
    else:
        print("[Scaler] ✅ System stable.")
