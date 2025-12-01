# Shopping-on-tuesday

![Python](https://img.shields.io/badge/-Python-blue?logo=python&logoColor=white) ![License](https://img.shields.io/badge/license-MIT-green)

## 📝 Description

Shopping-on-tuesday is a minimalist e-commerce platform designed to perfectly complement an Instagram-based stationary business. Built with Python, Flask, SQLAlchemy, and Jinja2, it offers a seamless and lightweight solution for showcasing and selling products. Key features include user authentication and smooth product handling, all wrapped in a clean and intuitive user interface.


## 🛠️ Tech Stack

- 🐍 Python


## 📦 Key Dependencies

```
Flask: 3.1.2
Flask-Login: 0.6.3
Flask-SQLALCHEMY: 3.1.1
Pillow: 12.0.0
Flask-WTF: 1.2.2
email-validator: latest
```

## 📁 Project Structure

```
.
├── LICENSE
├── app
│   ├── __init__.py
│   ├── admin
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── auth
│   │   ├── __init__.py
│   │   ├── forms.py
│   │   └── routes.py
│   ├── main
│   │   ├── __init__.py
│   │   └── routes.py
│   ├── models.py
│   ├── static
│   │   ├── css
│   │   │   └── style.css
│   │   └── js
│   │       └── main.js
│   └── templates
│       ├── admin
│       │   └── dashboard.html
│       ├── auth
│       │   └── login.html
│       ├── base.html
│       └── main
│           ├── index.html
│           ├── product_detail.html
│           └── products.html
├── config.py
├── requirements.txt
└── run.py
```

## 🛠️ Development Setup

### Python Setup
1. Install Python (v3.8+ recommended)
2. Create a virtual environment: `python -m venv venv`
3. Activate the environment:
   - Windows: `venv\Scripts\activate`
   - Unix/MacOS: `source venv/bin/activate`
4. Install dependencies: `pip install -r requirements.txt`


## 👥 Contributing

Contributions are welcome! Here's how you can help:

1. **Fork** the repository
2. **Clone** your fork: `git clone https://github.com/blu3-bird/Shopping-on-tuesday.git`
3. **Create** a new branch: `git checkout -b feature/your-feature`
4. **Commit** your changes: `git commit -am 'Add some feature'`
5. **Push** to your branch: `git push origin feature/your-feature`
6. **Open** a pull request

Please ensure your code follows the project's style guidelines and includes tests where applicable.

## Contributors ✨

Thanks goes to these wonderful people:

<!-- ALL-CONTRIBUTORS-LIST:START - Do not remove or modify this section -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/blu3-bird"><img src="https://avatars.githubusercontent.com/u/194448323?v=4?s=100" width="100px;" alt="Pardeep Singh"/><br /><sub><b>Pardeep Singh</b></sub></a><br /><a href="https://github.com/blu3-bird/Shopping-on-tuesday/commits?author=blu3-bird" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/MeloveGupta"><img src="https://avatars.githubusercontent.com/u/119809561?v=4?s=100" width="100px;" alt="Melove Gupta"/><br /><sub><b>Melove Gupta</b></sub></a><br /><a href="https://github.com/blu3-bird/Shopping-on-tuesday/commits?author=MeloveGupta" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/rooqidev"><img src="https://avatars.githubusercontent.com/u/227508742?v=4?s=100" width="100px;" alt="Rooqidev"/><br /><sub><b>Rooqidev</b></sub></a><br /><a href="https://github.com/blu3-bird/Shopping-on-tuesday/commits?author=rooqidev" title="Code">💻</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

## 📜 License

This project is licensed under the MIT License.

---

