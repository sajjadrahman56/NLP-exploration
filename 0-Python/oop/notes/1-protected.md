### Let's clarify your question:

1. **Is the following allowed inside a class?**  
   **`parentRef.protectedMethod(); // Compile-time error, because you are outside the package`**
   
   - The answer depends on **whether this code is inside or outside the package** where the `Parent` class is defined, and whether the access is through a **subclass reference** or a **parent class reference**.

2. **Does the `Parent` class never allow a reference to call a `protectedMethod()` outside its package?**
   
   - Yes, a **parent class reference** (`Parent parentRef = new Parent()`) **cannot** call a `protected` method **outside the package**. However, a **child class reference** (e.g., `Child childRef = new Child()`) can access the `protected` method, even if you're outside the package, because the child class inherits the method.

---

### Breakdown of `protected` Access in Java

#### Scenario 1: **Accessing `protected` Method Inside the Same Package**

If you're inside the same package as the `Parent` class, you can access the `protected` method using a reference of the `Parent` class or any subclass. For example:

```java
package parentPackage;

public class Parent {
    protected void protectedMethod() {
        System.out.println("Protected method in Parent class");
    }

    public static void main(String[] args) {
        Parent parentRef = new Parent();
        parentRef.protectedMethod(); // This works fine because we're inside the same package
    }
}
```

This works because **inside the same package**, `protected` members behave similarly to `public` members for any class within the same package.

#### Scenario 2: **Accessing `protected` Method Outside the Package (Wrong Approach)**

Now, if you are **outside the package** and try to access the `protected` method using a **parent class reference**, it will result in a **compile-time error**. For example:

```java
package childPackage;

import parentPackage.Parent;

public class OtherClass {
    public static void main(String[] args) {
        Parent parentRef = new Parent();
        parentRef.protectedMethod(); // Compile-time error: 'protectedMethod()' has protected access in 'Parent'
    }
}
```

This will give a compile-time error because the `Parent` class' `protected` members are not accessible via a `Parent` class reference from outside the package.

#### Scenario 3: **Accessing `protected` Method Outside the Package (Correct Approach)**

The correct approach to access a `protected` method from **outside the package** is to use a **child class reference**, like this:

```java
package childPackage;

import parentPackage.Parent;

public class Child extends Parent {
    public static void main(String[] args) {
        Child childRef = new Child();
        childRef.protectedMethod(); // This works because child class inherits the protected method
    }
}
```

This works because `Child` extends `Parent`, and a subclass can access the `protected` members of its superclass even when outside the package. Here, the `protectedMethod()` is inherited by `Child`, and since we are using the `Child` reference, it is accessible.

---

### Real-life Scenario: When Do We Use `protected` Access Modifier?

The `protected` access modifier is often used in **inheritance scenarios** where you want to:
1. **Restrict direct access** to certain members from outside the class (especially from code in other packages).
2. **Allow controlled access** to these members in subclasses, even if the subclass is in a different package.

#### Common Use Cases:

1. **Framework Development**:
   - When building frameworks or libraries, you often want to provide certain functionality that can be extended by the framework users, but you don't want that functionality to be exposed to everyone directly. `protected` methods allow subclasses to access and customize the behavior, but other classes cannot directly invoke those methods.

   Example:
   ```java
   public abstract class Shape {
       protected abstract void draw(); // Can only be accessed and overridden by subclasses

       public void render() {
           // some rendering code
           draw(); // Calls the protected draw method in the subclass
       }
   }

   public class Circle extends Shape {
       @Override
       protected void draw() {
           System.out.println("Drawing a Circle");
       }
   }
   ```

2. **Inheritance with Controlled Access**:
   - In complex hierarchies, you may have base classes that contain sensitive logic or methods. These methods should only be accessible by classes extending the base class but not by other unrelated classes.
   
   Example:
   ```java
   public class Account {
       protected double balance; // Only accessible to subclasses

       public void deposit(double amount) {
           balance += amount;
       }
   }

   public class SavingsAccount extends Account {
       public void addInterest() {
           balance += balance * 0.05; // Accessing the protected balance field
       }
   }
   ```

3. **Template Method Design Pattern**:
   - In design patterns like **Template Method**, you want to provide a basic algorithm in the parent class but allow subclasses to customize parts of it by overriding `protected` methods.

   Example:
   ```java
   public abstract class DataProcessor {
       // Template method
       public final void processData() {
           fetchData();
           process();
           saveData();
       }

       protected abstract void fetchData(); // Subclasses must provide implementation
       protected abstract void process();
       protected abstract void saveData();
   }

   public class CSVProcessor extends DataProcessor {
       @Override
       protected void fetchData() {
           System.out.println("Fetching data from CSV file");
       }

       @Override
       protected void process() {
           System.out.println("Processing CSV data");
       }

       @Override
       protected void saveData() {
           System.out.println("Saving processed CSV data");
       }
   }
   ```

---

### **Summary of Key Points:**

- **`protected` members** can be accessed within the same package or in subclasses (even from different packages).
- **From outside the package**, you **cannot access a `protected` method** using a **parent class reference** (`Parent parentRef = new Parent()`).
- You **can** access a `protected` method using a **child class reference** (`Child childRef = new Child()`), even if you are outside the package.
- The `protected` modifier is often used in scenarios involving inheritance to provide controlled access to methods or fields while keeping them hidden from other parts of the code that shouldn't access them.

In real-world applications, the `protected` modifier is most useful when you want to enable extension of functionality (inheritance) while keeping certain implementation details restricted to subclasses.