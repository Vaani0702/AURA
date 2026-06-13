import subprocess

print("AURA Trend Scout Starting...\n")

subprocess.run(["python", "src/google_trends_collector.py"])

subprocess.run(["python", "src/trend_detector.py"])

subprocess.run(["python", "src/trend_analyst.py"])

subprocess.run(["python", "src/save_to_supabase.py"])
subprocess.run(["python", "src/trend_memory.py"])
subprocess.run(["python", "src/trend_acceleration.py"])
print("\nAURA Trend Scout Complete!")
