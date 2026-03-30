# 💥 Exam Panic Solver

> Stop studying randomly — plan smart!

A terminal-based study planner that automatically builds a personalized study schedule based on your exam dates, topics, and difficulty levels. No more guessing how much time to spend on each subject.

---

## 🎯 The Problem It Solves

Most students open their books the night before an exam with no plan. This tool takes your exam date, your topics, and how hard each one is — then calculates exactly how many hours to spend on each topic per day, so you never waste time or panic last minute.

---

## ✨ Features

- 📅 **Smart Schedule Generator** — Automatically splits study hours across topics weighted by difficulty
- 🚨 **Panic Meter** — Color-coded urgency alerts (green → yellow → red) based on days left
- ✅ **Progress Tracker** — Mark topics as done and watch your progress bar fill up
- 💾 **Auto Save** — All your data is saved automatically in a local JSON file
- 🎨 **Colored Terminal UI** — Clean, readable interface using ANSI colors (no external libraries)

---

## 📸 Preview

```
╔══════════════════════════════════════════════════╗
║           💥  EXAM PANIC SOLVER  💥              ║
║      Stop studying randomly — plan smart!        ║
╚══════════════════════════════════════════════════╝

  📆 Today: Monday, 2025-06-01

  Your Upcoming Exams:
  • Math                 3 days left  [██████░░░░] 3/5 topics
  • Physics              12 days left [████░░░░░░] 2/5 topics

──────────────────────────────────────────────────
  Menu:
  1. ➕ Add new exam
  2. 📅 View full schedule
  3. ✅ Mark topic as done
  4. 🗑️  Delete exam
  5. 🚪 Exit
──────────────────────────────────────────────────
```

---

## 🚀 Getting Started

### Requirements
- Python 3.x
- No external libraries needed!

### Run the project

```bash
# Clone the repository
git clone https://github.com/your-username/exam-panic-solver.git

# Navigate into the folder
cd exam-panic-solver

# Run the program
python exam_panic_solver.py
```

---

## 🧠 How It Works

1. You add an exam with a subject name, date, and list of topics
2. For each topic, you rate the difficulty: Easy (1), Medium (2), or Hard (3)
3. The program calculates the total available hours until the exam
4. It distributes those hours across topics — harder topics get more time automatically
5. You can mark topics as done and track your overall progress

### Example

If you have **10 days**, studying **3 hours/day**, and 3 topics:

| Topic       | Difficulty | Hours Assigned |
|-------------|------------|----------------|
| Calculus    | 🔴 Hard    | 15.0 hrs       |
| Statistics  | 🟡 Medium  | 10.0 hrs       |
| Algebra     | 🟢 Easy    | 5.0 hrs        |

---

## 📁 Project Structure

```
exam-panic-solver/
│
├── exam_panic_solver.py   # Main program
├── exams_data.json        # Auto-generated data file (created on first run)
└── README.md              # You're reading it!
```

---

## 🛠️ Built With

| Tool | Purpose |
|------|---------|
| Python 3 | Core language |
| `json` | Saving and loading exam data |
| `datetime` | Calculating days left until exam |
| `os` | Clearing the terminal screen |
| ANSI Escape Codes | Colored terminal output |

---

## 🌱 Possible Future Improvements

- [ ] Export schedule to a `.txt` or `.pdf` file
- [ ] Add a Pomodoro timer for study sessions
- [ ] Set daily reminders using system notifications
- [ ] GUI version using `tkinter`

---

## 👨‍💻 Author

**Beshoy**
- GitHub: [@your-username](https://github.com/your-username)

---

## 📄 License

This project is open source and available under the [MIT License](LICENSE).
