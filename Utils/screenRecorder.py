import subprocess
import os
import time
import signal
import inspect
 
class ScreenRecorder:
    # def __init__(self, test_name, output_dir="recordings"):
    #     os.makedirs(output_dir, exist_ok=True)
    #     timestamp = time.strftime("%H%M%S")
    #     # self.temp_file = os.path.join(output_dir, f"temp_{timestamp}.mp4")
    #     self.final_file = os.path.join(output_dir, f"{test_name}_{timestamp}.mp4")
    #     self.process = None
       
 
    def __init__(self, test_name=None, output_dir="reports/recordings"):
        os.makedirs(output_dir, exist_ok=True)
 
        if test_name is None:
            # Automatically get the name of the calling script
            frame = inspect.stack()[1]
            filename = os.path.basename(frame.filename)
            test_name = os.path.splitext(filename)[0]  # Remove .py
 
        timestamp = time.strftime("%H%M%S")
        self.final_file = os.path.join(output_dir, f"{test_name}_{timestamp}.mp4")
        self.process = None
 
 
    def start(self):
        self.process = subprocess.Popen([
            "ffmpeg",
            "-y",
            "-f", "gdigrab",
            "-framerate", "10",
            "-i", "desktop",
            "-c:v", "libx264",
            "-preset", "ultrafast",
            self.final_file
        ], creationflags=subprocess.CREATE_NEW_PROCESS_GROUP, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
 
    def stop_and_save(self):
        if self.process:
            self.stop()
            try:
                # time.sleep(2)  # Allow FFmpeg to finalize the file
                # os.rename(self.temp_file, self.final_file)
                print(f"🎥 Saved recording: {self.final_file}")
            except Exception as e:
                print(f"❌ Failed to save recording: {e}")
 
    def stop(self):
        try:
            # Gracefully stop FFmpeg
            self.process.send_signal(signal.CTRL_BREAK_EVENT)
            self.process.wait(timeout=5)
        except Exception as e:
            print(f"⚠️ Error terminating FFmpeg: {e}")
           
    # def delete(self):
    #     self.stop()
    #     if os.path.exists(self.temp_file):
    #         os.remove(self.temp_file)
 
    # def stop_and_discard(self):
    #     if self.process:
    #         self._terminate_ffmpeg()
    #         if os.path.exists(self.temp_file):
    #             os.remove(self.temp_file)
    #             print("🗑️ Discarded failed test recording.")
   
    def stop_and_discard(self):
        if self.process:
            try:
                self.process.kill()
                self.process.wait(timeout=3)  # Forcefully kill and wait a bit
            except Exception as e:
                print(f"⚠️ Failed to kill recorder: {e}")
            for _ in range(3):  # Retry delete
                try:
                    if os.path.exists(self.final_file):
                        os.remove(self.final_file)
                        print("🗑️ Discarded failed test recording.")
                    break
                except PermissionError:
                    time.sleep(1)  # Wait for FFmpeg to release file
 
 
 