# Digital-Clock

⏰ Python Beep Clock


A simple Python script that displays the current date and time in real-time and plays a beep sound every 5 seconds.

📌 Features


* Continuously prints the current date and time.

* Plays a beep sound every 5 seconds.

* Uses Python’s built-in libraries (datetime, time, and winsound).

* Lightweight and easy to run on Windows.

🛠 Requirements


* Python 3.x

* Windows OS (since winsound works only on Windows)

🎵 How It Works


* The script checks the current second from the system clock.

* If the second is divisible by 5, a beep sound is played.

* The console keeps showing the current date and time every second.

📂 Example Output

* Current Date and Time: 23-08-2025 16:45:01
* Current Date and Time: 23-08-2025 16:45:02
* Current Date and Time: 23-08-2025 16:45:03
* Current Date and Time: 23-08-2025 16:45:04
* Current Date and Time: 23-08-2025 16:45:05 [(Beep sound plays here)]

⚠️ Notes


* Works only on Windows because of the winsound module.

* If you want cross-platform support, you can replace winsound.Beep with libraries like playsound or pygame.
