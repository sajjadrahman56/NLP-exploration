Here's a concise summary of the **four access modifiers in Java** — `public`, `default` (no modifier), `private`, and `protected`:

### 1. **public**

- **Visibility**: Accessible from **anywhere** (within the same class, same package, different packages, subclasses, and unrelated classes).
- **Usage**: Use `public` when you want to allow access to the class or its members from any part of the program.
  
**Example**:
```java
public class Example {
    public int value;
    
    public void display() {
        System.out.println("Public method");
    }
}
```

### 2. **default** (No Modifier)

- **Visibility**: Accessible **only within the same package** (package-private). Classes, methods, and variables are visible to other classes in the same package but are **not visible to classes in different packages**.
- **Usage**: Use `default` when you want to restrict access to a class or its members to other classes within the same package but keep them hidden from outside the package.

**Example**:
```java
class Example { // Default class
    int value; // Default field (no modifier)
    
    void display() { // Default method
        System.out.println("Default method");
    }
}
```

### 3. **private**

- **Visibility**: Accessible **only within the same class**. A `private` member is completely hidden from any other class, including subclasses and classes in the same package.
- **Usage**: Use `private` when you want to ensure that a field or method is not accessible or modifiable from outside its own class. It's often used for **encapsulation** to protect the internal state of the object.

**Example**:
```java
public class Example {
    private int value; // Private field
    
    private void display() { // Private method
        System.out.println("Private method");
    }
}
```

### 4. **protected**

- **Visibility**:
  - Accessible within the **same package** (like `default`).
  - Accessible in **subclasses** (even in different packages), but only through a **subclass reference**.
- **Usage**: Use `protected` when you want to allow access to members within the same package and give **subclasses** access (even outside the package), while restricting access from unrelated classes.

**Example**:
```java
public class Parent {
    protected int value; // Protected field
    
    protected void display() { // Protected method
        System.out.println("Protected method");
    }
}
```

### **Comparison Summary Table**:

| Modifier   | Same Class | Same Package | Subclass (Different Package) | Other Classes (Different Package) |
|------------|------------|--------------|------------------------------|------------------------------------|
| **public**    | ✔️          | ✔️            | ✔️                            | ✔️                                  |
| **default**   | ✔️          | ✔️            | ❌                            | ❌                                  |
| **protected** | ✔️          | ✔️            | ✔️ (via subclass reference)   | ❌                                  |
| **private**   | ✔️          | ❌            | ❌                            | ❌                                  |

### **Key Points**:
- `public`: Accessible from **anywhere**.
- `default`: Accessible only **within the same package**.
- `protected`: Accessible within the same package and **subclasses** (via subclass reference).
- `private`: Accessible only **within the same class**, completely hidden from outside.

Each modifier is used based on the **level of access control** you want to enforce for your fields and methods, helping achieve **encapsulation**, **inheritance**, and **information hiding**.