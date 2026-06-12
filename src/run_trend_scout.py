import subprocess

print("AURA Trend Scout Starting...\n")

subprocess.run(["python", "google_trends_collector.py"])

subprocess.run(["python", "trend_detector.py"])

subprocess.run(["python", "trend_analyst.py"])

subprocess.run(["python", "save_to_supabase.py"])

print("\nAURA Trend Scout Complete!")git commit -m "Cleanup gitignore and generated files"
