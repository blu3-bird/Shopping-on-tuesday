<!-- TOP BANNER -->
<div align="center">
  <img src="https://capsule-render.vercel.app/api?type=waving&color=0:ff00c8,100:00c6ff&height=160&text=Shopping-on-Tuesday&fontSize=48&fontColor=ffffff&animation=twinkling"/>
</div>


<p align="center">
  <img src="https://img.shields.io/badge/-Python-blue?logo=python&logoColor=white" />
  <img src="https://img.shields.io/badge/License-MIT-green" />
  <img src="https://img.shields.io/badge/Flask-App-orange?logo=flask&logoColor=white" />
</p>


## 📝 Description

Shopping-on-Tuesday is a clean and beginner-friendly e-commerce platform built for Instagram-based stationery shops.  
Powered by **Flask + SQLAlchemy**, it delivers a smooth workflow — from browsing products to signing in — without unnecessary overhead.

If you want something minimal but functional, this project is the sweet spot.

---

## 🛠️ Tech Stack

- 🐍 Python  
- 🔥 Flask  
- 🗄️ SQLAlchemy  
- 🎨 Jinja2  
- 🌐 HTML / CSS / JavaScript  

---

## 📦 Key Dependencies

Here’s the clean format you wanted:

- **Flask** → `3.1.2`  
- **Flask-Login** → `0.6.3`  
- **Flask-SQLAlchemy** → `3.1.1`  
- **Flask-WTF** → `1.2.2`  
- **Pillow** → `12.0.0`  
- **Email Validator** → `latest`  

---

## 📁 Project Structure

