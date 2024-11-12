#include <iostream>
#include <vector>
#include <memory>

// Abstract base class
class Shape {
public:
    // Pure virtual function (no implementation in base class)
    virtual void draw() const = 0;
    
    // Virtual destructor to ensure proper cleanup of derived classes
    virtual ~Shape() = default;
};

// Derived class 'Line'
class Line : public Shape {
public:
    void draw() const override {
        std::cout << "Drawing a line." << std::endl;
    }
};

// Derived class 'Circle'
class Circle : public Shape {
public:
    void draw() const override {
        std::cout << "Drawing a circle." << std::endl;
    }
};

int main() {
    // Vector of unique_ptr to hold polymorphic objects of type Shape
    std::vector<std::unique_ptr<Shape>> shapes;

    // Push derived objects into the vector
    shapes.push_back(std::make_unique<Line>());
    shapes.push_back(std::make_unique<Circle>());

    // Iterate through the vector and call the draw function of each object
    for (const auto& shape : shapes) {
        shape->draw();
    }

    return 0;
}
