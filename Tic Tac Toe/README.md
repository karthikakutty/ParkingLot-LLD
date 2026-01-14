# Tic-Tac-Toe Game Engine (Python | LLD | Design Patterns)

A console-based Tic-Tac-Toe game engine built using clean **Object-Oriented Design** and **Low-Level Design (LLD)** principles.  
The project focuses on **architecture, extensibility, and state management**, rather than just gameplay.

---

## 🚀 Key Features

- Turn-based Tic-Tac-Toe engine (N x N supported)
- Human vs Bot gameplay
- Multiple bot difficulty levels (Easy, Medium, Hard – strategy-based)
- Pluggable winning strategies (Row, Column, Diagonal)
- Snapshot-based Undo functionality (Memento Pattern)
- Clean separation of responsibilities (Controller, Service, Model)
- Extensible architecture for future enhancements

---

## 🧠 Design Highlights

### 1. Strategy Pattern
- Used for:
  - Winning logic (Row, Column, Diagonal)
  - Bot behavior (Easy / Medium / Hard)
- Enables adding new strategies without modifying existing code

### 2. Factory Pattern
- `BotFactory` dynamically creates bot strategies based on difficulty level
- Decouples bot creation from game logic

### 3. Memento Pattern (Snapshot-based Undo)
- Full game state (board, moves, turn, status) is captured before each move
- Enables multi-level undo with safe state rollback

### 4. Layered Architecture
- **Controller** → Handles user interaction
- **Service** → Contains game logic
- **Model** → Represents core entities (Game, Board, Cell, Player)

---

## 🧩 Project Structure

### src/
### 1. controller/
- **GameController.py** → Handles user input and game flow
### 2. services/
- **GameServices.py** → Core game logic and state management
### 3. models/
- **Game.py** → Game state and metadata
- **Board.py** → Board representation
- **Cell.py** → Individual cell logic
- **Player.py** → Human player model
- **Bot.py** → Bot player abstraction
- **GameSnapshot.py** → Snapshot for undo (Memento pattern)
### 4.helper/
- **Strategy/**
  - **botStgy/** → Bot strategies (Easy / Medium / Hard)
      - **BotStgy.py** → Base strategy interface
        1. **Easy.py** → Easy bot (first available move)
        2. **Medium.py** → Medium bot (win / block strategy)
        3. **Hard.py** → Hard bot (Minimax-based strategy)

  - **winningStgy/** → Winning strategies (Row / Column / Diagonal)
      1. **rowWS.py** → Row-based winning strategy
      2. **colWS.py** → Column-based winning strategy
      3. **diagonalWS.py** → Diagonal winning strategy

- **BotFactory.py** → Factory for bot strategy creation
### 5. main.py # Application entry point