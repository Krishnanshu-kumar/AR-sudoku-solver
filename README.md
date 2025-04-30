# 🧩 Sudoku Solver & AR Recorder
**Author:** Krishnanshu Kumar (2206031@kiit.ac.in)  

---

## 🚀 Project Overview

A fun, interactive Sudoku experience that blends classic puzzle solving with cutting-edge computer vision and augmented reality. Extract a Sudoku grid from camera input or image files, solve it instantly using the high-performance Exact Cover method, and overlay the solution back onto your live video feed!

---

## ✨ Key Features

- **Real-Time Grid Extraction**  
  Detect and digitize the Sudoku board from a live camera stream or imported image with OpenCV and ML models.
- **Exact Cover Solver**  
  Lightning-fast, deterministic solving using Donald Knuth’s Algorithm X for guaranteed correctness—no backtracking guesswork needed.
- **Augmented Reality Overlay**  
  Watch the solved numbers appear directly on your physical puzzle in real time, powered by AR techniques.
- **Manual Play & Validation**  
  Enter puzzles yourself, play by hand, then have the app check and verify your solution.
- **Image & Camera Inputs**  
  Import puzzles from photos, screenshots, or live camera—digitize and solve anywhere, anytime.

---

## 📦 Tech Stack

- **Language:** Python 3.x  
- **CV & AR:** OpenCV, MediaPipe, ARToolkit  
- **Solver:** Exact Cover / Algorithm X  
- **GUI:** Tkinter (or PyQt)  
- **Machine Learning:** TensorFlow / PyTorch for digit recognition  
- **Extras:** NumPy, imutils

---

## 🔧 Installation

1. **Clone the repo**  
   ```bash
   git clone https://github.com/your-username/sudoku-ar-solver.git
   cd sudoku-ar-solver
   ```
2. **Create & activate a virtual environment**  
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # On Windows, use `venv\Scripts\activate`
   ```
3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```
4. **Run the application**  
   ```bash
   python main.py
   ```

---

## 🎮 Usage

1. **Launch** the app with `python main.py`.  
2. **Choose Input**:  
   - **Camera Mode** – Point your webcam at any printed, screen, or handwritten Sudoku.  
   - **Image Mode** – Load a puzzle from file (JPEG, PNG).  
3. **Play or Solve**:  
   - **Manual Solve** – Enter digits directly in the GUI, then click **Validate**.  
   - **Auto‐Solve** – Click **Solve**, and watch the AR overlay display the completed grid in real time.

---

## 🔍 Implementation Highlights

- **Exact Cover Matrix Construction**  
  Transforms the 9×9 Sudoku constraints into a binary matrix for Algorithm X.  
- **Optimized Dancing Links**  
  Custom data structures for ultra-fast backtracking elimination.  
- **AR Rendering**  
  Computes homography to align solved digits back onto the original camera frame.

---

## 🌟 Future Scope

- **Rubik’s Cube Solver** via computer vision & AI  
- **Additional Puzzles**: crosswords, jigsaws, logic teasers  
- **Mobile & Web Apps** for on-the-go solving  
- **Community Contributions**: open up new algorithms & puzzle types

---

## 🤝 Contributing

1. Fork the repo  
2. Create a feature branch (`git checkout -b feature/YourIdea`)  
3. Commit your changes (`git commit -m "Add feature"`)  
4. Push to `origin` (`git push`)  
5. Open a Pull Request  

---


*Happy puzzling & coding!* 🎉
