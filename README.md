## Overview
EcoSim is an object-oriented Python project simulating a dynamic predator-prey ecosystem with graphical visualization. It demonstrates core OOP principles including inheritance, encapsulation, polymorphism, and exception handling, all built on a custom game engine using Python and Tkinter.

In this simulation, wombats and snakes interact within a 12x10 grid of land tiles (dirt and sand). Wombats graze on grass, while snakes hunt wombats. Grass spreads over dirt tiles, creating a balanced and evolving ecosystem.

---

## Features

- **Object-Oriented Design**  
  Implements abstraction, inheritance, polymorphism, and encapsulation across animals, plants, and tiles.

- **Graphical Interface**  
  Uses a custom game engine built with Tkinter to render real-time simulation graphics.

- **Dynamic Ecosystem**  
  Animals move autonomously, seek food, reproduce, and interact realistically.

- **Exception Handling**  
  Custom `OutOfBoundsException` ensures animals remain within simulation bounds.

- **Extensible Architecture**  
  Easily add new animals, plants, or terrain types following established OOP patterns.

---

## Installation and Running Instructions
### Prerequisites

- Python 3.7 or higher installed  
  Check Python version and package(pip) by running:
  ```bash
  python --version
  pip --version
- Install Pillow package
  ```bash
  pip install pillow

### Running the Simulation
- Start the program with:
  ```bash
  python ecosim.py

## Testing
Unit test are implemented for the vector2D class. To run the unittest:
```bash
python -m unittest vector2DTestCase.py
