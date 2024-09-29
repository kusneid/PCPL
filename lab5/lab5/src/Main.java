abstract class Figure {
    public abstract double GetArea(); // Метод для вычисления площади фигуры

    @Override
    public String toString() { 
        return "area= " + GetArea();
    }
}

class Rectangle extends Figure {
    private double width;
    private double height;

    public Rectangle(double width, double height) {
        this.width = width;
        this.height = height;
    }

    public double getWidth() {
        return width;
    }

    public double getHeight() {
        return height;
    }

    @Override
    public double GetArea() {
        return width * height;
    }

    @Override
    public String toString() {
        return "rectangle with that width and height " + getWidth() + " "+getHeight()+". " + super.toString();
    }
}

class Square extends Rectangle {
    public Square(double sideLength) {
        super(sideLength, sideLength);
    }

    @Override
    public String toString() {
        return "Square with that size " + getWidth() + ". " + super.toString();
    }
}


class Circle extends Figure {
    private double radius;

    public Circle(double radius) {
        this.radius = radius;
    }

    public double getRadius() {
        return radius;
    }

    @Override
    public double GetArea() {
        return Math.PI * radius * radius;
    }

    @Override
    public String toString() {
        return "Circle with radius " + radius + ". " + super.toString();
    }
}

// Интерфейс для печати информации
interface IPrint {
    void print();
}

// Основной класс программы
public class Main {
    public static void main(String[] args) {
        Rectangle rectangle = new Rectangle(5.0, 3.0);
        Square square = new Square(4.0);
        Circle circle = new Circle(2.5);

        printFigure(rectangle);
        printFigure(square);
        printFigure(circle);
    }

    public static void printFigure(Figure figure) {
        System.out.println(figure.toString());
    }
}
