# 📝 Md-Parser-Html

[![Python](https://img.shields.io/badge/Python-3.6%2B-blue.svg)](https://www.python.org/)
[![Licence MIT](https://img.shields.io/badge/Licence-MIT-green.svg)](LICENSE)
![Statut](https://img.shields.io/badge/statut-Inactif-red.svg)
![Made with ❤️](https://img.shields.io/badge/Made%20with-%E2%9D%A4-red)

> Projet réalisé dans le cadre du TP Markdown → HTML à l'ESGI  

---

## Description

`mdparsertp` est un parseur Markdown vers HTML responsive, développé en Python.  
Il permet de convertir un ou plusieurs fichiers `.md` en pages HTML statiques et stylisées.

---

## ⚙️ Installation rapide

```bash
git clone https://github.com/Tyno14/Md-Parser-Html.git
cd Md-Parser-Html
python3 -m venv venv
source venv/bin/activate
pip install .
```

## 🧪 Commandes d'utilisation

```bash
mdparsertp fichier.md --output mon_site --title "Titre Perso" --theme green --darkmode
```

| Commande                                             | Description                                             |
|------------------------------------------------------|---------------------------------------------------------|
| `mdparsertp [chemin/fichier.md]`                              | Conversion simple (par défaut, sortie = `site/`)       |
| `mdparsertp [chemin/fichier.md] --output test1`               | Dossier de sortie personnalisé                         |
| `mdparsertp [chemin/fichier.md] --title "Test Titre"`         | Titre HTML forcé                                       |
| `mdparsertp [chemin/fichier.md] --theme blue`                 | Thème forcé (bleu pastel)                              |
| `mdparsertp [chemin/fichier.md] --darkmode`                   | Active le mode sombre                                  |
| `mdparsertp [chemin/fichier.md] --theme green --darkmode`     | Combine `--theme` et `--darkmode`                      |
| `mdparsertp [Dossier/] --multipage`                         | Génère une page HTML par `.md`                         |
| `mdparsertp [Dossier/]--multipage --theme orange`          | Multidoc avec thème orange                             |
| `mdparsertp [Dossier/] --multipage --darkmode`              | Multidoc + mode sombre                                 |
| `mdparsertp [Dossier/] --multipage --output final --darkmode --theme green` | Tout combiné |

## 📦 Dépendances

- Python ≥ 3.6

- highlight.js (CDN)

## 🧑‍💻 Auteur

Tyno14 2025
