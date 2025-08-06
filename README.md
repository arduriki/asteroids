# Asteroids Game - OOP Implementation

A classic Asteroids game implementation built with Python and Pygame, demonstrating fundamental Object-Oriented Programming concepts.

## 🎮 Game Overview

A recreation of the classic Asteroids arcade game where players control a spaceship, shooting asteroids that split into smaller pieces when hit.

## 📚 Object-Oriented Programming Concepts Demonstrated

### 1. **Inheritance**
- **Base Class**: `CircleShape` (circleshape.py:5) serves as an abstract base class inheriting from `pygame.sprite.Sprite`
- **Derived Classes**: 
  - `Player` (player.py:14) - The spaceship controlled by the player
  - `Asteroid` (asteroid.py:9) - Floating space rocks
  - `Shot` (shot.py:7) - Projectiles fired by the player
- **Implementation**: All game entities inherit common properties (position, velocity, radius) and methods from `CircleShape`

### 2. **Encapsulation**
- **Data Hiding**: Each class manages its own internal state
  - Player manages rotation, shooting cooldown timer (player.py:17-18)
  - Asteroids handle their own splitting logic (asteroid.py:19-35)
- **Private State Management**: Objects maintain their position, velocity, and radius internally

### 3. **Polymorphism**
- **Method Overriding**: Each derived class implements its own versions of:
  - `draw()` method - Different visual representations for each entity
  - `update()` method - Unique behavior for movement and interactions
- **Example**: Player draws as a triangle (player.py:20-21), Asteroid as a circle (asteroid.py:13-14)

### 4. **Abstraction**
- **Abstract Methods**: `CircleShape` defines abstract methods `draw()` and `update()` (circleshape.py:16-20)
- **Interface Design**: Base class provides a consistent interface for all game objects
- **Collision Detection**: Universal `collides_with()` method works for all circular objects (circleshape.py:22-23)

### 5. **Composition**
- **Object Relationships**: 
  - Player creates Shot objects when firing (player.py:52-55)
  - Asteroids create smaller asteroids when split (asteroid.py:32-35)
  - AsteroidField manages asteroid spawning (asteroidfield.py:9)

### 6. **Single Responsibility Principle**
- Each class has a focused purpose:
  - `Player`: Handle user input and ship movement
  - `Asteroid`: Manage asteroid behavior and splitting
  - `Shot`: Control projectile movement
  - `AsteroidField`: Manage asteroid spawning mechanics

### 7. **Sprite Groups (Design Pattern)**
- **Group Management**: Uses Pygame's sprite groups for efficient object management (main.py:17-20)
- **Container Pattern**: Classes use static containers for automatic group assignment (main.py:22-27)

### 8. **Game Loop Architecture**
- **Main Game Loop**: Demonstrates event-driven programming (main.py:32-57)
- **Delta Time**: Frame-independent movement using dt (main.py:30, 57)
- **Separation of Concerns**: Update logic, collision detection, and rendering are clearly separated

## 🔧 Technical Features

- **Collision Detection**: Distance-based circular collision system
- **Rate Limiting**: Shooting cooldown mechanism prevents spam
- **Dynamic Object Creation**: Asteroids split into smaller pieces
- **Frame Rate Control**: Locked to 60 FPS for consistent gameplay
- **Vector Mathematics**: Using Pygame's Vector2 for physics calculations

## 📖 Key Learning Outcomes

1. **Class Hierarchy Design**: Creating meaningful inheritance relationships
2. **Method Overriding**: Implementing specific behaviors while maintaining a common interface
3. **Object Lifecycle**: Managing object creation, updates, and destruction
4. **Event-Driven Programming**: Handling user input and game events
5. **Collision Systems**: Implementing efficient collision detection between objects
6. **State Management**: Each object maintains and updates its own state
7. **Code Reusability**: Leveraging inheritance to avoid code duplication

## 💻 Technologies Used

- **Python**: Core programming language
- **Pygame**: Game development framework
- **Object-Oriented Design**: Primary programming paradigm

## 🚀 Installation & Running

```bash
# Install dependencies
pip install pygame

# Run the game
python main.py
```

## 🎯 Controls

- **W/S**: Move forward/backward
- **A/D**: Rotate left/right
- **Space**: Shoot

## 🏗️ Design Decisions

- **Circular Hitboxes**: Simplified collision detection while maintaining gameplay accuracy
- **Inheritance over Composition**: Chose inheritance for sprite entities due to Pygame's sprite system
- **Constants Module**: Centralized game configuration for easy tuning
- **Group-Based Updates**: Efficient batch processing of game objects

---

*This project demonstrates proficiency in OOP principles through practical game development, showcasing clean code architecture and proper software design patterns.*