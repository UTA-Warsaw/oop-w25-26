public class Person
{
    public string Name { get; set; }   // auto-properties
    public int Age { get; set; }

    public Person(string name, int age)   // constructor
    {
        Name = name;
        Age = age;
    }
}
