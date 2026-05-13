'''

differecen in abstract class and interface

On one hand, An abstract class is a class that cannot be instantiated and is designed to be subclassed by other classes.

abstract class Animal {
    abstract void sound();
}

Animal a = new Animal(); ❌

But another class must extend it:

class Dog extends Animal {
    void sound() {
        System.out.println("Bark");
    }
}

Dog d = new Dog(); ✅
or
Animal d = new Dog(); ✅

We cannot create objects directly from an abstract class. It only acts as a base/template for child classes.

- It contains abstract methods, which have no implementation in the abstract class and must be implemented by any concrete subclass. 

- Also have concrete methods, which have a defined implementation in the abstract class and are inherited by any concrete subclass.


On the other hand, An interface, is a collection of abstract methods that define a contract for a class to implement.

'''

'''
Example

interface Vehicle {
    void start();
    void stop();
}

class Car implements Vehicle {
    public void start() {
        System.out.println("Car started");
    }
    public void stop() {
        System.out.println("Car stopped");
    }
}

Vehicle v = new Car(); ✅


public abstract class Shape {

    private String color;

    public String getColor() {
        return color;
    }

    public void setColor(String color) {
        this.color = color;
    }

    public abstract double getArea();
}

class Circle extends Shape {

    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    @Override
    public double getArea() {
        return Math.PI * radius * radius;
    }
}

class Rectangle extends Shape {

    private double width;
    private double height;

    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }

    @Override
    public double getArea() {
        return width * height;
    }
}

Shape shape = new Circle(5); ✅
Circle circle = new Circle(5); ✅

'''