```
Shopping-on-tuesday/
├── .all-contributorsrc
├── config.py
├── CONTRIBUTORS.md
├── LICENSE
├── README.md
├── requirements.txt
├── run.py
└── app/
    ├── constants.py
    ├── models.py
    ├── __init__.py
    ├── templates/
    │   ├── base.html
    │   ├── main/
    │   │   ├── index.html
    │   │   ├── products.html
    │   │   └── product_detail.html
    │   ├── errors/
    │   │   ├── 400.html
    │   │   └── 500.html
    │   ├── components/
    │   │   └── trust_badges.html
    │   ├── auth/
    │   │   └── login.html
    │   └── admin/
    │       ├── add_product.html
    │       ├── dashboard.html
    │       ├── edit_product.html
    │       └── product_list.html
    ├── main/
    │   ├── routes.py
    │   └── __init__.py
    ├── auth/
    │   ├── forms.py
    │   ├── routes.py
    │   └── __init__.py
    ├── admin/
    │   ├── forms.py
    │   ├── routes.py
    │   └── __init__.py
    └── static/
        ├── js/
        │   └── main.js
        └── css/
            ├── error.css
            ├── add_edit_product.css
            ├── base.css
            ├── dashboard.css
            ├── index.css
            ├── products.css
            ├── product_detail.css
            ├── product_list.css
            ├── style.css
            └── super_admin_login.css
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

## 🌟 Contributors

<!-- ALL-CONTRIBUTORS-LIST:START -->
<!-- prettier-ignore-start -->
<!-- markdownlint-disable -->
<table>
  <tbody>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/blu3-bird"><img src="https://avatars.githubusercontent.com/u/194448323?v=4?s=100" width="100px;" alt="Pardeep Singh"/><br /><sub><b>Pardeep Singh</b></sub></a><br /><a href="https://github.com/blu3-bird/Shopping-on-tuesday/commits?author=blu3-bird" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/ZainabTravadi"><img src="https://avatars.githubusercontent.com/u/195310178?v=4?s=100" width="100px;" alt="Zainab Travadi"/><br /><sub><b>Zainab Travadi</b></sub></a><br /><a href="https://github.com/blu3-bird/Shopping-on-tuesday/commits?author=ZainabTravadi" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/etaiami09-cmd"><img src="https://avatars.githubusercontent.com/u/235846178?v=4?s=100" width="100px;" alt="Etai codes"/><br /><sub><b>Etai codes</b></sub></a><br /><a href="https://github.com/blu3-bird/Shopping-on-tuesday/commits?author=etaiami09-cmd" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/MeloveGupta"><img src="https://avatars.githubusercontent.com/u/119809561?v=4?s=100" width="100px;" alt="Melove Gupta"/><br /><sub><b>Melove Gupta</b></sub></a><br /><a href="https://github.com/blu3-bird/Shopping-on-tuesday/commits?author=MeloveGupta" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/rooqidev"><img src="https://avatars.githubusercontent.com/u/227508742?v=4?s=100" width="100px;" alt="Rooqidev"/><br /><sub><b>Rooqidev</b></sub></a><br /><a href="https://github.com/blu3-bird/Shopping-on-tuesday/commits?author=rooqidev" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/Padhmashikha"><img src="https://avatars.githubusercontent.com/u/219302428?v=4?s=100" width="100px;" alt="Padhmashikha Iyapparaju"/><br /><sub><b>Padhmashikha Iyapparaju</b></sub></a><br /><a href="https://github.com/blu3-bird/Shopping-on-tuesday/commits?author=Padhmashikha" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/MVGRAO"><img src="https://avatars.githubusercontent.com/u/134282307?v=4?s=100" width="100px;" alt="Venkata Gajapathi Rao Mugunda"/><br /><sub><b>Venkata Gajapathi Rao Mugunda</b></sub></a><br /><a href="https://github.com/blu3-bird/Shopping-on-tuesday/commits?author=MVGRAO" title="Code">💻</a></td>
    </tr>
    <tr>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/leotrevizo37"><img src="https://avatars.githubusercontent.com/u/63759139?v=4?s=100" width="100px;" alt="Leo Trevizo"/><br /><sub><b>Leo Trevizo</b></sub></a><br /><a href="https://github.com/blu3-bird/Shopping-on-tuesday/commits?author=leotrevizo37" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/MalathiBalaraman31"><img src="https://avatars.githubusercontent.com/u/149077958?v=4?s=100" width="100px;" alt="Malathi "/><br /><sub><b>Malathi </b></sub></a><br /><a href="https://github.com/blu3-bird/Shopping-on-tuesday/commits?author=MalathiBalaraman31" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://anujcom.vercel.app/"><img src="https://avatars.githubusercontent.com/u/154220750?v=4?s=100" width="100px;" alt="Anuj Kumar"/><br /><sub><b>Anuj Kumar</b></sub></a><br /><a href="https://github.com/blu3-bird/Shopping-on-tuesday/commits?author=Anujpandey12345" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://github.com/matthiastz"><img src="https://avatars.githubusercontent.com/u/23010759?v=4?s=100" width="100px;" alt="Matthias Tietz"/><br /><sub><b>Matthias Tietz</b></sub></a><br /><a href="https://github.com/blu3-bird/Shopping-on-tuesday/commits?author=matthiastz" title="Code">💻</a></td>
      <td align="center" valign="top" width="14.28%"><a href="https://xlebovoz-links.vercel.app/"><img src="https://avatars.githubusercontent.com/u/189365255?v=4?s=100" width="100px;" alt="XLEB"/><br /><sub><b>XLEB</b></sub></a><br /><a href="https://github.com/blu3-bird/Shopping-on-tuesday/commits?author=xlebovoz" title="Documentation">📖</a></td>
    </tr>
  </tbody>
</table>

<!-- markdownlint-restore -->
<!-- prettier-ignore-end -->

<!-- ALL-CONTRIBUTORS-LIST:END -->

---

## 📜 License

This project is licensed under the **MIT License**.

---

<!-- BOTTOM BANNER -->
<div align="center">
<img src="https://capsule-render.vercel.app/api?type=waving&color=0:ff00c8,100:00c6ff&height=160&section=footer&fontSize=0&animation=twinkling"/>
</div>

