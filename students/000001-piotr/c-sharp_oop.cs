using System;

public class Person
{
    // Fields
    public string Name;
    public int Age;

    // Constructor
    public Person(string name, int age)
    {
        Name = name;
        Age = age;
    }
}

public class Program
{
    public static void Main()
    {
        Person p1 = new Person("Piotr Brudny", 41);

        Console.WriteLine("Name: " + p1.Name + " Age: " + p1.Age);
    }
}

