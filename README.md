# Just Light Development (JLD)

Just Light Development (JLD) is a custom asynchronous Python web framework built on ASGI, designed to be lightweight and efficient. It leverages the power of Jinja2 for templating and Uvicorn for high-performance ASGI server execution. With support for both function-based and class-based views, JLD provides a simple yet robust platform for developing modern web applications.

---

## 🚀 Features

- **Asynchronous Request Handling**: Built on the ASGI standard for scalable, high-performance web applications.
- **Routing**: Dynamic routing with support for GET and POST methods.
- **Template Rendering**: Built-in integration with Jinja2 for dynamic HTML rendering.
- **Function-Based and Class-Based Views**: Flexibility to define views in the style you prefer.
- **Lightweight and Fast**: Designed to be minimal yet powerful, running on Uvicorn.

---

## 📚 Table of Contents

- [Getting Started](#getting-started)
- [How It Works](#how-it-works)
- [Installation](#installation)
- [Usage](#usage)
- [Features in Detail](#features-in-detail)
- [Contributing](#contributing)
- [License](#license)

---

## 📦 Installation

You can install the framework directly from GitHub using pip:
```bash
pip3 install git+https://github.com/Subhodip1307/Just_Light_Development
```

---

## 🛠 Usage

### Routing
Define your routes using the `@app.route()` decorator. Specify the HTTP methods you want to support:
```python
from jld import Template
from jld import app as APP
render = Template()
app=APP()
@app.route("/submit", methods=["POST"])
async def submit(request):
    name = request.POST.get("name", "Anonymous")
    return render.render("result.html", {"name": name})
```

### Template Rendering
Use Jinja2 to render dynamic HTML templates:
```python
from jld import Template
from jld import app as APP
render = Template()
app=APP()
@app.route("/submit", methods=["POST"])
async def submit(request):
    name = request.POST.get("name", "Anonymous")
    return render.render("result.html", {"name": name})
```

---

## 🌟 Features in Detail

1. **Dynamic Routing**:
   - Easily map URLs to Python functions or methods.
   - Supports multiple HTTP methods (GET, POST, etc.).

2. **Request Handling**:
   - Access GET and POST data through the `Request` object.
   - Parse headers, query strings, and request bodies effortlessly.

3. **Template Rendering with Jinja2**:
   - Use the `Template` class to render HTML with dynamic data.
   - Example:
     ```python
     render.render("template.html", {"key": "value"})
     ```

4. **ASGI Compatibility**:
   - Fully compatible with ASGI servers like Uvicorn, ensuring high performance and scalability.

5. **Class-Based Views**:
   - Define reusable, modular views using classes (future scope).

---

## 🤝 Contributing

We welcome contributions! If you'd like to improve this framework, feel free to:

1. Fork the repository.
2. Create a new branch:
   ```bash
   git checkout -b feature/your-feature-name
   ```
3. Commit your changes:
   ```bash
   git commit -m "Add your message here"
   ```
4. Push to the branch:
   ```bash
   git push origin feature/your-feature-name
   ```
5. Open a pull request.

---

## 📜 License

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

---

## 🙌 Acknowledgments

- **[Jinja2](https://jinja.palletsprojects.com/)**: For its powerful templating capabilities.
- **[Uvicorn](https://www.uvicorn.org/)**: For providing a lightning-fast ASGI server.
- **[Python](https://www.python.org/)**: The language that makes it all possible.

---

Thank you for using Just Light Development! 🌟
