#include <string>
using namespace std;

class Person {
protected:
    string name;
    int age;

public:
    Person(string name, int age) {
        this->name = name;
        this->age = age;
    }

    virtual void displayInfo() {
        cout << "Name: " << name << ", Age: " << age;
    }
};

class Student : public Person {
private:
    string studentID;

public:
    Student(string name, int age, string studentID) : Person(name, age) {
        this->studentID = studentID;
    }

    void displayInfo() override {
        Person::displayInfo();
        cout << ", Student ID: " << studentID << endl;
    }
};

class Teacher : public Person {
private:
    string subject;

public:
    Teacher(string name, int age, string subject) : Person(name, age) {
        this->subject = subject;
    }

    void displayInfo() override {
        Person::displayInfo();
        cout << ", Subject: " << subject << endl;
    }
};

int main() {
    Student student("Ahmet", 20, "12345");
    Teacher teacher("Ayşe", 35, "Matematik");

    student.displayInfo();
    teacher.displayInfo();

    return 0;
}