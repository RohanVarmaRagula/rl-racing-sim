# 🏎️ RL Racing Sim

Lightweight racing environment to train autonomous cars using reinforcement learning.  
Built solely with **Python + Pygame + RL algorithms (DQN, PPO, Actor-Critic, etc.)**

---

## 🚀 Getting Started

### 1️⃣ Create a virtual environment
```
python -m venv myvenv
```

### 2️⃣ Activate the virtual environment
```
myvenv/Scripts/activate   # Windows
source myvenv/bin/activate  # Linux/Mac
```

### 3️⃣ Install dependencies
```
pip install -r requirements.txt
```

### 4️⃣ Run the environment
```
python src/env/racing_env.py
```

---

## 📋 Project Roadmap
Legend - ⬜ To-do
🟨 Partial
✅ Done
| Phase                            | Goal                                             | Tasks                                                                                                                                                                                                                      |
| -------------------------------- | ------------------------------------------------ | -------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Implement Game & Physics**     | Build the base game and environment              | ✅ Collect transparent car images <br> ✅ Make basic tracks <br> 🟨 Implement `Car` class (`src/env/car.py`) <br> 🟨 Implement `Track` class (`src/env/track.py`) <br> 🟨 Implement `RacingEnv` class (`src/env/racing_env.py`) |
| **Phase 2: RL Algorithms**       | Study and implement baseline algorithms          | ⬜ Explore DQN, PPO, Actor-Critic <br> ⬜ Train cars on simple tracks using vector state spaces (position, velocity, distance sensors, etc.)                                                                                 |
| **Phase 3: Edge Case Testing**   | Test generalization of models                    | ⬜ Validate trained models on tough tracks <br> ⬜ If performance is poor, include tracks in training and retrain                                                                                                            |
| **Phase 4: Advanced Tracks**     | Push towards real-world style tracks             | ⬜ Create F1-inspired tracks <br> ⬜ Test trained cars on these tracks <br> ⬜ Compare lap times across algorithms                                                                                                            |
| **Phase 5: CNN + RL (Extended)** | Use raw pixels as input instead of state vectors | ⬜ Implement CNN + RL pipeline <br> ⬜ Benchmark vs. vector-state models                                                                                                                                                     |


## ✨ Future Ideas
- Improved GUI 
- Leaderboards for fastest lap times
- Procedurally generated tracks
